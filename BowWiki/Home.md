# Ball of Wax Home

Welcome to the BoW wiki!

Although hosted under the ``bow_orch`` repository, this wiki provides links to topics of interest for developers, testers and users of the BoW project across all the BoW apps.

This is the wiki for all of the apps in this project.  The Trello boards associated with bow_orch are likewise the Kanban boards for the entire proejct, not only for that repository.

Think of ``bow_orch`` as the Admin and Management app for the project. It handles set-ups, deployments and monitoring for each of the apps.  From a development perpsective, think of it as the Program Manager. And from a delivery perspective, it is like the Release Manager.

## BoW topics

- How to create and manage a Python [virtualenv](/ballofwax/bow_orch/wiki/Virtualenv/)
- Handling load balancing and security using [Nginx](/ballofwax/bow_orch/wiki/Nginx/)
- How to deploy a Python application "the right way" using [setup.py](/ballofwax/bow_orch/wiki/SetupPy/)
- Handling [orchestration](/ballofwax/bow_orch/wiki/Orchestration/) for configuration of Linux accounts and servers
- Handling [encryption]((/ballofwax/bow_orch/wiki/Crypto/)) in the Ball of Wax
- Making [REST calls]((/ballofwax/bow_orch/wiki/Rest/)) when using and testing the Ball of Wax (httpie, requests, tornado)

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
