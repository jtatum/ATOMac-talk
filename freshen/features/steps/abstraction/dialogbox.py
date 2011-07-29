"""Abstraction layer for dialog box popup"""
from automatorbase import AutomatorBase


# Constants
TEXTAREA_INDEX = 0
BUTTON_OK_INDEX = 0


class DialogBox(AutomatorBase):
    """Dialog box which appears, for instance when using 'Ask for Text'"""
    @classmethod
    def get(cls):
        app = super(DialogBox, cls).get()
        dialog = app.findAll(AXSubrole='AXDialog')[0]
        return dialog

    def textarea(self):
        """Big blank text field"""
        return self.item_index(self.findAllR(AXRole='AXTextArea'),
                               TEXTAREA_INDEX)

    def ok(self):
        """OK button"""
        return self.item_index(self.buttonsR(), BUTTON_OK_INDEX)