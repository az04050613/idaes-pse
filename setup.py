#!/usr/bin/env python
"""
Institute for the Design of Advanced Energy Systems
"""
from pathlib import Path
import os
import sys
from setuptools import setup, find_packages


def warn(s):
    sys.stderr.write("*** WARNING *** {}\n".format(s))


def get_version():
    code_file = os.path.join("idaes", "ver.py")
    code = open(code_file).read()
    local_namespace = {}
    exec(code, {}, local_namespace)
    return local_namespace["__version__"]


NAME = "idaes-pse"
VERSION = get_version()
README = open("README.md").read()
README = README[README.find("#") :]  # ignore everything before title


def rglob(path, glob):
    """Return list of paths from `path` matching `glob`.
    """
    p = Path(path)
    return list(map(str, p.rglob(glob)))


alamopy_dir = Path("apps") / "ddm-learning" / "alamo_python" / "alamopy"
ripe_dir = Path("apps") / "ddm-learning" / "ripe_python" / "ripe"


def find_all_packages():
    test_patterns = ["*.tests", "*.tests.*", "tests.*", "tests"]

    def fp(path, prefix):
        return [prefix + "." + x for x in find_packages(path, exclude=test_patterns)]

    return (
        ["idaes"]
        + fp("idaes", "idaes")
        + fp(alamopy_dir, "alamopy")
        + fp(ripe_dir, "ripe")
    )


kwargs = dict(
    zip_safe=False,
    name=NAME,
    version=VERSION,
    packages=find_all_packages(),
    package_dir={
        "idaes": "idaes",
        "alamopy": alamopy_dir,
        "ripe": ripe_dir,
    },
    # Put abstract (non-versioned) deps here.
    # Concrete dependencies go in requirements[-dev].txt
    install_requires=[
        # idaes core / dmf
        "backports.shutil_get_terminal_size",
        "bokeh==0.12.9",
        "bunch",
        "click",
        "colorama",
        "humanize",
        "jupyter",
        "lxml",
        "matplotlib",
        "mock",
        "numpy",
        "networkx",
        "pandas",
        "pendulum==1.4.4",
        "pint",
        "psutil",
        "pyomo",
        "pytest",
        "pyutilib",
        "pyyaml",
        "sympy",
        "tinydb",
        "toml",
        # alamopy
        # ripe
        "rbfopt",
    ],
    entry_points={"console_scripts": ["dmf = idaes.dmf.cli:base_command"]},
    extras_require={
        # For developers. Only installed if [dev] is added to package name
        "dev": [
            "alabaster>=0.7.7",
            "coverage",
            "flake8",
            "flask>=1.0",
            "flask-bower",
            "flask-restful",
            "jsonschema",
            "jupyter_contrib_nbextensions",
            "mock",
            "pytest-cov",
            "python-coveralls",
            "snowballstemmer==1.2.1",
            "sphinx-rtd-theme>=0.1.9",
            "sphinxcontrib-napoleon>=0.5.0",
            "sphinx-argparse",
        ]
    },
    package_data={
        # If any package contains these files, include them:
        "": [
            "*.template",
            "*.json",
            "*.dll",
            "*.so",
            "*.svg",
            "*.png",
            "*.jpg",
            "*.csv",
            "*.ipynb",
        ]
    },
    include_package_data=True,
    data_files=[],
    maintainer="Keith Beattie",
    maintainer_email="ksbeattie@lbl.gov",
    url="https://idaes.org",
    license="BSD ",
    platforms=["any"],
    description="IDAES Process Systems Engineering Framework",
    long_description=README,
    long_description_content_type="text/markdown",
    keywords=[NAME, "energy systems", "chemical engineering", "process modeling"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: End Users/Desktop",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: BSD License",
        "Natural Language :: English",
        "Operating System :: MacOS",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: Unix",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: Implementation :: CPython",
        "Topic :: Scientific/Engineering :: Mathematics",
        "Topic :: Scientific/Engineering :: Chemistry",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)

setup(**kwargs)
