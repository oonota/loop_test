from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext


ext_modules = [
    Extension( "loop", ["loop.pyx"] ),
]

setup(
    name = "Sample looo app",
    cmdclass = { "build_ext" : build_ext },
    ext_modules = ext_modules,
)


