# learn_python
A repo for me to experiemnt with Python as I learn it.
I don't think this will be interesting to anybody but me.


## Table of contents

<!-- mdtoc-start -->
&bull; [skeleton](#skeleton)  
&nbsp;&nbsp;&nbsp;&nbsp;&bull; [Table of contents](#table-of-contents)  
&nbsp;&nbsp;&nbsp;&nbsp;&bull; [Introduction](#introduction)  
&nbsp;&nbsp;&nbsp;&nbsp;&bull; [License](#license)  
<!-- TOC created by '../mdtoc/mdtoc.pl README.md' (see https://github.com/fordsfords/mdtoc) -->
<!-- mdtoc-end -->


## Introduction

Files named "skeleton.*" contain more stuff than the more-minimal "skel.*"
files.

See my [notes](notes.md).


## Resources

* https://docs.python.org/ - official doc home (multiple versions).
* https://docs.python.org/3.11/library/stdtypes.html - Standard types.
* https://docs.python.org/3.11/library/functions.html - Library functions.
* https://docs.python.org/3.11/reference/index.html - Language reference.


## System Changes

For my vanilla WSL2 Ubuntu install, I did:
````
sudo apt install python3-pip
sudo apt install pylint
sudo apt install flake8
````
See [Why apt install](#why-apt-install).


## Why apt install

Apparently you can use `pip` or `apt install` to install `pylint` and `flake8`.
I chose `apt install` because, according to ChatGPT:

When deciding whether to install Pylint (or other Python packages) using apt or pip, consider the following factors:

Using apt (System Package Manager):
* Stability: Packages installed via apt are typically stable and well-tested for the specific version of Ubuntu you're using. However, they may not be the latest version available.
* System-Wide Installation: apt installs the package system-wide, which means it will be available for all users and Python environments on your system.
* Dependencies: apt manages dependencies for the system Python version, which could avoid potential conflicts with other system packages.
* Older Versions: The version available through apt might be outdated compared to the latest version available via pip.
Using pip (Python Package Installer):
* Latest Version: pip usually provides the most recent version of the package, which might include new features and bug fixes not present in the apt version.
* Virtual Environments: pip is better suited for managing packages within virtual environments, allowing you to isolate dependencies for different projects. This prevents conflicts and keeps your global Python environment clean.
* Flexibility: With pip, you can install packages directly from PyPI, custom repositories, or even directly from source code repositories like GitHub.
* Potential Conflicts: Installing globally with pip (i.e., using pip install pylint) could potentially lead to conflicts with system packages, especially if different projects require different versions of the same package.
Recommendation:
* For General Use: If you're using Pylint system-wide and don't need the latest features, installing it via apt is a good choice for stability and ease of maintenance.

For Development: If you want the latest version or if you are working within a virtual environment, pip is preferable. When using pip, it's generally recommended to use it within a virtual environment to avoid system-wide conflicts.

Using pip within a virtual environment gives you more control and flexibility, which is often preferred for development work. However, if you're setting up a system-wide environment and prefer stability, apt is a solid option.


## License

I want there to be NO barriers to using this code, so I am releasing it to the public domain.  But "public domain" does not have an internationally agreed upon definition, so I use CC0:

Copyright 2024 Steven Ford http://geeky-boy.com and licensed
"public domain" style under
[CC0](http://creativecommons.org/publicdomain/zero/1.0/):
![CC0](https://licensebuttons.net/p/zero/1.0/88x31.png "CC0")

To the extent possible under law, the contributors to this project have
waived all copyright and related or neighboring rights to this work.
In other words, you can use this code for any purpose without any
restrictions.  This work is published from: United States.  The project home
is https://github.com/fordsfords/learn_python

To contact me, Steve Ford, project owner, you can find my email address
at http://geeky-boy.com.  Can't see it?  Keep looking.
