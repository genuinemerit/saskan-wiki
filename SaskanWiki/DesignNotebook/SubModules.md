# Git Submodules

A submodule is a Git repository that is pulled _in toto_ into another repository. This makes it easier to manage collections of functionality that need to be managed like a coherent set up services, but also included within other apps and service collections.

In the case of "Ball of Wax", there's a collection of standard or generic services that I use over and over again, including:

- A class of constants
- A class of generic functions
- A class that handles logging
- A class that handles encryption

These also have corresponding configuration, template or static files in some cases.

I handle this as a distinct Git repo named __bow-quiver__.  The entire repo is imported into other apps and then its functions and objects become easily importable in the style of ``from BowQuiver.bow_logger import BowLogger`` and so on.  Where I need to reference "bow-quiver"-managed configuration, template or static files in a parent app, I make a symbolic link to the relevant file within the embedded BowQuiver app.

Example structure of a "parent" app:

```home/bow-data/BowData```

Then within BowData I load the ``bow-quiver`` repo and run its setup.py.  So now I have:

```home/bow-data/BowData/bow-quiver/BowQuiver```

and can use references to BowQuiver in my ``__init__.py`` modules and so on, as well as referencing any of the file that I need.  This is a local copy of bow-quiver.  Any changes made to the (remote) sub-module do not automatically flow; I have to re-import the "submodule".  How to do this is explained below.

## Managing Submodules

To install as a sub-module:

- See: [git-submodule](https://mirrors.edge.kernel.org/pub/software/scm/git/docs/git-submodule.html)
- See: [Understanding Git Submodules](https://www.speirs.org/blog/2009/5/11/understanding-git-submodules.html)
- See: [Pro Git - Second Edition](https://learning.oreilly.com/library/view/pro-git-second/9781484200766/9781484200773_Ch07.xhtml#Sec75)

The last link above is the best one. I have this book on O'Reilly Playlists / Safari. If I need somewhat more complex steps, that is a good place to start getting oriented. The first link is the ``man`` page for git submodule.  Well worth reading too. Will help with various circumstances and options. The middle link is an OK summary to get started, references similar capabilities in svn.

Basically, from within the parent or "super" module, do:

``git submodule add /path/to/submodule NameOfDirInSuperWhereItGoes``

or

``git submodule add https://github.com/project/module``

and do not identify a target dir name, just "clone" it like you would any other repo
or do provide a target dir name; that is OK too.

Along with the imported sub-module, this will also create a .gitmodules file.
It identifies the source and target of the sub-module.
If multiple sub-modules, then multiple entries in this file.
Then:

``git commit -m "Added submodule my-submodule-name"``

I can do work in the sub-module autonomously, even from within the super-module, since it is a distinct .git.
To refresh it in the super-module after making local changes, treat that directory like any other change:

```bash
git add NameOfSubDir
git commit -m "Advanced SubMod to a new HEAD"
...
```

Note that JUST committing changes in the sub-module will not "auto-reflect" into the super-module.
When cloning a project that has sub-modules, the target dir will be empty. In this case, need to run...

```bash
git submodule init
git submodule update
```

...or, when doing a clone, include the ``--recursive`` option, which will auto init and update any submodules.
I think I'll need to do the ``git submodule update`` if I know the underlying project has been updated??
Not exactly. What you need to do in that case is either:

``git submodule update --remote --merge``

or go into to submodule itself and do a regular pull from master. The above command is easier.
In all likelihood, it will make things easier if we always assume we're pulling in from the master branch of the submodule, but see the man page if you need to pull in from a non-master branch of the submodule remote repo.
