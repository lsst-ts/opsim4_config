import lsst.sims.ocs.configuration.science.north_ecliptic_spur
assert type(config)==lsst.sims.ocs.configuration.science.north_ecliptic_spur.NorthEclipticSpur, 'config is of type %s.%s instead of lsst.sims.ocs.configuration.science.north_ecliptic_spur.NorthEclipticSpur' % (type(config).__module__, type(config).__name__)
config.scheduling.airmass_bonus=0.0
config.scheduling.hour_angle_bonus=0.3
config.scheduling.hour_angle_max=3.0
config.filters['g'].exposures=[20]
config.filters['r'].exposures=[20]
config.filters['i'].exposures=[20]
config.filters['z'].exposures=[20]
config.filters['g'].num_visits=60
config.filters['r'].num_visits=138
config.filters['i'].num_visits=138
config.filters['z'].num_visits=120
