"""Base abstraction layer for Automator"""
import atomac
import time


# Constants
BUNDLE = 'com.apple.Automator'


class AutomatorBase(atomac.NativeUIElement):
    """Base class for Automator abstraction layer"""
    @classmethod
    def get(cls):
        return cls.getAppRefByBundleId(BUNDLE)

    @staticmethod
    def launch():
        atomac.launchAppByBundleId(BUNDLE)
        time.sleep(3)

    @staticmethod
    def terminate():
        atomac.terminateAppByBundleId(BUNDLE)
        time.sleep(2)

    def item_index(self, items, index):
        """From a list of items, return the item with the specified index
           or None
        """
        if len(items) > index:
            return items[index]
        return None

    def double_click(self, thing):
        """Offset double-click method

            Most items require a slight offset to the position or clicks
            don't work. This takes a thing and applies the offset before
            double-clicking on it
        """
        coords = [pos + 1 for pos in thing.AXPosition]
        self.doubleClickMouse(coords)