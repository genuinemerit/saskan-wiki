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

This wiki uses both HTML and the [Markdown](http://daringfireball.net/projects/markdown/) syntax.

The wiki is a public git repository:

```bash
git clone https://github.com/genuinemerit/saskan-wiki
```

Currently there is only a __master__ branch.

Wiki pages are edited and create them locally, then added, committed, pushed to GitHub as normal.

## Syntax highlighting

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
