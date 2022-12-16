


Service Brokers




[Home](./app_help.html) •
 [Application](./app_arch.html) •
 [Services](./svc_arch.html) •
 [Data](./data_arch.html)


# Service Brokers
A Channel is a specific implementation of a type of Broker. The terms are sometimes used inter-changeably. Just keep in mind that there may be multiple implementations of, for example, a Publish-Subscribe broker within the game system. Each implementation is a Channel.
 Broker types are:
 * **Request-Reply**. Also called request-response, this is for handling transactional messages. A single client, for example, an Actor in the game, requests a specific type of service, for example, to move its avatar to a specific target. The response is delivered to a single client, the Actor, which is the only one who can consume the response.
 * **Publish-Subscribe**. This is for handling broadcast messages. A single client, for example, the game events server, publishes a message to all clients who have subscribed to the channel, for example, all the Actors in a given zone. The message is delivered to multiple clients who have subscribed to the channel. This type of channel might be used for a chat channel.
 * **Recipient List**. This is another flavor of a broadcast channel. A single client, for example, the game time server, publishes a message to a pre-defined list of clients. This type of channel can be thought of as a "push" broadcast because the server decides which clients should recieve the message.
 * **Datatype Channel**. This is a more sophisticated breakdown of a Request-Reply broker. The client sends a request to the server, which is a request to create a new instance of a datatype. The server responds with a new instance of the datatype. The client can then send updates to the server, which will update the instance. The client can also send requests to the server to delete the instance. This type of broker is used for game objects, for example, a player's avatar. Furthermore, a datatype channel typically provides multiple inter-related sub-channels. For example, there could be a datatype channels relating to purchases on a game marketplace. A market-query determines if any item is available at a given market, perhaps info about quantity and quality. The market-price-quote sub-channel handles haggling over the price. The actual purchase and exchange of goods is handled by the market-purchase-order sub-channel (and perhaps others). A Datatype Channel can be thought of as a kind of network of inter-related request-reply channels.
 * **Peer-to-Peer**. This is for handling direct messages between two clients. This type of broker is used for private chat, for example.
 * **Invalid Message**. This is for routing log messages to the appropriate log file when no response can be found for a given request.


The system metadata defines the characteristics of brokers (channel types) which are available within the system. And it also defines what specific implementations of those channel types are available within the system. The system metadata also defines the characteristics of the channels themselves, for example, the topic, the controller, and the set of peers (clients) who are subscribed to the channel, along with the name and version of the channel.




