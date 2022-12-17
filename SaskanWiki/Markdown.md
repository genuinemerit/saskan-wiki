# Markdown Notes

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
