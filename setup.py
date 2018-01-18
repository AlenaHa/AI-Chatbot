#! /usr/bin/env python


import itertools
import os

from setuptools import find_packages, setup


ETC = os.path.join("etc", "cbot")
RES = os.path.join("res", "cbot")


def read(fpath):
    with open(os.path.join(os.path.dirname(__file__), fpath)) as stream:
        return stream.read()


def get_requirements(path="requirements.txt"):
    data = read(path)
    lines = []
    for line in data.splitlines():
        line = line.strip()
        if not line:
            continue
        if line.startswith("-r"):
            new_path = line[2:].strip()
            lines.extend(get_requirements(path=new_path))
            continue
        lines.append(line)
    return lines


def discover_data(root):
    for dirpath, dirnames, filenames in os.walk(root):
        paths = []
        for name in filenames:
            path = os.path.join(dirpath, name)
            paths.append(path)
        yield dirpath, paths


setup(
    name="cbot",
    version="0.1.0",
    description="AI chatbot.",
    long_description=read("README.md"),
    url="https://github.com/AlenaHa/AI-Chatbot",
    license="MIT",
    author="A6",
    author_email="cmin764@gmail.com",
    packages=find_packages(),
    scripts=[os.path.join("bin", "cbot")],
    include_package_data=True,
    zip_safe=False,
    install_requires=get_requirements(),
    test_suite="tests",
    data_files=itertools.chain(*map(discover_data, (ETC, RES))),
)
