"""Steps relating to an Automator workflow"""
from lettuce import *
import atomac
import time

from abstraction.workflowwindow import WorkflowWindow
from abstraction.selectscreen import SelectScreen
from abstraction.dialogbox import DialogBox
from abstraction.savesheet import SaveSheet


# Constants
STATUS_SUCCESS_VALUE = 'Workflow completed '

@before.each_scenario
def window(scenario):
    world.window = WorkflowWindow.get()


@after.each_scenario
def close(scenario):
    window = WorkflowWindow.get()
    if window:
        window.close().Press()
        time.sleep(1)
    savesheet = SaveSheet.get()
    if savesheet:
        button = savesheet.dont_save()
        if button:
            button.Press()


@step('an empty workflow')
def new(step):
    """Click choose on the select sheet to start a new workflow"""
    ss = SelectScreen.get()
    ss.choose().Press()


@step('an Ask for Text action')
def ask_for_text(step):
    world.window.search().AXValue = 'ask'
    world.window.search().Confirm()

    world.window.double_click(world.window.ask_for_text())


@step('a Speak Text action')
def speak_text(step):
    world.window.search().AXValue = 'speak'
    world.window.search().Confirm()

    world.window.double_click(world.window.speak_text())


@step('I click Run')
def run(step):
    try:
        world.window.run().Press()
    except atomac.ErrorCannotComplete:
        # Expected failure - the button stays "clicked" which causes the Press
        # method to time out
        pass
    time.sleep(1)


@step('I enter "(.*)" in the dialog')
def enter(step, text):
    dialog = DialogBox.get()
    dialog.textarea().AXValue = text
    time.sleep(3)


@step('I click OK in the dialog')
def ok(step):
    dialog = DialogBox.get()
    dialog.ok().Press()


@step('the workflow runs successfully within (\d+) seconds')
def successful(step, timeout):
    for count in range(int(timeout)):
        if world.window.status().AXValue == STATUS_SUCCESS_VALUE:
            return
        print repr(world.window.status().AXValue)
        time.sleep(1)
    assert False