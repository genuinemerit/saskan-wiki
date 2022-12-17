# Service Message Structures

Each message has a specific physical structure defined by metadata and implemented by a message structure class.

## Message Hierarchy

The structured messages have a hierarchy as well as specific record layouts. The level of complexity of the hierarchies depends on the the needs of the topic and the complexity of the channel.
 Topic definition sit at the top of the hierarchy. This identifies what "family" a message belogs to. Within a topic are **plans** describing a logically-connected group of messages. For example, a set of request and response messages involved in the movement of an avatar from one location to another on a map. These messages are logically connected and are grouped together in a plan.
 A plan can involve more than one channel. For example, the avatar movement plan may involve a request to move the avatar, a response to that request, and a notification to other game objects that the avatar has moved. These messages are logically connected and grouped together in a plan, but the messages are handled by two distinct channels.
  Finally, there is a specific schema (record layout) for each individual message. It is defined by metadata and implemented by one or more message structuring classes.

## Message Schema

Messages sent over the network are encoded in JSON. The JSON is compressed using the GZIP algorithm. The compressed JSON is then encoded using the Base64 algorithm. The Base64 encoded string is then sent over the network along with a sizing block.
 A message schema is defined minimally as a type and an object which describes its form.
 Types are complex: record, enum, array, map (a/k/a hash), union (combination of other types), or fixed/binary (a byte string). In the game world and its admin software, the current intention is that all schemas will be records to start out wtih. Other types will be deployed only as/when needed.
 Every Saskan message schema has a **name** to identify what logical message or messages (memmber/s of a Plan) use the schema. Typically this includes an indication of its role in the plan, for example inclding a term like "\_request" or "\_reply" in its name.
 Every message schema also has a version number, which is part of its name. This helps to manage change over time, similar to how a well-designed RESTful system works.
 The name of a schema is usually qualified by a channel name, plan name and/or topic name. The idea is to encourage re-use and simplicity. No need to create new base message schemas if in fact the same structure is simply being shared across multiple service plans. This type of sharing is managed at the metadata level.
 The message **object** is typically a collection of fields where each field has a name and a type. Fields may have optional attributes too, like fixed values, default values, or enumerated values (lists).
 Types include: int, long, float, double, string, boolean, bytes, null and binary.
 Optional attributes include:
 * *default*: default value for field
 * *order*: order of field in record
 * *aliases*: list of aliases for field
 * *doc*: documentation for a speicific field


Within the Python classes, message structures are handled using standard Python objects and types. These are converted to JSON when the message packages are constructed. Archived messages are stored in GZIPped, Base64-encoded JSON format, preceded by a 4-byte sizing block, that is, in the same format used when transmitting them as a payload across the network.

