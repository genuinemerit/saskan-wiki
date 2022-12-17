# Overview of Application Functions and Procedures

Along with its message-based services layer, the Saskan software ecosystem also uses several types of more traditional software components.

### Functional Components

Python classes providing generic functions used by many other classes are referred to as **functional components**. These include:
 * File IO, including metadata management, pickling and persistence
 * Record IO, for handling construction of specific data record types
 * Message IO, for handling construction and sequencing of specific message payloads
 * Shell IO, providing calls to operating system functions
 * Music IO, handling MIDI and audio file construction and playback, including manufacturing of scores
 * Time IO, providing time and date functions set in the game world
 * Wiretap IO, managing logging and monitoring functions
 * Graphs IO, for manipulating and displaying graph data, including maps
 * Reports IO, for generating and displaying reports

Software modules implement python classes which provide those features exposed as methods callable by other compoments.


### Procedural and Event-Driven (GUI) Components

**Procedural components** (python classes with a "\_\_main\_\_" hook) are like a script that executes a particular task one time. The main procedural component is **saskan\_install.py**, which installs the software under the user's home account on Linux and in the /dev/shm memory space. It is run from the command line, via a bash script, requires sudo-level privileges, and communicates directly to the console.
 
 **Event-Driven components** (python classes with a "\_\_main\_\_" hook and a pygame event loop) use the PyGame library to provide a GUI. The main event-driven component at present is **saskan\_eyes.py**, which provides a GUI for the admin application components. It is launched from the command line, via a bash script. The intention is to provide one or more additional GUI compoonents, tentatively, **saskan.py** for the game itself.
