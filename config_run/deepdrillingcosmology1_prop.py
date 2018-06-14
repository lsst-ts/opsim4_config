import lsst.sims.ocs.configuration.science.deep_drilling_cosmology1
assert type(config)==lsst.sims.ocs.configuration.science.deep_drilling_cosmology1.DeepDrillingCosmology1, 'config is of type %s.%s instead of lsst.sims.ocs.configuration.science.deep_drilling_cosmology1.DeepDrillingCosmology1' % (type(config).__module__, type(config).__name__)
config.sky_user_regions=[290, 744, 820, 858, 1200, 1427, 2412, 2689, 2786]
config.scheduling.airmass_bonus=0.0
config.scheduling.hour_angle_bonus=0.3
