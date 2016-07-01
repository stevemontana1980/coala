.. image:: https://cloud.githubusercontent.com/assets/7521600/15992701/ef245fd4-30ef-11e6-992d-275c5ca7c3a0.jpg

coala: Language Independent Code Analysis
-------------
**coala provides a common command-line interface for linting and fixing all
your code, regardless of the programming languages you use.**

With coala, users can create rules and standards to be followed in the source
code. coala has an **user-friendly interface** that is completely customizable.
It can be used in any environment and is completely modularized.

coala has a set of official bears (plugins) for several languages, including
popular languages such as **C/C++**, **Python**, **JavaScript**, **CSS**,
**Java** and many more, in addition to some generic language independent
algorithms. To learn more about the different languages supported and the
bears themselves,
`click here. <https://github.com/coala-analyzer/bear-docs/blob/master/README.rst>`__

|Linux Build Status| |Windows Build status| |Scrutinizer Code Quality|
|codecov.io| |Documentation Status| |Gitmate|

.. Start ignoring LineLengthBear

================================================= ================================================ ====================================================== =========================================================
`Official Website <http://coala-analyzer.org/>`__ `Twitter <https://twitter.com/coala_analyzer>`__ `Facebook <https://www.facebook.com/coalaAnalyzer/>`__ `Video Demo <https://asciinema.org/a/42968?autoplay=1>`__
================================================= ================================================ ====================================================== =========================================================

.. Stop ignoring

-----

.. contents::
    :local:
    :depth: 1
    :backlinks: none

-----

========
Features
========

* Out-of-the-box support for various `popular languages <https://github.com/coala-analyzer/bear-docs/blob/master/README.rst>`__
  such as **C/C++**, **Python**, **Javascript**, **CSS**, **Java** and many
  others with built-in check routines.
* User-friendly interfaces such as JSON, interactive CLI or any custom format.
* Plugins for gedit, Sublime Text, Atom, Vim and Emacs.
* Multi-threading support for optimal performance by parallelizing the routines.
* File caching support - run only on changed files (experimental).

-----

============
Installation
============

To install the **latest stable version** run:

.. code-block:: bash

    $ pip3 install coala-bears

To install the latest development version run:

.. code-block:: bash

    $ pip3 install coala-bears --pre

|PyPI| |Windows| |Linux|

-----

=====
Usage
=====

To get the list of arguments and their meaning, run:

.. code-block:: bash

    $ coala --help

To run coala over your project, create a ``.coafile``, the project-specific
configuration file that will store all your settings for coala. A sample
``.coafile`` will look something like this:

.. code-block:: bash

    [Default]
    files = src/**/*.py
    bears = SpaceConsistencyBear
    use_spaces = True

Store this file in the project's root directory and run coala:

.. code-block:: bash

    $ coala

Please read our
`coafile specification <http://coala.readthedocs.io/en/latest/Users/coafile.html>`__
to learn more.

If you want to quickly test some settings without a ``.coafile``, you
can run:

.. code-block:: bash

    $ coala --files=setup.py --bears=SpaceConsistencyBear -S use_spaces=True

-----

=======
Support
=======

Feel free to contact us at our `Gitter channel <https://gitter.im/coala-analyzer/coala>`__, we'd be happy to help!

You can also drop an email at our
`mailing list <https://github.com/coala-analyzer/coala/wiki/Mailing-Lists>`__.

|gitter|

-----

================
Getting Involved
================

If you would like to be a part of the coala community, you can check out our
`Getting Involved <http://coala.readthedocs.io/en/latest/Getting_Involved/README.html>`__
page or ask us at our active Gitter channel, where we have maintainers from
all over the world. We appreciate any help!

We also have a
`newcomer guide <http://coala.readthedocs.io/en/latest/Getting_Involved/Newcomers.html>`__
to help you get started by fixing an issue yourself! If you get stuck anywhere
or need some help, feel free to drop a mail at our
`newcomer mailing list <https://groups.google.com/d/forum/coala-newcomers>`__
or contact us on Gitter.

|gitter|

-----

=======
Authors
=======

coala is maintained by a growing community. Please take a look at the
meta information in `setup.py <setup.py>`__ for current maintainers.

-----

=======
License
=======

|AGPL|

.. |Windows| image:: https://img.shields.io/badge/platform-Windows-brightgreen.svg
.. |Linux| image:: https://img.shields.io/badge/platform-Linux-brightgreen.svg
.. |PyPI| image:: https://img.shields.io/pypi/pyversions/coala.svg
   :target: https://pypi.python.org/pypi/coala
.. |Linux Build Status| image:: https://img.shields.io/circleci/project/coala-analyzer/coala/master.svg?label=linux%20build
   :target: https://circleci.com/gh/coala-analyzer/coala
.. |Windows Build status| image:: https://img.shields.io/appveyor/ci/coala/coala/master.svg?label=windows%20build
   :target: https://ci.appveyor.com/project/coala/coala/branch/master
.. |Scrutinizer Code Quality| image:: https://img.shields.io/scrutinizer/g/coala-analyzer/coala.svg?label=scrutinizer%20quality
   :target: https://scrutinizer-ci.com/g/coala-analyzer/coala/?branch=master
.. |codecov.io| image:: https://img.shields.io/codecov/c/github/coala-analyzer/coala/master.svg?label=branch%20coverage
   :target: https://codecov.io/github/coala-analyzer/coala?branch=master
.. |Documentation Status| image:: https://readthedocs.org/projects/coala/badge/?version=latest
   :target: http://coala.rtfd.org/
.. |AGPL| image:: https://img.shields.io/github/license/coala-analyzer/coala.svg
   :target: https://www.gnu.org/licenses/agpl-3.0.html
.. |Gitmate| image:: https://img.shields.io/badge/Gitmate-0%20issues-brightgreen.svg
   :target: http://gitmate.com/
.. |gitter| image:: https://badges.gitter.im/coala-analyzer/coala.svg
    :target: https://gitter.im/coala-analyzer/coala
    :alt: Chat on Gitter
