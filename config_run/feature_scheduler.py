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

    nside = fs.set_default_nside(nside=32)  # Required

    target_maps = {}
    target_maps['u'] = fs.generate_goal_map(nside=nside, NES_fraction=0.,
                                            WFD_fraction=0.31, SCP_fraction=0.15,
                                            GP_fraction=0.15, WFD_upper_edge_fraction=0.,
                                            generate_id_map=True)
    target_maps['g'] = fs.generate_goal_map(nside=nside, NES_fraction=0.2,
                                            WFD_fraction=0.44, SCP_fraction=0.15,
                                            GP_fraction=0.15, WFD_upper_edge_fraction=0.,
                                            generate_id_map=True)
    target_maps['r'] = fs.generate_goal_map(nside=nside, NES_fraction=0.46,
                                            WFD_fraction=1.0, SCP_fraction=0.15,
                                            GP_fraction=0.15, WFD_upper_edge_fraction=0.,
                                            generate_id_map=True)
    target_maps['i'] = fs.generate_goal_map(nside=nside, NES_fraction=0.46,
                                            WFD_fraction=1.0, SCP_fraction=0.15,
                                            GP_fraction=0.15, WFD_upper_edge_fraction=0.,
                                            generate_id_map=True)
    target_maps['z'] = fs.generate_goal_map(nside=nside, NES_fraction=0.4,
                                            WFD_fraction=0.9, SCP_fraction=0.15,
                                            GP_fraction=0.15, WFD_upper_edge_fraction=0.,
                                            generate_id_map=True)
    target_maps['y'] = fs.generate_goal_map(nside=nside, NES_fraction=0.,
                                            WFD_fraction=0.9, SCP_fraction=0.15,
                                            GP_fraction=0.15, WFD_upper_edge_fraction=0.,
                                            generate_id_map=True)

    target_2normfactor = {}
    for filtername in target_maps:
        target_2normfactor[filtername] = target_maps[filtername][0]

    norm_factor = fs.calc_norm_factor(target_2normfactor)

    cloud_map = fs.generate_cloud_map(target_maps, filtername='i',
                                      wfd_cloud_max=0.7,
                                      scp_cloud_max=0.7,
                                      gp_cloud_max=0.7,
                                      nes_cloud_max=0.7)

    width = (20.,)
    z_pad = (28.,)
    weight = (1.0,)
    height = (80.,)

    filters = ['u', 'g', 'r', 'i', 'z', 'y']
    # filters = ['r', 'i']
    surveys = []

    sb_limit_map = fs.utils.generate_sb_map(target_maps, filters)

    filter_prop = {'u': 0.0774,
                   'g': 0.117,
                   'r': 0.224,
                   'i': 0.224,
                   'z': 0.200,
                   'y': 0.154}

    target_map_weights = {'u': 0.1,
                          'g': 0.1,
                          'r': 0.075,
                          'i': 0.05,
                          'z': 0.05,
                          'y': 0.05}

    for filtername in filters:
        bfs = list()
        # bfs.append(fs.M5_diff_basis_function(filtername=filtername, nside=nside))
        bfs.append(fs.HourAngle_bonus_basis_function(max_hourangle=4.))
        bfs.append(fs.M5_diff_basis_function(filtername=filtername, nside=nside))
        #     bfs.append(fs.Skybrightness_limit_basis_function(nside=nside,
        #                                                      filtername=filtername,
        #                                                      min=sb_limit_map[filtername]['min'],
        #                                                      max=sb_limit_map[filtername]['max']))
        bfs.append(fs.Target_map_basis_function(filtername=filtername,
                                                target_map=target_maps[filtername][0],
                                                out_of_bounds_val=hp.UNSEEN, nside=nside,
                                                norm_factor=norm_factor))
        bfs.append(fs.MeridianStripeBasisFunction(nside=nside, width=width,
                                                  weight=weight,
                                                  height=height,
                                                  zenith_pad=z_pad))
        # bfs.append(fs.HADecAltAzPatchBasisFunction(nside=nside,
        #                                            patches=patches[::-1]))
        bfs.append(fs.Aggressive_Slewtime_basis_function(filtername=filtername, nside=nside, order=6., hard_max=120.))
        bfs.append(fs.Goal_Strict_filter_basis_function(filtername=filtername,
                                                        tag=None,
                                                        time_lag_min=90.,
                                                        time_lag_max=150.,
                                                        time_lag_boost=180.,
                                                        boost_gain=2.0,
                                                        unseen_before_lag=True,
                                                        proportion=1.,
                                                        aways_available=True))
        bfs.append(fs.Avoid_Fast_Revists(filtername=None, gap_min=30., nside=nside))  # Hide region for 0.5 hours
        bfs.append(fs.Bulk_cloud_basis_function(max_cloud_map=cloud_map, nside=nside))
        bfs.append(fs.Moon_avoidance_basis_function(nside=nside, moon_distance=40.))
        # bfs.append(fs.CableWrap_unwrap_basis_function(nside=nside, activate_tol=70., unwrap_until=315,
        #                                               max_duration=90.))
        # bfs.append(fs.NorthSouth_scan_basis_function(length=70.))

        # weights = np.array([2., 0.1, 0.1, 1., 3., 1.5, 1.0, 1.0, 1.0])
        weights = np.array([0.5, 1., target_map_weights[filtername], 1., .5, 1.0, 1.0, 1.0, 1.0])
        surveys.append(fs.Greedy_survey_fields(bfs, weights, block_size=1,
                                               filtername=filtername, dither=True,
                                               nside=nside,
                                               tag_fields=True,
                                               tag_map=target_maps[filtername][1],
                                               tag_names=target_maps[filtername][2],
                                               ignore_obs='DD'))

    # Set up pairs
    pairs_bfs = []

    pair_map = np.zeros(len(target_maps['z'][0]))
    pair_map.fill(hp.UNSEEN)
    wfd = np.where(target_maps['z'][1] == 3)
    nes = np.where(target_maps['z'][1] == 1)
    pair_map[wfd] = 1.
    pair_map[nes] = 1.

    pairs_bfs.append(fs.Target_map_basis_function(filtername='',
                                                  target_map=pair_map,
                                                  out_of_bounds_val=hp.UNSEEN, nside=nside))
    pairs_bfs.append(fs.MeridianStripeBasisFunction(nside=nside, zenith_pad=(45.,), width=(35.,)))
    pairs_bfs.append(fs.Moon_avoidance_basis_function(nside=nside, moon_distance=30.))

    surveys.append(fs.Pairs_survey_scripted(pairs_bfs, [1., 1., 1.], ignore_obs='DD', min_alt=20.,
                                            filt_to_pair='gri'))
    # surveys.append(fs.Pairs_different_filters_scripted(pairs_bfs, [1., 1., 1.], ignore_obs='DD', min_alt=20.,
    #                                                    filter_goals=filter_prop))
    # surveys.append(fs.Pairs_survey_scripted([], [], ignore_obs='DD'))

    # Set up the DD
    # ELAIS S1
    surveys.append(fs.Deep_drilling_survey(9.45, -44., sequence='rgizy',
                                           nvis=[20, 10, 20, 26, 20],
                                           survey_name='DD:ELAISS1', reward_value=100, moon_up=None,
                                           fraction_limit=0.148, ha_limits=([0., 0.5], [23.5, 24.]),
                                           nside=nside,
                                           avoid_same_day=True,
                                           filter_goals=filter_prop))
    surveys.append(fs.Deep_drilling_survey(9.45, -44., sequence='u',
                                           nvis=[7],
                                           survey_name='DD:u,ELAISS1', reward_value=100, moon_up=False,
                                           fraction_limit=0.0012, ha_limits=([0., 0.5], [23.5, 24.]),
                                           nside=nside))

    # XMM-LSS
    surveys.append(fs.Deep_drilling_survey(35.708333, -4 - 45 / 60., sequence='rgizy',
                                           nvis=[20, 10, 20, 26, 20],
                                           survey_name='DD:XMM-LSS', reward_value=100, moon_up=None,
                                           fraction_limit=0.148, ha_limits=([0., 0.5], [23.5, 24.]),
                                           nside=nside,
                                           avoid_same_day=True,
                                           filter_goals=filter_prop))
    surveys.append(fs.Deep_drilling_survey(35.708333, -4 - 45 / 60., sequence='u',
                                           nvis=[7],
                                           survey_name='DD:u,XMM-LSS', reward_value=100, moon_up=False,
                                           fraction_limit=0.0012, ha_limits=([0., 0.5], [23.5, 24.]),
                                           nside=nside))

    # Extended Chandra Deep Field South
    # XXX--Note, this one can pass near zenith. Should go back and add better planning on this.
    surveys.append(fs.Deep_drilling_survey(53.125, -28. - 6 / 60., sequence='rgizy',
                                           nvis=[20, 10, 20, 26, 20],
                                           survey_name='DD:ECDFS', reward_value=100, moon_up=None,
                                           fraction_limit=0.148, ha_limits=[[0.5, 1.0], [23., 22.5]],
                                           nside=nside,
                                           avoid_same_day=True,
                                           filter_goals=filter_prop))
    surveys.append(fs.Deep_drilling_survey(53.125, -28. - 6 / 60., sequence='u',
                                           nvis=[7],
                                           survey_name='DD:u,ECDFS', reward_value=100, moon_up=False,
                                           fraction_limit=0.0012, ha_limits=[[0.5, 1.0], [23., 22.5]],
                                           nside=nside))
    # COSMOS
    surveys.append(fs.Deep_drilling_survey(150.1, 2. + 10. / 60. + 55 / 3600., sequence='rgizy',
                                           nvis=[20, 10, 20, 26, 20],
                                           survey_name='DD:COSMOS', reward_value=100, moon_up=None,
                                           fraction_limit=0.148, ha_limits=([0., 0.5], [23.5, 24.]),
                                           nside=nside,
                                           avoid_same_day=True,
                                           filter_goals=filter_prop))
    surveys.append(fs.Deep_drilling_survey(150.1, 2. + 10. / 60. + 55 / 3600., sequence='u',
                                           nvis=[7], ha_limits=([0., .5], [23.5, 24.]),
                                           survey_name='DD:u,COSMOS', reward_value=100, moon_up=False,
                                           fraction_limit=0.0012,
                                           nside=nside))

    # Extra DD Field, just to get to 5. Still not closed on this one
    surveys.append(fs.Deep_drilling_survey(349.386443, -63.321004, sequence='rgizy',
                                           nvis=[20, 10, 20, 26, 20],
                                           survey_name='DD:290', reward_value=100, moon_up=None,
                                           fraction_limit=0.148, ha_limits=([0., 0.5], [23.5, 24.]),
                                           nside=nside,
                                           avoid_same_day=True,
                                           filter_goals=filter_prop))
    surveys.append(fs.Deep_drilling_survey(349.386443, -63.321004, sequence='u',
                                           nvis=[7],
                                           survey_name='DD:u,290', reward_value=100, moon_up=False,
                                           fraction_limit=0.0012, ha_limits=([0., 0.5], [23.5, 24.]),
                                           nside=nside,
                                           filter_goals=filter_prop))

    scheduler = fs.Core_scheduler(surveys, nside=nside)  # Required
