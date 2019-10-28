import sys
from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize

name = sys.argv[1]
sys.argv.pop(1)

setup(
    ext_modules = cythonize(name + ".py", language_level = "3")
)
