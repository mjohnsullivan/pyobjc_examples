#!/bin/bash

rm -rf build dist
python setup.py py2app
open dist/PyObjCExample.app
