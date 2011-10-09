"""General steps common to all Automator features"""
from lettuce import *
import time

from abstraction.automatorbase import AutomatorBase


@before.each_scenario
def restart(scenario):
    """Restart Automator"""
    AutomatorBase.terminate()
    AutomatorBase.launch()

@after.each_scenario
def wait(scenario):
    time.sleep(1)