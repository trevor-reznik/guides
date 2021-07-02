
<a name="table-of-contents"/>

![Pictures](banners/bash-shell-usage.png)

###### Header

```bash
#!/bin/bash
```

###### Permission 

```bash
chmod +x ~/myscript.sh
```

----


# Functions

```bash
function_name () {
  commands
}
```

----

# Variables

The `$#` variable holds the number of positional parameters/arguments passed to the function.


The `$0` variable is reserved for the function’s name.


The `$*` and `$@` variables hold all positional parameters/arguments passed to the function.


When double-quoted, `"$*"` expands to a single string separated by space (the first character of IFS) - `"$1 $2 $n"`.


When double-quoted, `"$@"` expands to separate strings - `"$1" "$2" "$n"`


When not double-quoted, `$*` and `$@` are the same.

---


### Variable Concat

```bash
foo="Hello"
foo="${foo} World"
echo "${foo}"
> Hello World
```

In general to concatenate two variables you can just write them one after another:

```bash
a='Hello'
b='World'
c="${a} ${b}"
echo "${c}"
> Hello World
```