"""
This is an example configuration for the Feature Based Scheduler. The if statement is used to bypass the configuration
expect when instantiated by the Feature Scheduler Driver. Note that we import and fill in a SurveyTopology class that
informs the (S)OCS about the projects defined on the configuration.

The only things that cannot be changed here are the names of the variables survey_topoly and scheduler. It is possible
as those are expected by the Driver. The way those objects are configured are entirely up to the user though.

07/2018 - Version 0
"""
import numpy as np
import healpy as hp
import lsst.sims.featureScheduler as fs
from lsst.ts.scheduler.kernel import SurveyTopology

if __name__ == 'config':
    survey_topology = SurveyTopology()
    survey_topology.num_general_props = 4
    survey_topology.general_propos = ["NorthEclipticSpur", "SouthCelestialPole", "WideFastDeep", "GalacticPlane"]
    survey_topology.num_seq_props = 1
    survey_topology.sequence_propos = ["DeepDrillingCosmology1"]

    target_maps = {}
    nside = fs.set_default_nside(nside=32)  # Required

    target_maps['i'] = fs.generate_goal_map(NES_fraction=.8,
                                            WFD_fraction=1.0, SCP_fraction=.8,
                                            GP_fraction=.8,
                                            WFD_upper_edge_fraction=0.0,
                                            nside=nside,
                                            generate_id_map=True)

    cloud_map = fs.utils.generate_cloud_map(target_maps, filtername='i',
                                            wfd_cloud_max=0.7,
                                            scp_cloud_max=0.7,
                                            gp_cloud_max=0.7,
                                            nes_cloud_max=0.7)

    width = (20.,)
    z_pad = (28.,)
    weight = (1.,)
    height = (80.,)

    # filters = ['u', 'g', 'r', 'i', 'z', 'y']
    filters = ['i']
    surveys = []

    sb_limit_map = fs.utils.generate_sb_map(target_maps, filters)

    filter_prop = {'u': 0.069,
                   'g': 0.097,
                   'r': 0.222,
                   'i': 0.222,
                   'z': 0.194,
                   'y': 0.194}

    for filtername in filters:
        bfs = list()
        # bfs.append(fs.M5_diff_basis_function(filtername=filtername, nside=nside))
        bfs.append(fs.HourAngle_bonus_basis_function(max_hourangle=6.))
        #     bfs.append(fs.Skybrightness_limit_basis_function(nside=nside,
        #                                                      filtername=filtername,
        #                                                      min=sb_limit_map[filtername]['min'],
        #                                                      max=sb_limit_map[filtername]['max']))
        bfs.append(fs.Normalized_Target_map_basis_function(filtername=filtername,
                                                           target_map=target_maps[filtername][0],
                                                           out_of_bounds_val=hp.UNSEEN, nside=nside, max_diff=1.))
        bfs.append(fs.MeridianStripeBasisFunction(nside=nside, width=width,
                                                  weight=weight,
                                                  height=height,
                                                  zenith_pad=z_pad))
        # bfs.append(fs.HADecAltAzPatchBasisFunction(nside=nside,
        #                                            patches=patches[::-1]))
        bfs.append(fs.Agreesive_Slewtime_basis_function(filtername=filtername, nside=nside, order=6., hard_max=120.))
        # bfs.append(fs.Strict_filter_basis_function(filtername=filtername,
        #                                            tag=[3],
        #                                            time_lag_min=90.,
        #                                            time_lag_max=150.,
        #                                            time_lag_boost=180.,
        #                                            boost_gain=1.0,
        #                                            unseen_before_lag=True,
        #                                            proportion=None,
        #                                            aways_available=filtername in 'rizy'))
        bfs.append(fs.Avoid_Fast_Revists(filtername=None, gap_min=120., nside=nside))  # Hide region for 2 hours!
        bfs.append(fs.Bulk_cloud_basis_function(max_cloud_map=cloud_map, nside=nside))
        bfs.append(fs.Moon_avoidance_basis_function(nside=nside, moon_distance=40.))
        # bfs.append(fs.CableWrap_unwrap_basis_function(nside=nside, activate_tol=70., unwrap_until=315,
        #                                               max_duration=90.))
        # bfs.append(fs.NorthSouth_scan_basis_function(length=70.))

        # weights = np.array([2., 0.1, 0.1, 1., 3., 1.5, 1.0, 1.0, 1.0])
        weights = np.array([.5, 1., 1., .5, 1.0, 1.0, 1.0])
        surveys.append(fs.Greedy_survey_fields(bfs, weights, block_size=1,
                                               filtername=filtername, dither=True,
                                               nside=nside,
                                               tag_fields=True,
                                               tag_map=target_maps[filtername][1],
                                               tag_names=target_maps[filtername][2],
                                               ignore_obs='DD'))

    scheduler = fs.Core_scheduler(surveys, nside=nside)  # Required
