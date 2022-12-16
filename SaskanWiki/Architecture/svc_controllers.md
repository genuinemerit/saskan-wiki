


Service Controllers




[Home](./app_help.html) •
 [Application](./app_arch.html) •
 [Services](./svc_arch.html) •
 [Data](./data_arch.html)


# Service Controllers
The Controller component directs the traffic on a given Channel. This component is often referred to as a Server.
 It is implemented as a python class with a module name like "[servicens]\_server.py".
 The controller component has two asyncio tasks:
 * The "server" task, which handles a stream reader and a stream writer. On a specified host and port, it waits for and gathers messages for a given channel, which is subscribed to by a set of peers. When a message is received, then it is passed along to the channel's subscribers.
 * The "main" task, which launches the server.


The controller components are collectively referred to as the Message Brokers.
 Along with handling traffic on the channels they also operate as Content-Based Routers, meaning they send requests to the appropriate back-end response handlers as needed. In more complex cases, the content-based router may be a separate object from the base controller.
 The reponse components return a key to the message broker, which is what gets posted as a reply on the channel. The client can then use the key to retrieve the message from the Harvest namespace.




