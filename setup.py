"""
This is a setup.py script generated by py2applet

Usage:
    python setup.py py2app
"""
import os

from setuptools import setup

APP = [f"mac/{'Test' if os.environ.get('TEST_MODE') else ''}Pomodouroboros.py"]
DATA_FILES = [
    "IBFiles/GoalListWindow.xib",
    "IBFiles/IntentionEditor.xib",
    "IBFiles/MainMenu.xib",
    "IBFiles/StandardMenus.xib",
]
OPTIONS = {
    "plist": {
        "LSUIElement": True,
        "NSRequiresAquaSystemAppearance": False,
        "CFBundleIdentifier": f"im.glyph.and.this.is.{'test' if os.environ.get('TEST_MODE') else ''}pomodouroboros",
    },
    "iconfile": f"{'test' if os.environ.get('TEST_MODE') else ''}icon.icns",
}

setup(
    name=f"{'Test' if os.environ.get('TEST_MODE') else ''}Pomodouroboros",
    app=APP,
    data_files=DATA_FILES,
    options={"py2app": OPTIONS},
)
