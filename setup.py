#
# Copyright 2019 University of Southern California
# Distributed under the GNU GPL 3.0 license. See LICENSE for more info.
#

""" Installation script for DERIVA Client Tools
"""
import io
from setuptools import setup
from version import __version__


def get_readme_contents():
    with io.open('README.md') as readme_file:
        return readme_file.read()


url = 'https://github.com/informatics-isi-edu/deriva-client'
author = 'USC Information Sciences Institute, Informatics Systems Research Division'
author_email = 'isrd-support@isi.edu'


setup(
    name='deriva-client',
    description='A Python-based application suite of client software for use with the DERIVA platform.',
    long_description=get_readme_contents(),
    long_description_content_type='text/markdown',
    url=url,
    author=author,
    author_email=author_email,
    maintainer=author,
    maintainer_email=author_email,
    version=__version__,
    python_requires='>=3.8',
    install_requires=[
        'bdbag[boto]==1.7.2',
        'globus_sdk>=3,<4',
        'minid==2.0.1',
        'fair-research-login==0.3.1',
        'fair-identifiers-client==0.5.1',
        'deriva==1.7.0',
        'deriva-qt==1.7.0',
        'deriva-chisel==0.3.0',
        'deriva-catalog-manage==0.9.2',
        'deriva-workbench==0.1.2',
        'bdbag_gui==1.2.1',
        "PyQtWebEngine==5.15.5"
    ],
    license='GNU GPL 3.0',
    classifiers=[
        'Intended Audience :: Science/Research',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        "Operating System :: POSIX",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12'
    ]
)


