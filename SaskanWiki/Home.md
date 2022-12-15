# Saskantinon Home

Welcome, huum and sint alike, to the Saskan wiki!
This wiki is produced by a group of Free Jaxen working at at undisclosed location in the Southern Krunkinotto.


It provides links to topics of interest for users, designers, developers, and testers of the Saskantinon project -- both the apps and the novel(s).

GitHub is the code repository.  GitHub Issues and Pull Requests are used to identify, track and fix problems and incidents, and to review migration proposals.

The Wiki has the following sub-sections:

- [DsignNotebook](DesignNotebook/d_Home.md)
- [Architecture](Architecture/a_home.html)
- [GameGuide](GameGuide/g_home.md)


## Wiki features

This wiki Repo hosts both HTML pages and files in the [Markdown](http://daringfireball.net/projects/markdown/) syntax.

saskan-wiki is a public git repository. To clone it:

```bash
git clone https://github.com/genuinemerit/saskan-wiki
```
Currently there is only a __master__ branch.

The HTML (and other) files stored in the repo, but not hosted under its wiki sub-repo, are used as reference materials. They may or may not eventually be incorporated into the wiki itself, or into other documentation or Help systems.


The actual wiki pages are edited and created in the `wiki` sub-system of this repo. That is effectively a separate repo. To locally edit the MD files in the wiki itself:

```bash
git clone https://github.com/genuinemerit/saskan-wiki/wiki/wiki.git
```


## Markdown syntax highlighting

Highlight snippets of text use lexers, short names and mime types from the [Pygments](http://pygments.org/) library.

Example of Python code:

```python
#!python

def wiki_rocks(text):
    formatter = lambda t: "funky"+t
    return formatter(text)
```

Here is a link to the [Pygment lexers library][lexers].

[lexers]: http://pygments.org/docs/lexers/
