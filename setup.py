"""
Script for building the PyObjCExample Mac app

Usage: python setup.py py2app
"""
from distutils.core import setup
import py2app

nib_name = 'Hello'

# Set the NIB name
plist = dict(
             NSMainNibFile=nib_name,
             CFBundleShortVersionString="1.0",
             NSHumanReadableCopyright="Released under the BSD license",
             LSUIElement = True # Hide the app running in the dock
             )

setup(
    name="PyObjCExample",
    app=["main.py"],
    data_files=[nib_name + ".xib"],
    options=dict(py2app=dict(plist=plist))
)