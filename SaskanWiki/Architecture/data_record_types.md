# Record Type / Categories of Data

Most stored textual and numerical data is organized as JSON data.

 Message formats are defined using a more explicit JSON schema. See [Service Message Structures](./svc_structure.html) for more detail.

 In some cases, data are managed in an ODF spreadsheet, then loaded to pandas dataframes, transformed into graph data, and then stored as pickled networkx objects.

 - Image data are stored as binary files using PNG, JPG and other standard image formats.
 - Sound effect files will likely be WAV or OGG formats.
 - Music files will likely be stored as MIDI, though some may be "compiled" into WAV or OGG.
 - Animation effects will be handled by PyGame. Not sure yet if OpenGL will be used. No plans at this point to serve up video files.




