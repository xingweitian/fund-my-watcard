from importlib.machinery import SourceFileLoader

from setuptools import find_packages, setup

VERSION = SourceFileLoader("version", "src/fund_my_watcard/version.py").load_module().VERSION

with open("requirements.txt") as f:
    requirements = [_.strip() for _ in f.readlines() if _]

with open("README.md", encoding="utf-8") as f:
    long_description = f.read()

with open("Contributors.txt", encoding="utf-8") as f:
    contributors = [_.strip() for _ in f.readlines() if _]

setup(
    name="fund-my-watcard",
    version=VERSION,
    packages=find_packages("src"),
    package_dir={"": "src"},
    python_requires=">=3.5",
    entry_points={"console_scripts": ["watcard = fund_my_watcard.main:main"]},
    install_requires=requirements,
    author=", ".join(contributors),
    author_email="xingweitian@gmail.com",
    description="A tool to fund WatCard in an easy way",
    long_description_content_type="text/markdown",
    long_description=long_description,
    license="GPL-3.0",
    keywords="WatCard",
    url="https://github.com/xingweitian/fund-my-watcard",
    classifiers=[
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
)
