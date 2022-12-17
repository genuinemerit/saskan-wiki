# Service Responses / Messaging Gateway

See the [Service Message Requests](Requests) section for a contextualization of the message response process flow.

There are likely to be many `*_reponse.py` modules, but they all have functions in common:

* **Message Expiration**>. The lifetime of a message is typically limited to a few seconds, though some might need a longer lifespan. The message expiration is set by the gateway according to the metadata defining the message and its context. There is a "sweeper" process that continually checks for expired message in the Harvest namespace and archives or deletes them.

* **Harvest IO**. Write message content to the shared memory namespace per format defined by metadata.

* **Broker IO**. Return the key to the Harvest record to the message broker. (Not sure yet what this communication process consists of...async call I think.) This is also the point at which a message may be routed to an Invalid Message broker rather than its originally-intended channel.

