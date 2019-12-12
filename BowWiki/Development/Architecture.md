# Ball of Wax Architecture

## Languages

The focus is mainly on Python3, with JavaScript and Bash scripts as needed.

## Apps and Repositories

Code is organized into discrete GitHub repositories. Each repository may contain one or more applications, along with other code.

- __bow-lab__: Master branch only
  - _setup_: scripts used when creating an environment, including Nginx configuration
  - _tools_: miscellaneous utlities

- __bow-data__:  Master and Develop branches
  - _BowData_: Back end app. Model and store level services. Includes __bow-quiver__ sub-module.
  - _test_: unit tests for _BowData_

- __bow_wiki__: Master branch only
  - _BowWiki_: App for deploying development wiki pages and documentation.
  - _Wiki_: GitHub wiki for end-user-facing documentation.

- __bow-quiver__:  Master branch only
  - _BowQuiver_: Sub-module providing generic, cross-functional calls and services

- __bow-gen__: Initial rendering services for a world or scenario

- __bow-lang__: Glossary and language services

- __bow-res__: Character, place, resource management services

- __bow_orch__: Build, deploy, admin, authorize, monitor services

- __bow-story__: Expository materials. May just replace this with Scrivener project.

## Design

Diagrams are created using LucidChart. See the online [BallOfWax collection](https://www.lucidchart.com/documents#docs?folder_id=151197380&browser=icon) for in-progress versions.

Static copies are exported, generally as PNG files, and added to bow-wiki:BowWiki.
See:

- [BoW Services Architecture](diagrams/Bow_Services_Architecture.png)
