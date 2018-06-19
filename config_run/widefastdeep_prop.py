import lsst.sims.ocs.configuration.science.wide_fast_deep
assert type(config)==lsst.sims.ocs.configuration.science.wide_fast_deep.WideFastDeep, 'config is of type %s.%s instead of lsst.sims.ocs.configuration.science.wide_fast_deep.WideFastDeep' % (type(config).__module__, type(config).__name__)
config.scheduling.airmass_bonus=0.0
config.scheduling.hour_angle_bonus=0.3
config.scheduling.hour_angle_max=3.0
config.filters['u'].num_visits=19
config.filters['g'].num_visits=27
config.filters['r'].num_visits=60
config.filters['i'].num_visits=60
config.filters['z'].num_visits=53
config.filters['y'].num_visits=53
