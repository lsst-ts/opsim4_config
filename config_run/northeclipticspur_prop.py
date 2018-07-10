import lsst.ts.schedulerConfig.science.north_ecliptic_spur
assert type(config)==lsst.ts.schedulerConfig.science.north_ecliptic_spur.NorthEclipticSpur, 'config is of type %s.%s instead of lsst.ts.schedulerConfig.science.north_ecliptic_spur.NorthEclipticSpur' % (type(config).__module__, type(config).__name__)
config.scheduling.airmass_bonus=0.0
config.scheduling.hour_angle_bonus=0.3
config.scheduling.hour_angle_max=3.0
