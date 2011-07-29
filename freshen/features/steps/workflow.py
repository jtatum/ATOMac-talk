"""Steps relating to an Automator workflow"""
from freshen import *
import atomac
import time

from steps.application import *

from steps.abstraction.workflowwindow import WorkflowWindow
from steps.abstraction.selectscreen import SelectScreen
from steps.abstraction.dialogbox import DialogBox
from steps.abstraction.savesheet import SaveSheet


# Constants
STATUS_SUCCESS_VALUE = 'Workflow completed '

@Before
def window(sc):
    scc.window = WorkflowWindow.get()


@After
def close(sc):
    window = WorkflowWindow.get()
    if window:
        window.close().Press()
        time.sleep(1)
    savesheet = SaveSheet.get()
    if savesheet:
        button = savesheet.dont_save()
        if button:
            button.Press()


@Given('an empty workflow')
def new():
    """Click choose on the select sheet to start a new workflow"""
    ss = SelectScreen.get()
    ss.choose().Press()


@Given('an Ask for Text action')
def ask_for_text():
    scc.window.search().AXValue = 'ask'
    scc.window.search().Confirm()

    scc.window.double_click(scc.window.ask_for_text())


@Given('a Speak Text action')
def speak_text():
    scc.window.search().AXValue = 'speak'
    scc.window.search().Confirm()

    scc.window.double_click(scc.window.speak_text())


@When('I click Run')
def run():
    try:
        scc.window.run().Press()
    except atomac.ErrorCannotComplete:
        # Expected failure - the button stays "clicked" which causes the Press
        # method to time out
        pass
    time.sleep(1)


@When('I enter "(.*)" in the dialog')
def enter(text):
    dialog = DialogBox.get()
    dialog.textarea().AXValue = text
    time.sleep(3)


@When('I click OK in the dialog')
def ok():
    dialog = DialogBox.get()
    dialog.ok().Press()


@Then('the workflow runs successfully within (\d+) seconds')
def successful(timeout):
    for count in range(int(timeout)):
        if scc.window.status().AXValue == STATUS_SUCCESS_VALUE:
            return
        print repr(scc.window.status().AXValue)
        time.sleep(1)
    assert False