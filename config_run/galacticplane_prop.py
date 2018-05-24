import lsst.sims.ocs.configuration.science.galactic_plane
assert type(config)==lsst.sims.ocs.configuration.science.galactic_plane.GalacticPlane, 'config is of type %s.%s instead of lsst.sims.ocs.configuration.science.galactic_plane.GalacticPlane' % (type(config).__module__, type(config).__name__)
config.scheduling.airmass_bonus=0.0
config.scheduling.hour_angle_bonus=0.3
config.scheduling.hour_angle_max=3.0
config.filters['u'].exposures=[40]
config.filters['g'].exposures=[20]
config.filters['r'].exposures=[20]
config.filters['i'].exposures=[20]
config.filters['z'].exposures=[20]
config.filters['y'].exposures=[20]
config.filters['u'].num_visits=45
config.filters['g'].num_visits=45
config.filters['r'].num_visits=45
config.filters['i'].num_visits=45
config.filters['z'].num_visits=45
config.filters['y'].num_visits=45
