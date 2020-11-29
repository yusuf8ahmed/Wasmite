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

# rm -rf build dist wasmite.egg-info
# python setup.py sdist bdist_wheel 
# python -m twine upload --skip-existing dist/*
# python -m twine upload dist/*

setup(
    name="wasmite",
    version="0.1.5",
    author="Yusuf Ahmed",
    author_email="yusufahmed172@gmail.com",
    packages=find_packages(exclude=['env', ".vscode"]),
    description="Wasmite: Webassembly is the future but now it has a testing toolchain",
    long_description=read('Readme.md'),
    long_description_content_type="text/markdown",
    install_requires=['loguru', "wasmer>=1.0.0-alpha3", "wasmer-compiler-cranelift>=1.0.0-alpha3"],
    url="https://github.com/yusuf8ahmed/Wasmite",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Development Status :: 2 - Pre-Alpha",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Topic :: Internet",
        "Topic :: Internet :: WWW/HTTP :: Browsers",
        "Topic :: Internet :: WWW/HTTP :: HTTP Servers",
        "Topic :: Internet :: WWW/HTTP :: WSGI",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Middleware",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Server",
        "Topic :: Software Development :: Assemblers",
        "Topic :: Software Development :: Testing",
        "Topic :: Software Development :: Quality Assurance",
        "Topic :: System :: Monitoring",
    ],
    platforms = 'any',
    keywords = ["wasmer", "wasmite", "wasp", "wasm", "debug", "debugging", "unit",
                "unit testing", "unit tests", "unit testing wasm", "unit tests wasm",
                "debug wasm", "debugging wasm"],
    python_requires='!=3.9, !=2.*',
    zip_safe = False
)