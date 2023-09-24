import os, pathlib
import pytest
cwd = os.getcwd()
path = cwd + '/tests/'
os.chdir(path)
#print(pathlib.Path.cwd())
pytest.main()