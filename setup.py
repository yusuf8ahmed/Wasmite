from operator import attrgetter
from os import path
from setuptools import setup, find_packages

def read(fname):
    return open(path.join(path.dirname(__file__), fname)).read()

def from_here(relative_path):
    return path.join(path.dirname(__file__), relative_path)

with open('requirements.txt') as f: 
    requirements = f.readlines() 

# source env/bin/activate

setup(
    name="wasmite",
    version="0.1",
    author="Yusuf Ahmed",
    author_email="yusufahmed172@gmail.com",
    description="Wasm is the future but now it has a testing toolchain",
    long_description=read('Readme.md'),
    long_description_content_type="text/markdown",
    install_requires=['loguru', "wasmer", "wasmer-compiler-cranelift"],
    entry_points ={ 
        'console_scripts': [ 
            'wasmite = wasmite.__main__:main'
        ] 
    },
    python_requires='>=3',
    zip_safe = False
)