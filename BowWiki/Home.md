# Ball of Wax Home

Welcome to the BoW wiki!

This wiki provides links to topics of interest for users, designers, developers, and testers of the BoW project across all the BoW apps.

This is the wiki for all of the apps in this project.

Trello Kanban boards are used to track tasks at the project level for each app and for the overall Ball of Wax effort. GitHub is the code repository.  GitHub Issues and Pull Requests are used to identify, track and fix problems and incidents, and to review migration proposals.

The Wiki has the following sub-sections:

- [Development](Development/HomeDevelopment/)
- Glossary
- Test Guide

## Wiki features

This wiki uses the [Markdown](http://daringfireball.net/projects/markdown/) syntax.

The wiki is a git repository:

```bash
git clone https://bitbucket.org/ballofwax/bow_orch.git/wiki
```

Just keep everything in the __master__ branch. No need to create branches.

Wiki pages are normal files, with the .md extension. Edit and create them locally, then add, commit, push as normal.

## Syntax highlighting

Highlight snippets of text use lexers, short names and mime types from the [Pygments](http://pygments.org/ )library.

Example of Python code:

```python
#!python

def wiki_rocks(text):
    formatter = lambda t: "funky"+t
    return formatter(text)
```

Here is a link to the [Pygment lexers library][lexers].

[lexers]: http://pygments.org/docs/lexers/
