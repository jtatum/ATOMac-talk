"""Abstraction layer for the type selection sheet"""
from automatorbase import AutomatorBase


# Constants
WINDOW_TITLE = 'Untitled*'
BUTTON_CLOSE_TITLE = 'Close'
BUTTON_CHOOSE_INDEX = 2


class SelectScreen(AutomatorBase):
    """The select screen pops up when creating a new document in Automator"""
    @classmethod
    def get(cls):
        app = super(SelectScreen, cls).get()
        window = app.windows(WINDOW_TITLE)[0]
        sheet = window.sheets()[0]
        return sheet

    def close(self):
        """Close button"""
        return self.buttons(BUTTON_CLOSE_TITLE)[0]

    def choose(self):
        """Choose button"""
        return self.item_index(self.buttons(), BUTTON_CHOOSE_INDEX)
