import lsst.sims.ocs.configuration.instrument.optics_loop_corr
assert type(config)==lsst.sims.ocs.configuration.instrument.optics_loop_corr.OpticsLoopCorr, 'config is of type %s.%s instead of lsst.sims.ocs.configuration.instrument.optics_loop_corr.OpticsLoopCorr' % (type(config).__module__, type(config).__name__)
config.tel_optics_cl_delay=[0.0, 36.0]
