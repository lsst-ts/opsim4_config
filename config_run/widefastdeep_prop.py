import lsst.sims.ocs.configuration.science.wide_fast_deep
assert type(config)==lsst.sims.ocs.configuration.science.wide_fast_deep.WideFastDeep, 'config is of type %s.%s instead of lsst.sims.ocs.configuration.science.wide_fast_deep.WideFastDeep' % (type(config).__module__, type(config).__name__)
config.scheduling.airmass_bonus=0.0
config.scheduling.hour_angle_bonus=0.3
config.scheduling.hour_angle_max=3.0
config.filters['u'].num_grouped_visits=1
config.filters['u'].max_grouped_visits=1
config.filters['g'].num_grouped_visits=1
config.filters['g'].max_grouped_visits=1
config.filters['r'].num_grouped_visits=1
config.filters['r'].max_grouped_visits=1
config.filters['i'].num_grouped_visits=1
config.filters['i'].max_grouped_visits=1
config.filters['z'].num_grouped_visits=1
config.filters['z'].max_grouped_visits=1
config.filters['y'].max_grouped_visits=1
