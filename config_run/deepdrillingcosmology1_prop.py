import lsst.ts.schedulerConfig.science.deep_drilling_cosmology1
assert type(config)==lsst.ts.schedulerConfig.science.deep_drilling_cosmology1.DeepDrillingCosmology1, 'config is of type %s.%s instead of lsst.ts.schedulerConfig.science.deep_drilling_cosmology1.DeepDrillingCosmology1' % (type(config).__module__, type(config).__name__)
config.scheduling.airmass_bonus=0.0
config.scheduling.hour_angle_bonus=0.3
