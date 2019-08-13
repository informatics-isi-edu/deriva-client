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

## Installed Applications

###### Command-Line Interface (CLI) applications
| Executable Name | Description |
| --- | --- |
|`bdbag`|The [`bdbag`](https://github.com/fair-research/bdbag/blob/master/doc/cli.md#bdbag-command-line-interface-cli) application provides a variety of functions for working with [`BagIt`](https://datatracker.ietf.org/doc/draft-kunze-bagit/) file archives, a file packaging format used by DERIVA for data export. This format is created by the DERIVA web applications when exporting data sets using the `BDBAG` option.|
|`bdbag-utils`|The [`bdbag-utils`](https://github.com/fair-research/bdbag/blob/master/doc/utils.md#bdbag-bdbag-utils--reference) application is used to make some of the more repetitive and programmable tasks associated with creating and maintaining bags easier.|
|`deriva-acl-config`|The [`deriva-acl-config`](http://docs.derivacloud.org/deriva-py/cli/deriva-acl-config.html#deriva-acl-config) utility reads a configuration file and uses it to set ACLs for an ermrest catalog (or for a schema or table within that catalog).|
|`deriva-annotation-config`|The [`deriva-annotation-config`](http://docs.derivacloud.org/deriva-py/cli/deriva-annotation-config.html#deriva-annotation-config) utility reads a configuration file and uses it to set annotations for an _ERMrest_ catalog (or for a schema or table within that catalog).|
|`deriva-annotation-dump`|Outputs the current set of annotations in use for the specified catalog in JSON format.|
|`deriva-annotation-rollback`|Provides a function to rollback the entire annotation hierarchy for the specified catalog to a given point in time specified by catalog snapshot ID. |
|`deriva-catalog-config`|Provides functions to set up catalog schema and tables with a standard baseline annotation and ACL configuration.|
|`deriva-catalog-dump`|Provides functions to dump the current configuration of a catalog as a set of [`deriva-py`](http://docs.derivacloud.org/deriva-py/index.html#python-command-line-clients-and-api-deriva-py) scripts. The scripts are pure deriva-py and have placeholder variables to set annotations, acls, and acl-bindings.|
|`deriva-csv`|Provides functions to upload `csv` or other table-like data to a catalog with options to create a new table, validate input data and upload data.|
|`deriva-download-cli`|The [`deriva-download-cli`](http://docs.derivacloud.org/deriva-py/cli/deriva-download-cli.html#deriva-download-cli) is used for orchestrating the bulk export of tabular data (stored in _ERMrest_ catalogs) and download of asset data (stored in _Hatrac_, or other supported HTTP-accessible object store).|
|`deriva-hatrac-cli`|The [`deriva-hatrac-cli`](http://docs.derivacloud.org/deriva-py/cli/deriva-hatrac-cli.html) is a command-line utility for interacting directly with the DERIVA _Hatrac_ object store.|
|`deriva-upload-cli`|The [`deriva-upload-cli`]() provides batch upload functionality for both catalog (_ERMrest_) and asset (_Hatrac_) data. This application is generally used for automating the bulk transfer of data to DERIVA servers.|
|`deriva-globus-auth-utils`|The [`deriva-globus-auth-utils`]() provides numerous utility functions for working with the [Globus Auth API](https://docs.globus.org/api/auth/reference/) in addition to Globus Auth Native App login functionality.|

###### Graphical User Interface (GUI) applications
| Executable Name | Application Name | Description |
| --- | --- | --- |
|`deriva-auth`|DERIVA Authentication Agent|Provides credential authentication and refresh services for one or more DERIVA servers. This application is intended to be run in the background after the user completes the login sequence for each server.|
|`deriva-upload`|DERIVA Upload Utility|Provides batch upload functionality for both catalog and asset data. This application is an interactive tool used for the bulk transfer of data to DERIVA servers.|

## Installer packages for Windows and MacOSX
Pre-packaged installers of `deriva-client` for Windows and MacOSX are 
available. 
These installer packages include a bundled Python interpreter and all 
other software dependencies and are recommended for Windows and MacOSX 
users who are looking for a more traditional "turnkey" installation that 
does not require them to install Python and manage Python software package 
installations.  

[Download the installer packages here.](https://github.com/informatics-isi-edu/deriva-client-bundle/releases)


## Installing `deriva-client` from PyPi via `pip`
For users who already have Python installed and are comfortable installing 
Python software via the `pip` application, `deriva-client` can be easily 
installed along with all of it's dependencies directly from 
[PyPi](https://pypi.org/project/deriva-client) using basic `pip` commands.

### Installation Prerequisites

* A Python 3.5.4 or greater system installation is required. The latest 
stable version of Python is recommended. 
* Verify that the appropriate Python 3 interpreter can be invoked from a 
command shell using the `python3` command. This can be tested simply 
with the following command: 

```sh
python3 --version
```

### Installation Quickstart

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

###### Important Note: For MacOSX users running Python 3.5.x with pip version < 9.0.3
If you encounter the following error:
```
Could not fetch URL https://pypi.python.org/simple/pip/: 
There was a problem confirming the ssl certificate: 
[SSL: TLSV1_ALERT_PROTOCOL_VERSION] tlsv1 alert protocol version (_ssl.c:720) - skipping
```
This error means that you cannot update `pip`, `setuptools`, and `wheel` 
via the command provided above. You can work around this error by issuing the 
following commands instead, and then continue with the installation procedure as described. 

```sh
curl https://bootstrap.pypa.io/get-pip.py | python3
pip install --upgrade setuptools
```

###### Windows
The following commands assume a Windows `Command Prompt` command shell is used. For a 
`Powershell` shell, the `activate.ps1` activation script should be invoked instead.
```
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

---

### Installation Procedure

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
        python -m pip install --upgrade pip setuptools wheel
        ```
    2. For _user environments_ execute the following:
        ```sh
        python3 -m pip install --user --upgrade pip setuptools wheel
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

## Source Code
The source code and additional documentation for the primary components of `deriva-client` can be found at the links below: 

* [`deriva-py`](https://github.com/informatics-isi-edu/deriva-py)
* [`deriva-qt`](https://github.com/informatics-isi-edu/deriva-qt)
* [`deriva-catalog-manage`](https://github.com/informatics-isi-edu/deriva-catalog-manage)
