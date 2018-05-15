import lsst.sims.ocs.configuration.instrument.dome
assert type(config)==lsst.sims.ocs.configuration.instrument.Dome, 'config is of type %s.%s instead of lsst.sims.ocs.configuration.instrument.Dome' % (type(config).__module__, type(config).__name__)
config.azimuth_freerange=4.
config.settle_time=0.
