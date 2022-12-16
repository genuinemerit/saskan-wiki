# Technology Stack

GUI engine: PyGame

 Backend data are managed in the style of a "not only SQL" data manager like Redis. At present this is implemented using proprietary methods. Data is stored as immutable Python objects pickled to an in-memory data space ("/dev/shm"), using a distinctive set of keys that include expiration information. Data are converted to JSON and persisted when necessary.

 A formal ontology provides the foundational basis for describing data structures, relationships and meanings. Application metadata and configuration settings are coded as JSON. Some game data is designed in ODF spreadsheets, loaded into the app using Pandas and may be pickled as networked-data objects.

 Nearly all programming is done in Python3.10 under an anaconda virtual environment, using the VS Code editor.

 The app ontology is managed as an OWL structure edited using the Protege editor. Relational database, if needed, will be implemented at first using SQLite, then likely to be moved to Postgres.

 Code is versioned on GitHub. The repository is:
 * https://github.com/genuinemerit/bow-data-schema
* https://github.com/genuinemerit/bow-quiver


All testing and development takes place on Ubuntu Linux.




