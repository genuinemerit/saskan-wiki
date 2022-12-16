# Services Activation

The **Service Activator module** launches or stops the `*_server.py` modules on one or more specific channels.

The activator module executes a set of operating system commands, via a Python script. TThe commands are executed on the host where the activator module is running, in a subprocess, so the activator module is not blocked while the commands are running. The activator module can be run on any host, but it is typically run on the same host as the services it is activating.

The Saskan Admin GUI includes a section devoted to interacting with the activator module. For the current system, the Admin GUI is a locally-hosted PyGame application, not a web app, though it could just as well be implemented as a web applicaiton. Eventually, the intention is to convert the game system to operate over the Internet.  In order to support higher-end video and sound, and to reduce network traffic, end-user GUI's and some aspects of the game engine will likely remain locally installed, with the network used only for message traffic requiring shared resources or intra-player communications.

