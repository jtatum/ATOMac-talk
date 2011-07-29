"""Abstraction layer for the workflow window"""
from automatorbase import AutomatorBase


# Constants
DEFAULT_WINDOW_TITLE = 'Untitled*'
SPLITGROUP_INDEX = 0
TOOLBAR_INDEX = 0
CHECKBOX_ACTIONS_INDEX = 1
CHECKBOX_VARIABLES_INDEX = 0
TEXTFIELD_SEARCH_INDEX = 0
TEXTFIELD_SPEAK_TEXT_VALUE = 'Speak Text'
TEXTFIELD_ASK_FOR_TEXT_VALUE = 'Ask for Text'
BUTTON_RUN_INDEX = 5
STATICTEXT_STATUS_INDEX = 0


class WorkflowWindow(AutomatorBase):
    """The main workflow window"""
    @classmethod
    def get(cls, title=DEFAULT_WINDOW_TITLE):
        app = super(WorkflowWindow, cls).get()
        window = app.windows(title)[0]
        return window

    def splitgroup(self):
        """Return the split group"""
        return self.item_index(self.findAll(AXRole='AXSplitGroup'),
                               SPLITGROUP_INDEX)

    def toolbar(self):
        """Return the toolbar at the top of the window"""
        return self.item_index(self.findAll(AXRole='AXToolbar'),
                               TOOLBAR_INDEX)

    def actions(self):
        """Actions 'checkbox'"""
        splitgroup = self.splitgroup()
        if not splitgroup:
            return None
        return self.item_index(splitgroup.findAll(AXRole='AXCheckBox'),
                               CHECKBOX_ACTIONS_INDEX)

    def variables(self):
        """Variables 'checkbox'"""
        splitgroup = self.splitgroup()
        if not splitgroup:
            return None
        return self.item_index(splitgroup.findAll(AXRole='AXCheckBox'),
                               CHECKBOX_VARIABLES_INDEX)

    def search(self):
        """Search textfield"""
        return self.item_index(self.splitgroup().textFields(),
                               TEXTFIELD_SEARCH_INDEX)

    def ask_for_text(self):
        """Ask for text item"""
        return self.findFirstR(AXRole='AXTextField',
                               AXValue=TEXTFIELD_ASK_FOR_TEXT_VALUE)
    def speak_text(self):
        """Speak text item"""
        return self.findFirstR(AXRole='AXTextField',
                               AXValue=TEXTFIELD_SPEAK_TEXT_VALUE)

    def run(self):
        """Run button"""
        toolbar = self.toolbar()
        if not toolbar:
            return None
        return self.item_index(toolbar.buttons(), BUTTON_RUN_INDEX)

    def status(self):
        """Status area text field"""
        splitgroup = self.splitgroup()
        if not splitgroup:
            return None
        return self.item_index(splitgroup.findAll(AXRole='AXStaticText'),
                               STATICTEXT_STATUS_INDEX)

    def close(self):
        """Close button"""
        return self.AXCloseButton