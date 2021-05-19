<a name="table-of-contents"/>

# Python Style Guidelines

- [***Docstrings***](#docstrings)
  - [**Google**](#google-docstrings)
  - [**reSt**](#rest-docstrings)
  - [**Epytext**](#epytext-docstrings)
  - [**Numpydoc**](#numpy-docstrings)
  - [**Converting/Generating**](#converting-docstrings)


----------------------------------------------------------------------


<a name="docstrings"/>

### Docstrings


<a name="google-docstrings"/>

##### Google

Google has their own [format](https://github.com/google/styleguide/blob/gh-pages/pyguide.md#38-comments-and-docstrings) that is often used. It also can be interpreted by Sphinx (ie. using [Napoleon plugin](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/)).

```python
"""
This is an example of Google style.

Args:
    param1: This is the first param.
    param2: This is a second param.

Returns:
    This is a description of what is returned.

Raises:
    KeyError: Raises an exception.
"""
```


<a name="rest-docstrings"/>

##### reST

Nowadays, the probably more prevalent format is the reStructuredText (reST) format that is used by [Sphinx](http://sphinx-doc.org/) to generate documentation. 

Note: it is used by default in JetBrains PyCharm (type triple quotes after defining a method and hit enter). It is also used by default as output format in Pyment.

```python
"""
This is a reST style.

:param param1: this is a first param
:param param2: this is a second param
:returns: this is a description of what is returned
:raises keyError: raises an exception
"""
```


<a name="epytext-docstrings"/>

##### Epytext

Historically a javadoc like style was prevalent, so it was taken as a base for [Epydoc](http://epydoc.sourceforge.net/) (with the called Epytext format) to generate documentation.


```python
"""
This is a javadoc style.

@param param1: this is a first param
@param param2: this is a second param
@return: this is a description of what is returned
@raise keyError: raises an exception
"""
```


<a name="numpy-docstrings"/>

##### Numpydoc

Note that Numpy recommend to follow their own [numpydoc](https://numpydoc.readthedocs.io/en/latest/) based on Google format and usable by Sphinx.

```python
"""
My numpydoc description of a kind
of very exhautive numpydoc format docstring.

Parameters
----------
first : array_like
    the 1st param name `first`
second :
    the 2nd param
third : {'value', 'other'}, optional
    the 3rd param, by default 'value'

Returns
-------
string
    a value in a string

Raises
------
KeyError
    when a key error
OtherError
    when an other error
"""
```


<a name="converting-docstrings"/>

###### *Converting/Generating*
It is possible to use a tool like [Pyment](https://github.com/dadadel/pyment) to automatically generate docstrings to a Python project not yet documented, or to convert existing docstrings (can be mixing several formats) from a format to an other one.

Note: The examples are taken from the [Pyment documentation](https://github.com/dadadel/pyment/blob/master/README.rst)


--------------------------------------------------------------