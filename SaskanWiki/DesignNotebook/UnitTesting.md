# Unit Testing

Preference is to have structured, repeatable unit test scripts available for all or most major components.

For both Python and Bash, using the VS Code editor with shellcheck and pylint enabled is a good way to help ensure good form and to catch syntax probems early on.  And there is nothing wrong with developing scripts, up to a point, without formal unit test scripts. I am not following a strict test-driven-development methodology.

The "rule" should be that I don't move code to the master branch until there is a unit test script in place. That gives me something that can be used as part of a formal build (which I am not yet doing).

## Python unittest

For Python, use the unittest module to define distinct unit test scripts located in the ``/test`` directory under the parent directory for a given app.  For example:  ``~/bow-data/test``.

I've played around with some of the other Python unit test frameworks; and may come back to them at some point. For now, unittest meets my needs and I understand how to use it.

Unit test modules should be named to reflect the main module they are testing. For example, the UT module for ``bow_creds.py`` is named ``bow_credsTest.py``.  All of the functions within the UT module should be named starting with a 3-digit integer.  This will determine the order in which they are executed.  By and large, every test should be independent.  If dependencies are needed, then create a test with sub-functions.

To execute a set of tests with verbosity turned off:

```sudo python3 -m unittest -v test.bow_credsTest```

To execute a set of tests with verbosity turned on:

```sudo python3 -m unittest test.bow_credsTest```

"Verbosity" doesn't buy a lot. It is displays the name of the module and its docstring.

However, I often include a "DEBUG" mode as well, which is managed via an internal flag that can either be handled in the setup module, or in each test module.  I use this for providing more elaborated displays, which is especially helpful when testing/developing situations where it's useful to see the all the content in requests and responses, even if we are not checking the value of each and every attribute.

Keep in mind that in some cases, particularly with web servers and such, making sure the server itself is up and running properly is and should a separate set of tests from those dealing with a particular set of web or app services.

## Bash bats

``bats`` is a framework for building Bash unit test scripts.
It follows the [TAP protocol](https://en.wikipedia.org/wiki/Test_Anything_Protocol).

For more info, check out:

- ```man bats```
- ```info bats```
- [Bats wiki](https://github.com/sstephenson/bats/wiki/)
