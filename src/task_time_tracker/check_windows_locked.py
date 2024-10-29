# coding: utf-8
"""
check_windows_locked.py
Copyright: (c) Steve Barnes 2024
Author: Steve Barnes <gadgetsteve@hotmail.com>

Check if a windows system is screen locked.
"""

import sys
import time
from ctypes import LoadLibrary

import psutil

def lock_screen():
    """Lock the screen."""
    lib = LoadLibrary("C:/Windows/System32/user32.dll")
    lib.LockWorkStation()

def screen_locked():
    """Check if screen locked."""
    loc_proc_names = ["LogonUI.exe", ]  # Use a list in case of future changes
    return any(proc.name() in loc_proc_names for proc in psutil.process_iter())


if __name__ == "__main__":
    print(
        "Test of",
        sys.argv[0],
        "This will lock your screen, wait a couple of seconds",
        "before unlocking",
    )
    for count in range(10):
        print(time.asctime(), "LOCKED" if screen_locked() else "OPEN")
        time.sleep(1)
        if count == 2:
            lock_screen()
        
    print("Done!")
