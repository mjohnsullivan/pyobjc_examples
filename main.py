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
from AppKit import NSStatusBar, NSStatusItem, NSVariableStatusItemLength


class PyController(NSObject):
    """
    Simple Python controller that hooks up to a MacOSX nib
    """

    # Hook up the Interface Builder outlets for the UI elements
    # (only the text field and status menu are needed for this example)

    #window = objc.IBOutlet()
    #button = objc.IBOutlet()
    #label = objc.IBOutlet()
    text_field = objc.IBOutlet()
    status_menu = objc.IBOutlet()
    
    # The status menu
    status = None


    def _setup_status_bar(self):
        """
        Set up the status bar in the Mac menu
        """
        self.status = NSStatusBar.systemStatusBar().statusItemWithLength_(NSVariableStatusItemLength)
        self.status.setMenu_(self.status_menu)
        self.status.setTitle_("Core")
        self.status.setHighlightMode_(objc.YES)


    def awakeFromNib(self):
        """
        Set up the UI once the NIB is initialised
        """
        self._setup_status_bar()


    @objc.IBAction
    def buttonClick_(self, sender):
        """
        Handle a button click message
        """
        from datetime import datetime
        self.text_field.setStringValue_(datetime.now().strftime("%H:%M"))


if __name__ == "__main__":
    AppHelper.runEventLoop()