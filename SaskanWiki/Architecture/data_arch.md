# Data Architecture

Configuration data are coded as editable JSON files. These are loaded to the application "data/config" space at install time and stored as pickled objects during program execution.

 Persistent game-context data, such as place definitions and descriptions or music scores, are coded either as ODF spreadsheets or generated by special algorithms, then persisted into the application "data/game" space at install time as pickled objects.

 Images used in GUI components are created using a variety of tools and stored as binary image files in the application "images" space.

 All data used during execution are stored as either pickled objects or copies of binary files in shared memory (/dev/shm) during a session and accessed as key-value data records. This includes the configuration data, the game state, images, the musicology data, the service responses and so on. Inserted or modified data which need to be persisted between sessions are converted to JSON and stored in the application "save" space.

 During session execution, data is organized into high-level namespaces and stored as records, using a variety of structures, with unique keys. The key includes a record type specification, a create timestamp, an expiration timestamp, and a unique identifier. Additional indexes and lists are created in-memory as needed.

 In Linux terms, the records are files stored either under the application directory, which resides under the user's home directory, or in shared memory. The "data" space is a directory; the "config" and "game" are its subdirectories. The "save" and "images" spaces are a subdirectories of the application directory.

 From a design and architecture point of view, information about data can be divided into several categories:
 * [Namespaces](./data_namespaces.html)* [Record types](./data_record_types.html)* [Record structures](./data_record_structs.html)* [Graph Data structures](./data_graphs.html)


















