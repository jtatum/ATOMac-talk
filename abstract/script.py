"""Test script for automator workflow

    Create a new workflow, add a couple of actions to it, and run the workflow
"""
import atomac
import time

from workflowwindow import WorkflowWindow
from selectscreen import SelectScreen
from dialogbox import DialogBox


SelectScreen.terminate()
SelectScreen.launch()

ss = SelectScreen.get()
ss.choose().Press()

window = WorkflowWindow.get()
window.actions().Press()

window.search().AXValue = 'ask'
window.search().Confirm()

window.double_click(window.ask_for_text())

window.search().AXValue = 'speak'
window.search().Confirm()

window.double_click(window.speak_text())

try:
    window.run().Press()
except atomac.ErrorCannotComplete:
    # Expected failure - the button stays "clicked" which causes the Press
    # method to time out
    pass

dialog = DialogBox.get()
dialog.textarea().AXValue = "I'm sorry Dave, I'm afraid I can't do that."
time.sleep(3)
dialog.ok().Press()
