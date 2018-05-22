import lsst.sims.ocs.configuration.survey
assert type(config)==lsst.sims.ocs.configuration.survey.Survey, 'config is of type %s.%s instead of lsst.sims.ocs.configuration.survey.Survey' % (type(config).__module__, type(config).__name__)
config.general_proposals=['GalacticPlane', 'NorthEclipticSpur', 'SouthCelestialPole',
                          'WideFastDeep',
                          'WideFastDeepRollingAll',
                          'WideFastDeepRollingS',
                          'WideFastDeepRollingN']
