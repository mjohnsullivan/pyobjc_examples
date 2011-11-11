"""
Simple app to demonstrate integrating a NIB UI with Python using PyObjC.

To build the demo program, run the following in the terminal:

    $ python setup.py py2app

This creates a directory "dist" containing PyObjCExample.app.
    
Using the '-A' option causes the files to be symlinked to the .app bundle instead
of copied. This means you don't have to rebuild the app if you edit the sources or nibs.

However the '-A' option currently doesn't work on my system.
"""
from PyObjCTools import AppHelper
from Foundation import *


class PyController(NSObject):
    """
    Simple controller that hooks up the the NIV
    """

    # Hook up the Interface Builder outlets for the UI
    # elements (only the text field is needed for this example)

    #window = objc.IBOutlet()
    #button = objc.IBOutlet()
    #label = objc.IBOutlet()
    text_field = objc.IBOutlet()

    def awakeFromNib(self):
        pass

    @objc.IBAction
    def buttonClick_(self, sender):
        """
        Handle a button click message
        """
        from datetime import datetime
        self.text_field.setStringValue_(datetime.now().strftime("%H:%M"))


if __name__ == "__main__":
    AppHelper.runEventLoop()
