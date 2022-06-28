from setuptools import setup, find_packages

classifiers = ['Development Status :: 5 - Production/Stable',
'Intended Audience :: Education',
'Operating System :: Microsoft :: Windows :: Windows 10',
'License :: OSI Approved :: MIT License',
'Programming Language :: Python :: 3']





setup(name="PyTextAnalyzer",
version="1.1.0",
description="Python Module with functions helping with analyzing strings.",
author="Fallen Cat",
author_email="fallencat.user@gmail.com",
packages=find_packages(),
license='MIT',
classifiers=classifiers,
keywords='String Analyzer',
url='https://github.com/TheFallen-Cat/PyTextAnalyzer',
download_url='https://github.com/TheFallen-Cat/PyTextAnalyzer/archive/refs/tags/1.1.0.tar.gz')