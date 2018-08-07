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

    target_maps['i'] = fs.generate_goal_map(NES_fraction=0.1,
                                            WFD_fraction=.8, SCP_fraction=0.05,
                                            GP_fraction=.05,
                                            WFD_upper_edge_fraction=0.0,
                                            nside=nside,
                                            generate_id_map=True)

    target_maps['r'] = fs.generate_goal_map(NES_fraction=0.1,
                                            WFD_fraction=.8, SCP_fraction=0.05,
                                            GP_fraction=.05,
                                            WFD_upper_edge_fraction=0.0,
                                            nside=nside,
                                            generate_id_map=True)

    cloud_map = fs.utils.generate_cloud_map(target_maps, filtername='i',
                                            wfd_cloud_max=0.7,
                                            scp_cloud_max=0.7,
                                            gp_cloud_max=0.7,
                                            nes_cloud_max=0.7)

    width = (16, 20.,)
    z_pad = (7, 28.,)
    weight = (1.0, 0.9,)
    height = (7.5, 80.,)

    # patches = []
    #
    # patches.append({'ha_min': 2.5, 'ha_max': 21.5,
    #                 'alt_max': 82., 'alt_min': 74.,
    #                 'dec_min': -30.2444 - 8., 'dec_max': -30.2444 + 8.,
    #                 'az_min': 0., 'az_max': 360.,
    #                 'weight': 1.0})
    #
    # patches.append({'ha_min': 4., 'ha_max': 23.9,
    #                 'alt_max': 82., 'alt_min': 65.,
    #                 'dec_min': -89., 'dec_max': 10.,
    #                 'az_min': 0., 'az_max': 360.,
    #                 'weight': .9})
    #
    # patches.append({'ha_min': 0., 'ha_max': 20.,
    #                 'alt_max': 82., 'alt_min': 65.,
    #                 'dec_min': -89., 'dec_max': 10.,
    #                 'az_min': 0., 'az_max': 360.,
    #                 'weight': .9})
    #
    # az = 30
    # patches.append({'alt_max': 82., 'alt_min': 20.,
    #                 'dec_min': -90, 'dec_max': 90,
    #                 'az_min': 0., 'az_max': az,
    #                 'weight': .9})
    # patches.append({'alt_max': 82., 'alt_min': 20.,
    #                 'dec_min': -90, 'dec_max': 90,
    #                 'az_min': 360. - az, 'az_max': 360.,
    #                 'weight': .9})
    #
    # patches.append({'alt_max': 82., 'alt_min': 20.,
    #                 'dec_min': -90, 'dec_max': 90,
    #                 'az_min': 180. - az, 'az_max': 180. + az,
    #                 'weight': .9})

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

    filter_prop = {'r': 0.5,
                   'i': 0.5}

    for filtername in filters:
        bfs = list()
        # bfs.append(fs.M5_diff_basis_function(filtername=filtername, nside=nside))
        bfs.append(fs.HourAngle_bonus_basis_function(max_hourangle=4.))
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
        bfs.append(fs.Goal_Strict_filter_basis_function(filtername=filtername,
                                                        tag=None,
                                                        time_lag_min=90.,
                                                        time_lag_max=150.,
                                                        time_lag_boost=180.,
                                                        boost_gain=2.0,
                                                        unseen_before_lag=True,
                                                        proportion=filter_prop[filtername],
                                                        aways_available=True))
        bfs.append(fs.Avoid_Fast_Revists(filtername=None, gap_min=30., nside=nside))  # Hide region for 0.5 hours
        bfs.append(fs.Bulk_cloud_basis_function(max_cloud_map=cloud_map, nside=nside))
        bfs.append(fs.Moon_avoidance_basis_function(nside=nside, moon_distance=40.))
        # bfs.append(fs.CableWrap_unwrap_basis_function(nside=nside, activate_tol=70., unwrap_until=315,
        #                                               max_duration=90.))
        # bfs.append(fs.NorthSouth_scan_basis_function(length=70.))

        # weights = np.array([2., 0.1, 0.1, 1., 3., 1.5, 1.0, 1.0, 1.0])
        weights = np.array([.5, 1., 1., .5, 1.0, 1.0, 1.0, 1.0])
        surveys.append(fs.Greedy_survey_fields(bfs, weights, block_size=1,
                                               filtername=filtername, dither=True,
                                               nside=nside,
                                               tag_fields=True,
                                               tag_map=target_maps[filtername][1],
                                               tag_names=target_maps[filtername][2],
                                               ignore_obs='DD'))

    scheduler = fs.Core_scheduler(surveys, nside=nside)  # Required
