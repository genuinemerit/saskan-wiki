# Structures

Name:value pairs with unique names is the fundamental design principle.
The system is not (yet) using Redis or Sqllite or Postrgres. It is using a simple JSON file for each data record, organized into namespaces defined as Linux directories.
Standard key structure is as follows, with each part of the key separated by a colon. Key content should not therefore use the colon character, expect as a part separator. Use of punctuation in the key content is discouraged.
 * Descriptive key part, minimally including a record type identifier with a version number. May have multiple parts, which are separated by a tilde (~).
 * Create timestamp, in the format YYYYMMDDHHMMSS.SSS. All dates and times are assumed to be UTC. There is no need to specify a time zone.
 * Expiration timestamp, in the format YYYYMMDDHHMMSS.SSS.
 * Unique identifier, a cryptographically strong hash.


Persisted data should be compressed and cast to base64 encoding. This is to reduce the size of the data files, and to avoid problems with special characters in the data.
 There are no plans at present to encrypt the data at rest, though that's not a bad idea. For senstive PPI data, it is a must. Such data should also be stored on a separate Linux server altogether.




