import lsst.sims.ocs.configuration.instrument.camera
assert type(config)==lsst.sims.ocs.configuration.instrument.camera.Camera, 'config is of type %s.%s instead of lsst.sims.ocs.configuration.instrument.camera.Camera' % (type(config).__module__, type(config).__name__)
# Maximum average number of filter changes per year.
config.filter_max_changes_avg_num=100000

