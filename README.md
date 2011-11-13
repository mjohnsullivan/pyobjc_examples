PyObjC Examples
===============

Purpose
-------

This is a simple example app to demonstrate how to create a Mac-native app using PyObjC to bridge between Python and a Mac-native NIB interface.

I cobbled this together from numerous searching across the net. It works on Lion 10.7.2, Xcode 4.2 and the versions of Python (2.7) PyObjC that come as standard on the Mac.

I did this purely to teach myself how to use PyObjC; if anyone has comments or corrections, let me know.

Build Instructions
------------------

Simplest way is to run the build script in the project: ./compile_run.sh

To manually build:

* Delete the dist and build directories if they exist (not doing so breaks the buid process)
* Run: python setup.py py2app

The app should now be built in the dist directory. To run from the terminal:

* open dist/PyObjCExample.app

Tying the nib to Python
-------------------

To tie a nib file to Python code, firstly create a nib file in Xcode. Then build up the UI as you want.

Next, create a new workspace in Xcode and add the newly create nib and the Python controller file (in this case, main.py).

Next, link the Python controller class to the nib by adding an NSObject to the nib and then making the class of the object be your Python controller class. With this in place you can now add IBOutlet variables to your Python class and link them in Xcode to the UI elements in the nib.
