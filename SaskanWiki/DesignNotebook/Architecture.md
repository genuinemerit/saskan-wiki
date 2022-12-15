# Ball of Wax Architecture

## Languages

The focus is mainly on Python3, with JavaScript and Bash scripts as needed.

## Apps and Repositories

Code is organized into discrete GitHub repositories. Each repository may contain one or more applications, along with other code.
Apps listed in this section are the ones currently deployed to either a Master or Develop branch in GitHub.

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

### Services and Resources

Each application generally supports one to many RESTful services. It may also provide classes that provide for directly instantiable/callable objects. In some cases static resources like HTML templates or configuration files are included.

All networked services are provided using _Tornado_ behind a _Nginx_ load balancer. Only TLS2 is supported. HTTP requests are auto-converted to HTTPS requests.

The following notes reflect current state of design for services and resources. Those appended with an asterisk have not been coded/tested yet.

Front-end:

- __bow-orch__:_BowReg_*
  - view: GET BowVisit
  - api: GET, POST BowConnect
  - api: GET, POST BowRegister
  - api: GET, POST BowLogin

- __bow-res__:_BowPlace_*
  - view: GET BowPlaces
  - api: GET, POST BowPlacesConnect
  - api: GET, POST BowPlacesFind
  - api: GET BowPlacesGet
  - api: POST BowPlacesSet

- __bow-lang__:_BowLang_*
  - Similar to bow_res

- __bow-gen__:_BowGen_*
  - Similar to bow_res

Middleware:

- __bow-orch__:_BowAuth_*
  - api: GET, POST BowAuthUser
  - api: GET, POST BowAuthSession
  - api: GET, POST BowAuthMessage

Back-end:

- __bow_quiver__:_BowQuiver_
  - /: CALL BowLogger
  - /: CALL BowConstants
  - /: CALL BowFunctions
  - /: CALL BowEncrypt
  - model: INCLUDE configurations
  - view:
    - static: INCLUDE robots.txt
    - templates: INCLUDE base HTML

- __bow-data__:_BowData_ (partially coded)
  - view: GET BowCredsShow*
  - api: GET BowCredsGet
  - api: POST BowCredsSet
  - api: GET BowPlacesGet*
  - api: POST BowPlacesSet*
  - model: CALL BowRecords
  - model: GET, PUT, PATCH, DELETE BowCredsData
  - model: PUT BowCredsSeed
  - model: GET, PUT, PATCH, DELETE BowPlacesData*
  - model: PUT BowPlacesSeed*
  - store: READ, WRITE db*
  - store: READ, WRITE pix*
  - store: READ, WRITE vault/.secrets

### Diagrams and Sketches

Diagrams are created using LucidChart. See the online [BallOfWax collection](https://www.lucidchart.com/documents#docs?folder_id=151197380&browser=icon) for in-progress versions.

Static copies are exported, generally as PNG files, and added to bow-wiki:BowWiki.
See:

- [BoW Services Architecture](diagrams/Bow_Services_Architecture.png) PNG
