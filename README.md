# deriva-client
[![PyPi Version](https://img.shields.io/pypi/v/deriva-client.svg)](https://pypi.python.org/pypi/deriva-client)
[![PyPi Wheel](https://img.shields.io/pypi/wheel/deriva-client.svg)](https://pypi.python.org/pypi/deriva-client)
[![Python Versions](https://img.shields.io/pypi/pyversions/deriva-client.svg)](https://pypi.python.org/pypi/deriva-client)
[![License](https://img.shields.io/pypi/l/deriva-client.svg)](https://www.gnu.org/licenses/gpl-3.0)

An application suite of Python-based client software for use with the 
DERIVA platform.

The `deriva-client` package bundles a set of software components 
(both CLI and GUI), that allow users to interact with DERIVA platform 
servers. These tools provide functions such as:
1. Authentication services for programmatic and non browser-based access.
2. Bulk import and export of catalog assets and (meta) data.
3. Catalog configuration, mutation and administration.


## Installer packages for Windows and MacOSX
Pre-packaged installers for Windows and MacOSX (which include a bundled 
Python interpeter and all other dependencies) for `deriva-client` can be 
found [here](https://github.com/informatics-isi-edu/deriva-client-bundle/releases). 
These installer packages are recommended for Windows and MacOSX users 
who are looking for a simple, turnkey installation.  

## Installing `deriva-client` from PyPi via `pip`
For users who already have Python installed and are comfortable installing 
Python software via the `pip` application, `deriva-client` can be easily 
installed along with all of it's dependencies directly from 
[PyPi](https://pypi.org/project/deriva-client) using `pip`.

#### Installation environment prerequisites:

* A Python 3.5.4 or greater installation (or virtual environment) is required. 

* For MacOSX and Linux systems which include Python as a core part of the
operating system, it is _highly recommended_ to install this software
into a _virtual environment_, so that it does not interfere or conflict
with the operating system's Python installation. The native Python3
[`venv`](https://docs.python.org/3/tutorial/venv.html) module, the 
[`virtualenv`](https://packaging.python.org/guides/installing-using-pip-and-virtualenv/) 
package from PyPi, or the [Anaconda Distribution](https://www.anaconda.com/distribution/)
environment are all suitable.  

* Instead of using a _virtual environment_, it is also possible to 
install the software into a [_user environment_](https://pip.pypa.io/en/stable/user_guide/#user-installs) 
using the `--user` argument to `pip install`.  

* Recent versions of `pip`, `setuptools`, and `wheel` are recommended. 
If these components are already installed, updating them to the latest 
versions available is _optional_.

#### Installation Sequence

1. Create and/or activate the target virtual environment, if any. 
This step is specific to the type of virtual environment being used.

2. Update `pip`, `setuptools`, and `wheel` (optional).

    1. For virtual environments execute the following:
        ```sh
        python -m pip install –-upgrade pip, setuptools, wheel
        ```
    2. For user environments execute the following:
        ```sh
        python -m pip install --user –-upgrade pip, setuptools, wheel
        ```
    3. For Linux system python installations it is recommended to use the 
    system's package manager such as `dnf`, `apt`, or `yum` to update 
    the following packages: `python3-pip`, `python3-setuptools` , and `python3-wheel`.

3. Install `deriva-client` directly from [PyPi](https://pypi.org/project/deriva-client) 
using the `pip install` command.
    1. For virtual environments execute the following:
        ```sh
        pip install deriva-client
        ```
    2. For user environments execute the following:
        ```sh
        pip install --user deriva-client
        ```
    3. For system-wide python installations (only do this if 
    you understand all of the ramifications):
        ```sh
        pip3 install deriva-client
        ```
##### IMPORTANT NOTE: 

###### Using `pip` to install software into __system-wide__ Python locations:

* Many newer Linux (as well as MacOSX) distributions contain both Python2
and Python3 installed alongside each other. In these environments, both
the python interpreter and `pip` are symbolically linked to the appropriate version,
with `python` and `pip` generally linked to the Python2 versions.
* Python3 versions are commonly accessed via `python3` and `pip3`.
If you are working _outside_ of a Python3 virtual environment and installing
either to the system-wide Python location (not recommended) or a user-based
location (e.g. with the `pip` `--user` argument), then you _must_
substitute `pip3` for `pip` when issuing `pip` installation commands.
* Also note that when installing into the system Python location via
`pip` on Linux/MacOSX, the commands must be run as root or the  `sudo`
command must be prefixed to the command line.
    
## Source code: 
The source code and additional documentation for the primary components of `deriva-client` can be found at the links below: 
* [`deriva-py`](https://github.com/informatics-isi-edu/deriva-py)
* [`deriva-qt`](https://github.com/informatics-isi-edu/deriva-qt)
* [`deriva-catalog-manage`](https://github.com/informatics-isi-edu/deriva-catalog-manage)
