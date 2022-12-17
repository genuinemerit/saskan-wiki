# Services Metadata

The experimental design intention is to make the system flexible and anti-fragile. By defining all services as metadata, it is hoped that modifications can occur largely by observing and testing behaviors which can be added, tweaked, removed, refactored without a great deal of re-compling/re-deploying program code.

 Services metadata is implemented in the first instance as JSON files held in the "config" namespaces and organized into the following categories:
 * **Controllers** - A Controller manages a Service Namespace. Metadata about the Topics it handles, what Brokers it uses.
 * **Brokers** - What types of Message Brokers are available and their characteristics, such as what kind of Channels they serve.
 * **Channels** - What types of Response Channels are available and their characteristics.
 * **Topics** - Metadata concerning logical categories of messages, typically organized around semantic or functional themes.
 * **Message Structures** - Generic and specific message record structures. Message hierarchies under each topic.
 * **Requests** - For a given Topic, what Request messages are defined, their rules and characteristics.
 * **Replies** - For a given Request, what Reply messages are defined, their rules and characteristics.


By using an ontology as the foundation, it is further considered that the design of both the services architecture and game content could be developed and changed in a manner that is flexible, controlled and obvious. To this end, there is the idea, for example, that SQL code (once a SQL engine is added) could be auto-generated as much as possible based on interpretation of behavioral use case patterns. (This is not yet implemented.) Or similarly that other types of code could be auto-generated, perhaps with the help of an AI engine of some kind.

