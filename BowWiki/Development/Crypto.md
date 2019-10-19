# Encryption and Cryptography

## Why

In this day and age, it just makes sense to know something about encryption and how to use it.

If I intend (as a I do, eventually) to have a payment component of my apps, it is a required part of the framework (PCI etc.)  And it is a dis-service to users to make it too easy for bad actors to get access to data they have no right to.

I understand that the major players, the PRC, the USA, the EU and Russians, are all light-years ahead of the rest of us. I won't pretend I'd be able to compete at the level of quantum encryption, for example. But having a grasp on the basics and being able to encrypt when needed is only common sense.

## Options

The programmatic methods I will probably work on are the following:

- From the python crptography package: Frenet method
- From the python gpg package: GPG. This relies on the C++ GnuPG project.
- From the OpenSSL (Linux) package: OpenSSL. Also see Python package:  openssl-python

For options available from service providers:

- Wherever AWS offers encryption at rest, use it
- Consider providing my own keys rather than relying on theirs

## Design

I have designed a simple Python class that handles basic encryption-at-rest functions.

It pre-supposes that encryption keys and encrypted credentials are stored "off-line" (on a specified server) that is identified only in a configuration file.  It can also handle basic file or string encryption.  Use the Frenet method.
