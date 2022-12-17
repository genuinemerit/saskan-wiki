# Graph Data

Some types of game data lend themselves to being structured in the form of a graph, also sometimes referred to as networked data. At present, there is an experimental class called "io\_graphs" that loads game data describing places, edited in the first instance in ODF spreadsheets and loaded into pandas data frames, then into a (networkx) graph data structure.

The native python networkx library is used to create the graph data structures, which are persisted to the application's "data" namespace as a pickled object.

Two types of graph data are envisioned: "place" graphs, and "path" graphs.
 * A place graph is a graph of places, where places are nodes, and the edges are the paths between places.
 * A path graph is a graph of paths, where paths are nodes, and the edges are the places between which the paths connect.


Whether or not this approach will facilitate a more flexible and efficient construction, management and use of game world objects, particularly its maps, remmains to be seen.

