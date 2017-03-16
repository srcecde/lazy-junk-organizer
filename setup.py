"""
Python Lazy Junk Files Organizer
========================
Developed by: Chirag Rathod (Srce Cde)
Email: chiragr83@gmail.com
========================
"""
import cx_Freeze
import sys

base = None

if sys.platform == "win32":
    base = "Win32GUI"

executables = [cx_Freeze.Executable("orgjunk.py", base=base)]

cx_Freeze.setup(
    name = "Lazy Junk Organiser",
    options = {"build_exe": {"packages": ["os"]}},
    version = "0.01",
    description = "Organise and clean in few moments",
    executables = executables
)
