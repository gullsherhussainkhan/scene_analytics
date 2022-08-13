#!/usr/bin/env python
from setuptools import setup, find_packages

import sys
sys.path.append(os.path.abspath('scene_analytics'))

setup_info = dict(
    name='sceneunderstanding',
    version='0.0.1',
    author='AWS ProServe',
    author_email='gullsher@amazon.de',
    url='',
    download_url='',
    project_urls={
        'Documentation': '',
        'Source': '',
        'Tracker': '',
    },
    description='Library for scene analytics using Computer Vision',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    license='BSD',
    classifiers=[
        'Development Status :: 1 - Planning',
        'Environment :: MacOS X',
        'Environment :: Win32 (MS Windows)',
        'Intended Audience :: Developers :: Quality Assurance/Control :: Data Scientist :: Machine Learning Engineer',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3.8',
        'Topic :: Automotive/Autonomous Vehicles',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],

    # Package info
    packages=['corelib'] + ['corelib.' + pkg for pkg in find_packages('corelib')],

    # Add _ prefix to the names of temporary build dirs
    options={'build': {'build_base': '_build'}, },
    zip_safe=True,
)

setup(**setup_info)