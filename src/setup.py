import sys, os
from cx_Freeze import setup,Executable

includefiles = ["README.md", "../ressources", "../csv_files"]
path = sys.path.append(os.path.join("GUI"))
includes = []
excludes = []
packages = []

setup(
    name = "MLE",
    version = "0.1",
    description = "A little a simple Enterprise Ressource Planner",
    author = "MLE Team",
    author_email = "",
    options = {"build_exe": {"path": path,'includes':includes,'excludes':excludes,'packages':packages,'include_files':includefiles}}, 
    executables = [Executable('MLE.py')]
)
