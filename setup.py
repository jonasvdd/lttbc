#!/usr/bin/env python
import os.path as osp
import sys

from setuptools import Extension, setup


def get_script_path():
    return osp.dirname(osp.realpath(sys.argv[0]))


def read(*parts):
    return open(osp.join(get_script_path(), *parts)).read()


class numpy_get_include:
    def __str__(self):
        import numpy
        return numpy.get_include()


lttbc_py = Extension("lttbcv2", sources=["lttbcv2.c"],
                     define_macros=[
                         ("NPY_NO_DEPRECATED_API", "NPY_1_7_API_VERSION")],
                     include_dirs=[numpy_get_include(),
                                   get_script_path()],
                     )

setup(
    name="lttbcv2",
    author="Jonas Van Der Donckt",
    ext_modules=[lttbc_py],
    author_email="jonvdrdo.vanderdonckt@ugent.be",
    maintainer="Jonas Van Der Donckt",
    url="https://github.com/dgoeries/lttbc/",
    description="Largest triangle three buckets module for Python written in C",
    long_description=read("README.txt"),
    long_description_content_type="text/markdown",
    license="MIT",
    install_requires=["numpy"],
    python_requires=">=3.5",

)
