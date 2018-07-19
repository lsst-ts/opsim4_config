"""
This is an example configuration for some of the basic parameters for simulations.

07/2018 - Version 0
"""
import lsst.sims.ocs.configuration.survey
assert type(config)==lsst.sims.ocs.configuration.survey.Survey, 'config is of type %s.%s instead of lsst.sims.ocs.configuration.survey.Survey' % (type(config).__module__, type(config).__name__)
# The delay (units=seconds) to skip the simulation time forward when not receiving a target.
config.idle_delay=60.0

# The start date (format=YYYY-MM-DD) of the survey.
config.start_date='2022-10-01'

# The fractional duration (units=years) of the survey.
config.duration=10.0
