# Python Application Packaging

As I move towards wanting to deploy a Python app inside a container, starting with Pyhon venvs, but also (eventually) Docker containers, maybe conda environments, and so on, it makes sense to simplify the purely "app" part of the deployment as much as possible.

My current approach to Python application architecture is pretty clean, with a relatively small number of diretories involved. But it stil requires something like doing a git pull or git clone.

My understanding is that with ``setup.py``, I can package up my python (and related) components more cleanly and simplify their deployment into a targeted enviornment.

## Terminology and References

Some of the aspects of using setup.py include:

- Python ``ditutils`` package.  The original approach, being phased out
- Python ``setuptools`` package. Replaced distutils in 2004
- Python ``wheel``.  A way to crfeate & distribute a cross-platform pre-compiled binary
- Python ``twine``.  For uploading distributiong to PyPI
- Using PIP locally?  Don't think that is a thing. Maybe using ``pip install .`` ?
- Using ``__init.py__`` in a prescriptive manner is part of the setuptools framework.
- Using PyPI, the Python Packaging Index. This is how to publish a module for public use.
- Using venv and virtualenv. See my wiki notes on these topics.

The ``setup.py`` file looks something like a Docker configuration. It describes the app, what packages it requires, and so on.  Apps constructed using it following a prescriptive file tree structure. It works something like a make file. All Pip does is run setup.py files. The setup.py file is part of the setuptools framework.

Something of interest to note is that packages can be identified as dependencies to be downloaded from specific links, rather than from PyPI. This might be useful during development, of if a given component is not intended to become open-source.

Next-level topics cover pulling in C modules, compiling under cython, pulling in dependencies other than Python ones, and so on.

This is a new area of learning for me. Some useful references are:

- [StackOverflow: What is setup.py?](https://stackoverflow.com/questions/1471994/what-is-setup-py)
- [python.org: Installing Python Modules using Pip](https://docs.python.org/3/installing/index.html#installing-index)
- [python.org: Distributing Python Modules](https://docs.python.org/3/distributing/index.html#distributing-index)
- [python.org: Recommended Tools](https://packaging.python.org/guides/tool-recommendations/#packaging-tool-recommendations)
- [python.org: Python Packaging User Guide](https://packaging.python.org/) -- The Bible
- [setuptools Documentation](https://setuptools.readthedocs.io/en/latest/) -- This is what I really need to learn
- [setuptools code base](https://github.com/pypa/setuptools)
- [setuptools tutorial](https://pythonhosted.org/an_example_pypi_project/setuptools.html) -- May be a little dated, but worth reading

## Notes

My initial attempts were not bad. I got some things generated. But I am not sure I fully understand how to use them and where to go next with this side of things.

I am going to let this hang for a while and not get too bogged down in it.  I have been doing a lot of "infrastructure" level work lately and now I want to go back and work some on the creative, application side of things, particulary the character- and scene-generation stuff.

For now, I am going to be satisfied with using "bow_orch" to set up and deploy environments, accounts and runtime enviornment for each app. And I will continue to develop it as an admin, deployment and monitoring application.  But for deploying the actual apps, I'll stick with using git for now.  Though I will probably adopt the file structure described in some of the setup.py instructions.

All good. I keep learning, which is the main thing I am after.  And having fun.

## Namespace packages

Not entirely sure I follow all the discussions, but I think I'm getting that there are two basic patterns for defining a package.

- Regular or traditional package, which is not a "namespace" package
- Namespace package, which follows [PEP 420](https://www.python.org/dev/peps/pep-0420/) and only works for PIP and Python3

Namespace packages organize code like:

    project1
        parent
            child
                one.py
    project2
        parent
            child
                two.py

..which allows us to combine project1 and project2 into a common import. (?) They do NOT use the ``__init.py__`` file.
Not entirely clear to me yet what the alternative is.

Traditional packages organize code like:

    project
      ``__init.py__`` names the proejct and maybe does some other stuff
      sub-package-a
        one.py
        two.py
      sub-package-b
        one.py
        two.py

Guess I'll try each approach and see where that gets me. I am finding more examples of the traditional approach, so I might just start there.  Pulling stuff generated from SwaggerHub (using CodeGen) for Python is instructive.  It creates code orgnized something like this for building API's:

    <project_name>
      docs
        <an .md file for each .py file in the api or models directory>

      <app_name>
        api
          _example_:
          admins_api.py  -- Code for specific services available to admin role
          developers_api.py -- Code for specific services available to developer role
          ``__init__.py`` -- Import the Classes from these ^ modules, like:
            from app_name.api.admins_api import AdminsApi
            from app_name.api.developers_api import DevelopersApi

        models
          _example_:
          inventory_item.py -- IO module to get, set values relating to inventory
          manufacturer.py -- IO module to get, set values relating to manufacturer
          ``__init__.py`` -- Import the Classes from these ^ modules

        <no sub-dir> -- generic-level modules for the app
        _example_:
        api_client.py -- generic API client wrapper. This might be my tornado program?
        configuration.py -- set config values, logging, authorization keys and so on
        rest.py -- a generic networking module. I'd probably use tornado instead
        ``__init__.py`` -- Import the Classes from all of these ^ modules and the lower-level ones
        _example_:

          # import apis into sdk package
          from app_name.api.admins_api import AdminsApi
          from app_name.api.developers_api import DevelopersApi
          # import ApiClient
          from app_name.api_client import ApiClient
          from app_name.configuration import Configuration
          # import models into sdk package
          from app_name.models.inventory_item import InventoryItem
          from app_name.models.manufacturer import Manufacturer

      test
        <.py test_ module for each api or modules py module>
        ``__init__.py`` -- empty

      git_push.sh -- Git-related commands. Could replace this with a .py module using gitpython
      README.md
      requirements.txt
      setup.py -- Set this up to configure pip installs from git
      test-requirements.txt
      tox.ini -- Don't know what this is



