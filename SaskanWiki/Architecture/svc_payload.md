# Service Message Payload

A common class called "MsgSequencer", implemented via module "msg\_sequencer.py", handle two asyncio tasks:
 * The "read\_msg" task, which reads bytes from a stream, pulling in the first 4 bytes to get message size, the message package itself.
 * The "send\_msg" task, calculates the size of message, sends that in 4 bytes, followed by the message package.

