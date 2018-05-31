import lsst.sims.ocs.configuration.science.south_celestial_pole
assert type(config)==lsst.sims.ocs.configuration.science.south_celestial_pole.SouthCelestialPole, 'config is of type %s.%s instead of lsst.sims.ocs.configuration.science.south_celestial_pole.SouthCelestialPole' % (type(config).__module__, type(config).__name__)
config.sky_region.selections[0].maximum_limit=-64.0
config.scheduling.airmass_bonus=0.0
config.scheduling.hour_angle_bonus=0.3
config.scheduling.hour_angle_max=3.0
