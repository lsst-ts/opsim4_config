"""
This is an example configuration for the Feature Based Scheduler. The if statement is used to bypass the configuration
expect when instantiated by the Feature Scheduler Driver. Note that we import and fill in a SurveyTopology class that
informs the (S)OCS about the projects defined on the configuration.

The only things that cannot be changed here are the names of the variables survey_topoly and scheduler. It is possible
as those are expected by the Driver. The way those objects are configured are entirely up to the user though.

07/2018 - Version 0
"""
import numpy as np
import lsst.sims.featureScheduler as fs
import healpy as hp
from lsst.sims.utils import _hpid2RaDec
from lsst.ts.scheduler.kernel import SurveyTopology
import time

t0 = time.time()

if __name__ == 'config':
    # Get rid of the silly north stripe
    def standard_goals(nside=None):
        """
        A quick function to generate the "standard" goal maps.
        """
        # Find the number of healpixels we expect to observe per observation
        if nside is None:
            nside = fs.set_default_nside()

        result = {}
        result['u'] = fs.generate_goal_map(nside=nside, NES_fraction=0.,
                                           WFD_fraction=0.31, SCP_fraction=0.15,
                                           GP_fraction=0.15, WFD_upper_edge_fraction=0.,
                                           generate_id_map=True)
        result['g'] = fs.generate_goal_map(nside=nside, NES_fraction=0.2,
                                           WFD_fraction=0.44, SCP_fraction=0.15,
                                           GP_fraction=0.15, WFD_upper_edge_fraction=0.,
                                           generate_id_map=True)
        result['r'] = fs.generate_goal_map(nside=nside, NES_fraction=0.46,
                                           WFD_fraction=1.0, SCP_fraction=0.15,
                                           GP_fraction=0.15, WFD_upper_edge_fraction=0.,
                                           generate_id_map=True)
        result['i'] = fs.generate_goal_map(nside=nside, NES_fraction=0.46,
                                           WFD_fraction=1.0, SCP_fraction=0.15,
                                           GP_fraction=0.15, WFD_upper_edge_fraction=0.,
                                           generate_id_map=True)
        result['z'] = fs.generate_goal_map(nside=nside, NES_fraction=0.4,
                                           WFD_fraction=0.9, SCP_fraction=0.15,
                                           GP_fraction=0.15, WFD_upper_edge_fraction=0.,
                                           generate_id_map=True)
        result['y'] = fs.generate_goal_map(nside=nside, NES_fraction=0.,
                                           WFD_fraction=0.9, SCP_fraction=0.15,
                                           GP_fraction=0.15,
                                           WFD_upper_edge_fraction=0.,
                                           generate_id_map=True)

        return result

    survey_topology = SurveyTopology()
    survey_topology.num_general_props = 4
    survey_topology.general_propos = ["NorthEclipticSpur", "SouthCelestialPole", "WideFastDeep", "GalacticPlane"]
    survey_topology.num_seq_props = 1
    survey_topology.sequence_propos = ["DeepDrillingCosmology1"]

    nside = fs.set_default_nside(nside=32)

    # Let's set up some alt_az maps
    # XXX--this is an initial guess at what reasoable blocks might look like!
    alt_az_blockmaps = []
    hpids = np.arange(hp.nside2npix(nside))
    az, alt = _hpid2RaDec(nside, hpids)

    # XXX--seem like reasonable numbers, but who knows if they are hte best!
    alt_low_limit = np.radians(20.)
    alt_high_limit = np.radians(82.)
    az_half_width = np.radians(15.)

    blank_map = hpids * 0.
    good = np.where(((az > 2. * np.pi - az_half_width) | (az < az_half_width)) &
                    (alt > alt_low_limit) & (alt < alt_high_limit))
    new_map = blank_map + 0
    new_map[good] = 1
    alt_az_blockmaps.append(new_map)

    good = np.where(((az > np.pi - az_half_width) & (az < np.pi + az_half_width)) &
                    (alt > alt_low_limit) & (alt < alt_high_limit))
    new_map = blank_map + 0
    new_map[good] = 1
    alt_az_blockmaps.append(new_map)

    # let's make some finer grained steps. Bring up the lower limit a bit.
    alt_high_limit = np.radians(75.)
    alt_low_limit = np.radians(35.)

    steps = np.arange(20, 330, 20)
    for step in steps:
        good = np.where((az > np.radians(step)) & (az < np.radians(step) + az_half_width * 2) &
                        (alt > alt_low_limit) & (alt < alt_high_limit))
        new_map = blank_map + 0
        new_map[good] = 1
        alt_az_blockmaps.append(new_map)

    # get rid of silly northern strip.
    target_map = standard_goals(nside=nside)

    # List to hold all the surveys (for easy plotting later)
    surveys = []

    # Set up observations to be taken in blocks
    filter1s = ['u', 'g', 'r', 'i', 'y']
    filter2s = [None, 'r', 'i', 'z', None]
    pair_surveys = []
    for filtername, filtername2 in zip(filter1s, filter2s):
        bfs = []
        bfs.append(fs.M5_diff_basis_function(filtername=filtername, nside=nside))
        if filtername2 is not None:
            bfs.append(fs.M5_diff_basis_function(filtername=filtername2, nside=nside))
        bfs.append(fs.Target_map_basis_function(filtername=filtername,
                                                target_map=target_map[filtername],
                                                out_of_bounds_val=hp.UNSEEN, nside=nside))
        if filtername2 is not None:
            bfs.append(fs.Target_map_basis_function(filtername=filtername2,
                                                    target_map=target_map[filtername2],
                                                    out_of_bounds_val=hp.UNSEEN, nside=nside))
        bfs.append(fs.Slewtime_basis_function(filtername=filtername, nside=nside))
        # XXX--put a huge boost on staying in the filter. Until I can tier surveys as list-of-lists
        weights = np.array([3.0, 3.0, 0.3, 0.3, 3.])
        if filtername2 is None:
            # Need to scale weights up so filter balancing still works.
            weights = np.array([6.0, 0.6, 3.])
        # XXX-
        # This is where we could add a look-ahead basis function to include m5_diff in the future.
        # Actually, having a near-future m5 would also help prevent switching to u or g right at twilight?
        # Maybe just need a "filter future" basis function?
        if filtername2 is None:
            survey_name = 'block, %s' % filtername
        else:
            survey_name = 'block, %s%s' % (filtername, filtername2)
        surveys.append(fs.Block_survey(bfs, weights, filtername=filtername, filter2=filtername2,
                                       dither=True, nside=nside, ignore_obs='DD',
                                       alt_az_masks=alt_az_blockmaps,
                                       survey_note=survey_name))
        pair_surveys.append(surveys[-1])

    # Let's set up some standard surveys as well to fill in the gaps. This is my old silly masked version.
    # It would be good to put in Tiago's verion and lift nearly all the masking. That way this can also
    # chase sucker holes.
    filters = ['u', 'g', 'r', 'i', 'z', 'y']
    greedy_surveys = []
    for filtername in filters:
        bfs = []
        bfs.append(fs.M5_diff_basis_function(filtername=filtername, nside=nside))
        bfs.append(fs.Target_map_basis_function(filtername=filtername,
                                                target_map=target_map[filtername],
                                                out_of_bounds_val=hp.UNSEEN, nside=nside))

        bfs.append(fs.North_south_patch_basis_function(zenith_min_alt=50., nside=nside))
        bfs.append(fs.Slewtime_basis_function(filtername=filtername, nside=nside))
        bfs.append(fs.Strict_filter_basis_function(filtername=filtername))

        weights = np.array([3.0, 0.3, 1., 3., 3.])
        # Might want to try ignoring DD observations here, so the DD area gets covered normally--DONE
        surveys.append(fs.Greedy_survey_fields(bfs, weights, block_size=1, filtername=filtername,
                                               dither=True, nside=nside, ignore_obs='DD'))
        greedy_surveys.append(surveys[-1])

    # Set up the DD surveys
    # dd_surveys = []
    dd_surveys = fs.generate_dd_surveys()
    surveys.extend(dd_surveys)

    survey_list_o_lists = [pair_surveys, greedy_surveys]
    # survey_list_o_lists = [dd_surveys, pair_surveys, greedy_surveys]

    scheduler = fs.Core_scheduler(survey_list_o_lists, nside=nside)
