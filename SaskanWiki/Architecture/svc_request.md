


Service Requests




[Home](./app_help.html) •
 [Application](./app_arch.html) •
 [Services](./svc_arch.html) •
 [Data](./data_arch.html)


# Service Requests
A request is submitted to a channel by message client, or initiated as part of a system event. The request message must be properly formatted or it will be rejected and routed to the Invalid Requests channel.
 The cient sends requests to the approriate channel for that type of message.
 The server(a/k/a Message Broker or Message Controller) receives the request and routes it to the appropriate back-end service. The calls to appropriate content-based routers are documented in the metadata that describes how specific topics, plans, channels and messages work.
 The back-end service processes are Python classes with names like "\_response.py". They are also referred to, colletively, as the Messaging Gateway. See the [Message Response](./svc_response.html) section for more information.
 The back-end service processes the request, including setting the appropriate expiration time, writing the content to the "Harvest" namespece, and returning a key to the server component, which then sends it to the messaging channel. Clients pick up the response key and read the response content from the Response Message Store. The current system relies entirely on message expirations. There is no delete flag created once a message is read from the Harvest namespace. This could change, but that is the current design, aimed at maximizing robustness.




