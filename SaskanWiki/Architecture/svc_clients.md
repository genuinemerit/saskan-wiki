


Service Clients




[Home](./app_help.html) •
 [Application](./app_arch.html) •
 [Services](./svc_arch.html) •
 [Data](./data_arch.html)


# Service Client Types
A message client or peer is a functional or procedrual system component that sends requests to and/or receives replies from a message channel. Many of the functional and proceedural components of the application are message clients. They may use common classes to handle the traffic, but each relationship is unique to a client. In this sense, clients are the "nodes" of the overall messaging network.
 There are three main types of **client relationships** to the messaging system:
 * **Transactional**. Very common. Requests use a request-reply broker by and large. Reponses are posted in the Repsonse Message Store (called the "Harvest" in the system namespaces), which are picked up by unique key. In other words, responses are very terse, containing only a key to a persisted response package. See [Service Responses](./svc_response.html) for more information on how this is handled.
 * **Polling Consumer**. This type of client uses publish-subscribe or recipient list channels, which is to say they receive broadcast messages. It is called a polling consumer because the messaging gateway polls through the list of subscribers (consumers) in order to notify them of the message. This type of client is used for the game time server, for example. Responses are still written to the "Harvest" namespace, but it is read by multiple consumers.
 * **Event-Driven Consumer**. This is another kind of a transactional client. There are two flavors. First, the response may be generated not by a request from the client, but by an event in the game (or admin) system to which the client is subscribed. Second, the transaction may be a multi-part, complex one, using a Datatype Channel broker. In this case, the set of messages occurs within a combination of inter-related and interdependent requests and events. For example, an in-game purchase request cannot be initiated unless it has first been established that the desired item is available and a price has been established and agreed-to.


The system metadata defines the characteristics of available client types. Generic base characteristics are defined, then specific versioned instances defined based on those.
 The hierarchy of metadata includes a description of the client type, as well as what specific client-objects are permitted to make the request, or to subscribe to the channel.




