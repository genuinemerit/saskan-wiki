# Service Topics

By and large, a topic is handled by a single service component across a single channel, but there is nothing to prevent use of multiple channels for a given topic if it makes sense to do so.

Likewise, multiple topics can be handled on the same channel.


The following topics are currently under consideration:

* **Logging**. This topic has the wiretap module as its primary client. It is used to log messages and other information to a file or database. It is also used to send messages to the console in order to report on debug/trace/info event, errors, warnings, or failures.
 * **Monitoring**. This topic also has the wiretap module as its primary client. It is used to send messages to the console and to a database in order to report on the status of the system. For example, to record the number of messages sent and received over a given channel in a period of time.
 * **Movement**. This topic has a game play module as its primary client. It is used to manage movement of avatars around the game world, for example on a map or within a scene.
 * **Timeline**. This topic has a game play module as its primary client. It is used to direct the development of events according to a script, or to track the in-game date-time progression in relation to game activities.
 * **Chat**. This topic has a game play module as its primary client. It is used to handle communications between players.
