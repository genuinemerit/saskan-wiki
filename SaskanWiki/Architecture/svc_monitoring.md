


Services Activation




[Home](./app_help.html) •
 [Application](./app_arch.html) •
 [Services](./svc_arch.html) •
 [Data](./data_arch.html)


### Services Monitoring


The Services Monitor module reads the Log namespace to display information at summary and detailed levels regarding the state and the status of the server, responder and requestor components of the messaging system.
 These components use the wiretap module to write monitor and log data to the Log namespace.
 The level of information monitoring and logged is driven by configuration settings. For example, how often to log a summary of the state of the system, how often to log a detailed report of the state of the system, how often to log a summary of the state of a specific component, how often to log a detailed report of the state of a specific component, etc.
 Metadata may also drive the generation of warning messages and even automated throttling of the system. For example, if a given channel is receiving heavy traffic, or if analysis has revealed that a given channel expects heavy traffic during certain peak periods, then instructions may be be crafted to automtically bring up more (or to reduce) ports to that channel.
 In an ideal state, collapsed channels could be automatically spun up to handle server or software failures. This is probably more approrpriate once the system is deployed on Digital Ocean, where additional Linux servers, and not only addtional ports under a given Linux server, can be spun up or taken down on demand.
 As the system becomes more hardened, the intention is that the Monitor will be able to provide data to the user/admin and/or to a "smart" (AI/ML) automated observer, which can make adjustments to the system based on the data. As noted, spinning up additional instances of a given type of server to relieve load pressure, avoid bottlenecks, or to prepare for and then throttle back down from known/expected peak load times.
 Designing in such feedback can also help with application design, as they can indicate what features (services) are most commonly or least commonly requested.
   


  



















