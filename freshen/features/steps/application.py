"""General steps common to all Automator features"""
from freshen import *
import time

from abstraction.automatorbase import AutomatorBase


@Before
def restart(sc):
    """Restart Automator"""
    AutomatorBase.terminate()
    AutomatorBase.launch()

@After
def wait(sc):
    time.sleep(1)