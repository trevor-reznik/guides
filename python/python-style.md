<a name="table-of-contents"/>

# Python Style Guidelines

*Things I keep forgetting*

- [***Docstrings***](#docstrings)
  - [**Google**](#google-docstrings)
  - [**reSt**](#rest-docstrings)
  - [**Epytext**](#epytext-docstrings)
  - [**Numpydoc**](#numpy-docstrings)
  - [**Converting/Generating**](#converting-docstrings)
- [***Indents***](#indents)
- [Whitespace](#whitespace)
[**Slicing**](#slicing)
[trailing commas](#trailing-commas)
[comments](#comments)
[naming](#naming)
[***return***](#return)
[***comparisons***](#comparisons)
[***type-checkers***](#type-checkers)
[***long-lines***](#long-lines)
[***conditional-indent***](#conditional-indent)
[***blank-lines***](#blank-lines)
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

###### More

- [Special Cases](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html)
- [More Examples](https://www.sphinx-doc.org/en/master/usage/extensions/example_google.html#example-google)

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

<a name="slicing"/>

###### Whitespace in slices

In a slice the colon acts like a binary operator, and should have equal amounts on either side (treating it as the operator with the lowest priority)

```python
# Good:
[ : an / extended % equation]
[:avariable]

# Bad:
ham[ : upper]
```

In an extended slice, both colons must have the same amount of spacing applied. Exception: when a slice parameter is omitted, the space is omitted:

```python
# Correct:
ham[lower+offset : upper+offset]
ham[: upper_fn(x) : step_fn(x)], ham[:: step_fn(x)]
ham[lower + offset : upper + offset]

# Wrong:
ham[lower + offset:upper + offset]
ham[1: 9], ham[1 :9], ham[1:9 :3]
ham[lower : : upper]
```

<a name="whitepspace"/>


###### Whitespace to indicate priority/order

```python
x = x*2 - 1
hypot2 = x*x + y*y
c = (a+b) * (a-b)
```

- Avoid trailing whitespace anywhere. Because it's usually invisible, it can be confusing: e.g. a backslash followed by a space and a newline does not count as a line continuation marker. Some editors don't preserve it and many projects (like CPython itself) have pre-commit hooks that reject it.
- Always surround these binary operators with a single space on either side: assignment (=), augmented assignment (+=, -= etc.), comparisons (==, <, >, !=, <>, <=, >=, in, not in, is, is not), Booleans (and, or, not).
- Always have the same amount of whitespace on both sides of a binary operator:


```python
# Wrong:
spam( ham[ 1 ], { eggs: 2 } )
bar = (0, )
if x == 4 : print x , y ; x , y = y , x
```

When combining an argument annotation with a default value, however, do use spaces around the = sign:

```python
# Correct:
def munge(sep: AnyStr = None): ...
def munge(input: AnyStr, sep: AnyStr = None, limit=1000): ...
# Wrong:
def munge(input: AnyStr=None): ...
def munge(input: AnyStr, limit = 1000): ...
```


<a name="indents"/>

## Indentation / Line-Breaks


###### Hanging Indents

 When using a hanging indent the following should be considered; there should be no arguments on the first line and further indentation should be used to clearly distinguish itself as a continuation line:


 ```python
 # Correct:

# Aligned with opening delimiter.
foo = long_function_name(var_one, var_two,
                         var_three, var_four)

# Add 4 spaces (an extra level of indentation) to distinguish arguments from the rest.
def long_function_name(
        var_one, var_two, var_three,
        var_four):
    print(var_one)

# Hanging indents should add a level.
foo = long_function_name(
    var_one, var_two,
    var_three, var_four)
# Wrong:

# Arguments on first line forbidden when not using vertical alignment.
foo = long_function_name(var_one, var_two,
    var_three, var_four)

# Further indentation required as indentation is not distinguishable.
def long_function_name(
    var_one, var_two, var_three,
    var_four):
    print(var_one)

```

<a name="conditional-indent"/>

###### Conditionals - Hanging Indetns
When the conditional part of an if-statement is long enough to require that it be written across multiple lines, it's worth noting that the combination of a two character keyword (i.e. if), plus a single space, plus an opening parenthesis creates a natural 4-space indent for the subsequent lines of the multiline conditional. This can produce a visual conflict with the indented suite of code nested inside the if-statement, which would also naturally be indented to 4 spaces. This PEP takes no explicit position on how (or whether) to further visually distinguish such conditional lines from the nested suite inside the if-statement. Acceptable options in this situation include, but are not limited to:

```python
# No extra indentation.
if (this_is_one_thing and
    that_is_another_thing):
    do_something()

# Add a comment, which will provide some distinction in editors
# supporting syntax highlighting.
if (this_is_one_thing and
    that_is_another_thing):
    # Since both conditions are true, we can frobnicate.
    do_something()

# Add some extra indentation on the conditional continuation line.
if (this_is_one_thing
        and that_is_another_thing):
    do_something()
(Also see the discussion of whether to break before or after binary operators below.)
```

The closing brace/bracket/parenthesis on multiline constructs may either line up under the first non-whitespace character of the last line of list, as in:

```python
my_list = [
    1, 2, 3,
    4, 5, 6,
    ]
result = some_function_that_takes_arguments(
    'a', 'b', 'c',
    'd', 'e', 'f',
    )
```

or it may be lined up under the first character of the line that starts the multiline construct, as in:

```python
my_list = [
    1, 2, 3,
    4, 5, 6,
]
result = some_function_that_takes_arguments(
    'a', 'b', 'c',
    'd', 'e', 'f',
)
```

<a name="long-lines"/>

###### Long Lines

The preferred way of wrapping long lines is by using Python's implied line continuation inside parentheses, brackets and braces. Long lines can be broken over multiple lines by wrapping expressions in parentheses. These should be used in preference to using a backslash for line continuation.

Backslashes may still be appropriate at times. For example, long, multiple with-statements cannot use implicit continuation, so backslashes are acceptable:

```python
with open('/path/to/some/file/you/want/to/read') as file_1, \
     open('/path/to/some/file/being/written', 'w') as file_2:
    file_2.write(file_1.read())
```

<a name="blank-lines"/>

###### Blank Lines
Surround top-level function and class definitions with two blank lines.

Method definitions inside a class are surrounded by a single blank line.

Extra blank lines may be used (sparingly) to separate groups of related functions. Blank lines may be omitted between a bunch of related one-liners (e.g. a set of dummy implementations).

Use blank lines in functions, sparingly, to indicate logical sections.

Python accepts the control-L (i.e. ^L) form feed character as whitespace; Many tools treat these characters as page separators, so you may use them to separate pages of related sections of your file. Note, some editors and web-based code viewers may not recognize control-L as a form feed and will show another glyph in its place.


<a name="trailing-commas"/>

When trailing commas are redundant, they are often helpful when a version control system is used, when a list of values, arguments or imported items is expected to be extended over time. The pattern is to put each value (etc.) on a line by itself, always adding a trailing comma, and add the close parenthesis/bracket/brace on the next line. However it does not make sense to have a trailing comma on the same line as the closing delimiter (except in the above case of singleton tuples):





<a name="comments"/>

## Comments

- Complete sentences
- First word capitalized
- Block comments generally consist of one or more paragraphs built out of complete sentences, with each sentence ending in a period.
- You should use two spaces after a sentence-ending period in multi- sentence comments, except after the final sentence.
- Paragraphs inside a block comment are separated by a line containing a single #.
- An inline comment is a comment on the same line as a statement. Inline comments should be separated by at least two spaces from the statement. They should start with a # and a single space.
- Conventions for writing good documentation strings (a.k.a. "docstrings") are immortalized in [PEP 257](https://www.python.org/dev/peps/pep-0257).

<a name="naming"/>

## Naming

Names that are visible to the user as public parts of the API should follow conventions that reflect usage rather than implementation.


###### Descriptive: Naming Styles

There are a lot of different naming styles. It helps to be able to recognize what naming style is being used, independently from what they are used for.


- When using acronyms in CapWords, capitalize all the letters of the acronym. Thus HTTPServerError is better than HttpServerError.
- In some fonts, these characters are indistinguishable from the numerals one and zero. When tempted to use 'l', use 'L' instead.


###### Type Variable Names
Names of type variables introduced in PEP 484 should normally use CapWords preferring short names: T, AnyStr, Num. It is recommended to add suffixes _co or _contra to the variables used to declare covariant or contravariant behavior correspondingly:

```python
from typing import TypeVar

VT_co = TypeVar('VT_co', covariant=True)
KT_contra = TypeVar('KT_contra', contravariant=True)
```

###### Exception Names

Because exceptions should be classes, the class naming convention applies here. However, you should use the suffix "Error" on your exception names (if the exception actually is an error).

Derive exceptions from Exception rather than BaseException. Direct inheritance from BaseException is reserved for exceptions where catching them is almost always the wrong thing to do.

Design exception hierarchies based on the distinctions that code catching the exceptions is likely to need, rather than the locations where the exceptions are raised. Aim to answer the question "What went wrong?" programmatically, rather than only stating that "A problem occurred" (see PEP 3151 for an example of this lesson being learned for the builtin exception hierarchy)

Class naming conventions apply here, although you should add the suffix "Error" to your exception classes if the exception is an error. Non-error exceptions that are used for non-local flow control or other forms of signaling need no special suffix.

Use exception chaining appropriately. In Python 3, "raise X from Y" should be used to indicate explicit replacement without losing the original traceback.

When deliberately replacing an inner exception (using "raise X" in Python 2 or "raise X from None" in Python 3.3+), ensure that relevant details are transferred to the new exception (such as preserving the attribute name when converting KeyError to AttributeError, or embedding the text of the original exception in the new exception message).

When raising an exception in Python 2, use raise ValueError('message') instead of the older form raise ValueError, 'message'.

The latter form is not legal Python 3 syntax.

The paren-using form also means that when the exception arguments are long or include string formatting, you don't need to use line continuation characters thanks to the containing parentheses.

When catching exceptions, mention specific exceptions whenever possible instead of using a bare except: clause:

```python
try:
    import platform_specific_module
except ImportError:
    platform_specific_module = None
A bare except: clause will catch SystemExit and KeyboardInterrupt exceptions, making it harder to interrupt a program with Control-C, and can disguise other problems. If you want to catch all exceptions that signal program errors, use except Exception: (bare except is equivalent to except BaseException:).
```

A good rule of thumb is to limit use of bare 'except' clauses to two cases:

If the exception handler will be printing out or logging the traceback; at least the user will be aware that an error has occurred.
If the code needs to do some cleanup work, but then lets the exception propagate upwards with raise. try...finally can be a better way to handle this case.
When binding caught exceptions to a name, prefer the explicit name binding syntax added in Python 2.6:

```python
try:
    process_data()
except Exception as exc:
    raise DataProcessingFailedError(str(exc))
This is the only syntax supported in Python 3, and avoids the ambiguity problems associated with the older comma-based syntax.
```

When catching operating system errors, prefer the explicit exception hierarchy introduced in Python 3.3 over introspection of errno values.

Additionally, for all try/except clauses, limit the try clause to the absolute minimum amount of code necessary. Again, this avoids masking bugs:

# Correct:
try:
    value = collection[key]
except KeyError:
    return key_not_found(key)
else:
    return handle_value(value)
# Wrong:
try:
    # Too broad!
    return handle_value(collection[key])
except KeyError:
    # Will also catch KeyError raised by handle_value()
    return key_not_found(key)
When a resource is local to a particular section of code, use a with statement to ensure it is cleaned up promptly and reliably after use. A try/finally statement is also acceptable.

###### Function and Method Arguments

Always use self for the first argument to instance methods.

Always use cls for the first argument to class methods.

If a function argument's name clashes with a reserved keyword, it is generally better to append a single trailing underscore rather than use an abbreviation or spelling corruption. Thus class_ is better than clss. (Perhaps better is to avoid such clashes by using a synonym.)

###### Method Names and Instance Variables
Use the function naming rules: lowercase with words separated by underscores as necessary to improve readability.


Use one leading underscore only for non-public methods and instance variables.

To avoid name clashes with subclasses, use two leading underscores to invoke Python's name mangling rules.

Python mangles these names with the class name: if class Foo has an attribute named __a, it cannot be accessed by Foo.__a. (An insistent user could still gain access by calling Foo._Foo__a.) Generally, double leading underscores should be used only to avoid name conflicts with attributes in classes designed to be subclassed.

Note: there is some controversy about the use of __names (see below).

Always use a def statement instead of an assignment statement that binds a lambda expression directly to an identifier:


###### Function Names

```python
# Correct:
def f(x): return 2*x

# Wrong:
f = lambda x: 2*x
The first form means that the name of the resulting function object is specifically 'f' instead of the generic '<lambda>'. This is more useful for tracebacks and string representations in general. The use of the assignment statement eliminates the sole benefit a lambda expression can offer over an explicit def statement (i.e. that it can be embedded inside a larger expression)
```


[Designing for Inheritance](https://www.python.org/dev/peps/pep-0008/#id49)


<a name="return"/>

## Return Statements


Be consistent in return statements. Either all return statements in a function should return an expression, or none of them should. If any return statement returns an expression, any return statements where no value is returned should explicitly state this as return None, and an explicit return statement should be present at the end of the function (if reachable):

Use ''.startswith() and ''.endswith() instead of string slicing to check for prefixes or suffixes.

startswith() and endswith() are cleaner and less error prone:


<a name="comparisons"/>

Object type comparisons should always use isinstance() instead of comparing types directly:

```python
# Correct:
if isinstance(obj, int):
# Wrong:
if type(obj) is type(1):
```

When checking if an object is a string, keep in mind that it might be a unicode string too! In Python 2, str and unicode have a common base class, basestring, so you can do:

```python
if isinstance(obj, basestring):
```


For sequences, (strings, lists, tuples), use the fact that empty sequences are false:

```python
# Correct:
if not seq:
if seq:
# Wrong:
if len(seq):
if not len(seq):
```

<a name="type-checkers"/>

## Type Checkers

[Function and Variable Annotations in PEP8](https://www.python.org/dev/peps/pep-0008/#id52)


Users who don't want to use type checkers are free to ignore them. However, it is expected that users of third party library packages may want to run type checkers over those packages. For this purpose PEP 484 recommends the use of stub files: .pyi files that are read by the type checker in preference of the corresponding .py files. Stub files can be distributed with a library, or separately (with the library author's permission) through the typeshed repo [5].z