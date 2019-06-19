from setuptools import setup, find_packages

setup(
    name="fund-my-watcard",
    version="0.1",
    packages=find_packages(),
    scripts=['fund-my-watcard/watcard'],
    install_requires=['EasyProcess==0.2.7',
                      'PyVirtualDisplay==0.2.3',
                      'selenium==3.141.0',
                      'six==1.12.0',
                      'splinter==0.10.0',
                      'urllib3==1.25.3'
                      ],
    author="xingweitian",
    author_email="xingweitian@gmail.com",
    description="A tool to fund your WatCard in an easy way",
    license="GPL-3.0",
    keywords="WatCard",
    url="https://github.com/xingweitian/fund-my-watcard"
)
