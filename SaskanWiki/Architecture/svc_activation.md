


Services Activation




[Home](./app_help.html) •
 [Application](./app_arch.html) •
 [Services](./svc_arch.html) •
 [Data](./data_arch.html)


# Services Activation


The **Service Activator module** launches or stops the \*\_server.py modules on one or more specific hosts and ports. Strictly speaking it is that port which is a Message Channel, though here the term tends more to refer to the functionality served by that port.
 The activator module executes a set of operating system commands, via a Python script. TThe commands are executed on the host where the activator module is running, in a subprocess, so the activator module is not blocked while the commands are running. The activator module can be run on any host, but it is typically run on the same host as the services it is activating.
 The Admin GUI includes a section devoted to interacting with the activator module. For the current system, the Admin GUI is a locally-hosted PyGame application, not a web app, though it could just as well be implemented as a web applicaiton.
   


  











