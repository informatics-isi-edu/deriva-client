# deriva-client
[![PyPi Version](https://img.shields.io/pypi/v/deriva-client.svg)](https://pypi.python.org/pypi/deriva-client)
[![PyPi Wheel](https://img.shields.io/pypi/wheel/deriva-client.svg)](https://pypi.python.org/pypi/deriva-client)
[![Python Versions](https://img.shields.io/pypi/pyversions/deriva-client.svg)](https://pypi.python.org/pypi/deriva-client)
[![License](https://img.shields.io/pypi/l/deriva-client.svg)](https://www.gnu.org/licenses/gpl-3.0)

The `deriva-client` package bundles an application suite of Python-based 
client software for use with the DERIVA platform. These tools provide functions such as:
1. Authentication services for programmatic and non browser-based access.
2. Bulk import and export of catalog assets and (meta) data.
3. Catalog configuration, mutation and administration.
4. Tools for working with [`bdbags`](https://github.com/fair-research/bdbag), 
a file container format used by DERIVA.


## Installer packages for Windows and MacOSX
Pre-packaged installers of `deriva-client` for Windows and MacOSX can be 
found [here](https://github.com/informatics-isi-edu/deriva-client-bundle/releases). 
These installer packages include a bundled Python interpeter and all 
other software dependencies and are recommended for Windows and MacOSX 
users who are looking for a more traditional "turnkey" installation.  

## Installing `deriva-client` from PyPi via `pip`
For users who already have Python installed and are comfortable installing 
Python software via the `pip` application, `deriva-client` can be easily 
installed along with all of it's dependencies directly from 
[PyPi](https://pypi.org/project/deriva-client) using basic `pip` commands.

### Installation environment prerequisites:

* A Python 3.5.4 or greater system installation is required. Verify that 
the appropriate Python interpreter can be invoked from a command shell 
using the `python3` command. This can be tested simply with the following 
command: 

```sh
python3 --version
```

### Quickstart installation

The following commands can be used to perform a `venv`-based _virtual 
environment_ installation to the current working directory. 

###### Mac/Linux
The following commands assume a `BASH` (or compatible) command shell is 
used. For a different command interpreter (e.g. `CSH`), invoke the `source` 
command on the appropriate activation script in the virtual environment's `bin` directory. 
```sh
python3 -m venv ./deriva-client-venv
source ./deriva-client-venv/bin/activate
python3 -m pip install --upgrade pip setuptools wheel
pip install deriva-client
```

###### Windows
The following commands assume a Windows `Command Prompt` command shell is used. For a 
`Powershell` shell, the `activate.ps1` activation script should be invoked instead.
```sh
python3 -m venv .\deriva-client-venv
.\deriva-client-venv\Scripts\activate
python3 -m pip install --upgrade pip setuptools wheel
pip install deriva-client
```

###### IMPORTANT NOTE: Python _virtual environments_ versus _user environments_
While a [_virtual environment_](https://docs.python.org/3/tutorial/venv.html) 
installation is generally the safest way to install and isolate multiple 
software packages, it also must be _activated_ before use and 
_deactivated_ after use. If this requirement is too cumbersome, the 
recommended alternative is to install the software into a 
[_user environment_](https://pip.pypa.io/en/stable/user_guide/#user-installs) 
instead. See the complete installation procedure below for more information.


### Installation procedure

* For MacOSX and Linux systems which include Python as a core part of the
operating system, it is _highly recommended_ to install this software
into a _virtual environment_ or a _user environment_, so that it does not interfere or conflict
with the operating system's Python installation. The native Python3
[`venv`](https://docs.python.org/3/tutorial/venv.html) module, the 
[`virtualenv`](https://packaging.python.org/guides/installing-using-pip-and-virtualenv/) 
package from PyPi, or the [Anaconda Distribution](https://www.anaconda.com/distribution/)
environment are all suitable for use as virtual environments.  

* Instead of using a _virtual environment_, it is also possible to 
install the software into a [_user environment_](https://pip.pypa.io/en/stable/user_guide/#user-installs) 
using the `--user` argument when invoking `pip install`.  

* Recent versions of `pip`, `setuptools`, and `wheel` are recommended. 
If these components are already installed, updating them to the latest 
versions available is _optional_.

#### Installation Sequence

1. Create and/or activate the target virtual environment, if any. 
This step is specific to the type of virtual environment being used.

2. Update `pip`, `setuptools`, and `wheel` (optional).

    1. For _virtual environments_ execute the following (ensure the 
    environment is _active_):
        ```sh
        python -m pip install –-upgrade pip setuptools wheel
        ```
    2. For _user environments_ execute the following:
        ```sh
        python3 -m pip install --user –-upgrade pip setuptools wheel
        ```
    3. For Linux system python installations it is recommended to use the 
    system's package manager such as `dnf`, `apt`, or `yum` to update 
    the following packages: `python3-pip`, `python3-setuptools` , and `python3-wheel`.

3. Install `deriva-client` directly from [PyPi](https://pypi.org/project/deriva-client) 
using the `pip install` command.
    1. For _virtual environments_ execute the following (ensure the 
    environment is _active_):
        ```sh
        pip install deriva-client
        ```
    2. For _user environments_ execute the following:
        ```sh
        pip3 install --user deriva-client
        ```
    3. For system-wide python installations (only do this if you 
        understand the complexities involved):
        ```sh
        pip3 install deriva-client
        ```

###### IMPORTANT NOTES: Using `pip` to install software into __system-wide__ Python locations

* Many newer Linux (as well as MacOSX) distributions contain both Python2
and Python3 installed alongside each other. In these environments, both
the python interpreter and `pip` are symbolically linked to the system 
default version, which in general results in `python` and `pip` being 
linked to the Python2 versions.
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
