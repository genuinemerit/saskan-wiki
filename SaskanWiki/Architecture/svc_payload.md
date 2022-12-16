


Service Message Payload




[Home](./app_help.html) •
 [Application](./app_arch.html) •
 [Services](./svc_arch.html) •
 [Data](./data_arch.html)


# Service Message Payload
A common class called "MsgSequencer", implemented via module "msg\_sequencer.py", handle two asyncio tasks:
 * The "read\_msg" task, which reads bytes from a stream, pulling in the first 4 bytes to get message size, the message package itself.
 * The "send\_msg" task, calculates the size of message, sends that in 4 bytes, followed by the message package.


At present, this class is delivered via the "bow\_quiver" repository. Will likely move it into a common repo with the rest of the code in the interest of keeping the code base consolidated and less confusing.




