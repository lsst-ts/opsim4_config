import lsst.sims.ocs.configuration.scheduler_driver
assert type(config)==lsst.sims.ocs.configuration.scheduler_driver.SchedulerDriver, 'config is of type %s.%s instead of lsst.sims.ocs.configuration.scheduler_driver.SchedulerDriver' % (type(config).__module__, type(config).__name__)
config.coadd_values=False
