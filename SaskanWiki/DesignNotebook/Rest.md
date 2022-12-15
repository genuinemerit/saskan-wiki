# Requesting and Listening for REST calls

## Why

Representational State Transfer is a widely used pattern. It helps to keep code organized, and it encourages
us to think in terms of Services.  This in turn creates an architecture that is flexible, anti-monolithic, adaptable
to distributed environments.

Python provides strong support for both REST and other networking options. For Ball of Wax, the default form of messaging is RESTful request-response.  If and when I find a need for chattier channels, I'll look harder at Web Sockets.  If and when I find a need for batchier channels, I'll look harder at the various pub-sub options.

The main programming frameworks and tools involved are:

- __Tornado__ for listening, taking action based on requests
- __Nginx__ for implementing security and load balancing in front of Tornado services
- The Python __requests__ module for making calls to services and catching the replies programmatically
- The command line tool __httpie__ for rapidly testing service calls

Of course many other options are available. These are the ones I will rely on for now.
Some other tools that are likely worth taking a look at include:

- Postman for testing service calls
- SwaggerHub for documenting and standardizing the structure of REST calls

## Tornado

For each method that catches a request, we pass in args and kwargs. Evaluating the parameters is one way to handle the URL and query parameters.

Your main friend when processing REST calls in Tornado is the __self.request__ object.
Decode its __body__ attribute to get data passed in the request body. Example:

``body_data = json.loads(self.request.body.decode('utf-8'))``

Handling request headers is slightly odd in that they are availabe in __self.request.headers__, which allows referencing them explicitly by name, like ``host_port = self.request.headers["Home"]`` for example.  But I haven't yet figured out any way to simply list all of the header name:values that arrived in a request.

## requests

A nice wrapper around the Python urllib, __requests__ works like this..

``response = requests.put("https://data.genuinemerit.org/creds",
                          headers=header, data=data, verify=True)``

..where "header" and "data" are Python dicts.  "verify=True" means you want it to check for valid TLS credentials.
It supports all of the main verbs.

Things we can do with the response:

- pp(response)
- pp(response.json())
- pp(response.url)
- pp(response.headers)
- pp(response.text)
- pp(response.history)
- pp(response.status_code)
- pp(response.exceptions)

## httpie

A nice alternative to CURL (which is still awesome, and is probably better for more complex situations), __httpie__ works like this...

To pass query params in httpie, use __name=='value'__ pairs using double equals, like:

``http -v GET https://char.genuinemerit.org/places/info about=='this_place'``

To pass extra or home-grown Request headers using httpie, list the __name:value__ pairs after the URL using a colon, like:

``http -v GET https://char.genuinemerit.org/places/info X-API-Token:12345677``

To test POST, PATCH or PUT with httpie,

- For data fields: [name]='value' (single equals sign)
- For pulling data in from a file:  [field]=@file.txt  (equals and at)
- For forcing use of application/x-www-form-urlencoded, prefix with --form (or -f)
- For file uploads via forms protocol: [field]@/dir/file (at)
- For raw JSON fields: [name]:='value' (colon and equals)
- Can also provide data inputs using redirected input

Examples..

Simple data:
    ``$ http POST http://localhost:1337 data='hello world' name='Phoenix Quinn'``

Embedded raw JSON using :@ syntax:
    ``$ http POST http://localhost:1337 data:@'["item1", "item2"]'``

Redirected input
    ``$ http POST http://localhost:1337 < redirected_data.json``

To force use of application/x-www-form-urlencoded; charset=utf-8 use --form, like:
    ``$ http --form POST http://localhost:1337 data='hello world' name='Phoenix Quinn'``

Serialized JSON object in a form, use =@
    ``$ http --form POST http://localhost:1337 data=@myobject.json``

To simulate a file upload, use @
    ``$ http --form POST http://localhost:1337 avatar_pix@'pix/PhoenixQuinn.png'``

The instructions on HTTPIE manual are a little unclear and maybe contradictory (or it took me a while to "get it").

For "raw JSON" (without forms) it is either = or :@ or =@

- = is for embedded "raw JSON" as a data item value
- :@ makes it a header item
- =@ is for data items and it has to be a file
- In all cases, use single quotes around the entire JSON expression

The "-v" param is for "verbose". It means "show me the request header and body" along with the response.

Example of a mildly-complex httpie call:

``http -v PUT https://auth.genuinemerit.org:56057/auth/key X-BoW-Internal-IP:"10.132.105.225" WWW-Authenticate:"BoW" app_name="bow_auth" port_range="56055:56059" serv_id='[{"method":"PUT", "app":"bow_auth", "path":"/auth/key"}]'``
