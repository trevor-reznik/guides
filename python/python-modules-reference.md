


# Python Modules Reference

<a name="table-of-contents"/>

##### Table of Contents

  - [***Table of contents***](#table-of-contents)
- [**SKLEARN**](#sklearn)
  - [***Load datasets***](#load-datasets)
  - [***Loading with pandas***](#loading-with-pandas)
  - [***Training and testing***](#training-and-testing)
  - [***Prediction model training***](#prediction-model-training)
- [**MATPLOTLIB**](#matplotlib)
  - [***Two functions on same graph***](#two-functions-on-same-graph)
  - [***Decoration***](#decoration)
  - [***Bar chart***](#bar-chart)
  - [***Histogram***](#histogram)
  - [***Scatter plot***](#scatter-plot)
  - [***Pie-chart***](#pie-chart)
- [**REQUESTS**](#requests)
- [**COLORAMA**](#colorama)
- [**ARGPARSE**](#argparse)
- [**BEAUTIFUL SOUP**](#beautiful-soup)
- [**EMOJI**](#emoji)
- [**TERMCOLOR**](#termcolor)
  - [***Text colors***](#text-colors)
  - [***Text highlights***](#text-highlights)
  - [***Text attributes***](#text-attributes)
  - [***Terminal properties***](#terminal-properties)
- [**FIREBASE**](#firebase)
  - [***Writing with `push()`***](#writing-with-push())
  - [***Updating***](#updating)
  - [***Reading***](#reading)
  - [***Deleting***](#deleting)
- [**PYTHON-FIRE**](#python-fire)
  - [***Setup***](#setup)
  - [***Basic usage***](#basic-usage)
- [**CLI-UI**](#cli-ui)













<a name="sklearn"/>

## SKLEARN

References:

- [sciki-learn tutorial docs](https://scikit-learn.org/stable/tutorial/index.html)
- [API reference](https://scikit-learn.org/stable/modules/classes.html)
- [Examples](https://scikit-learn.org/stable/auto_examples/index.html)
- [Geeks for Geeks Example](https://www.geeksforgeeks.org/python-create-test-datasets-using-sklearn/)
- [Docs](https://scikit-learn.org/stable/index.html)
- [Video Tutorials](https://github.com/justmarkham/scikit-learn-videos)

<a name="loading-datasets"/>

###### Load Datasets

```python

# load the iris dataset as an example
from sklearn.datasets import load_iris
iris = load_iris()


# store the feature matrix (X) and response vector (y)
X = iris.data
y = iris.target


# store the feature and target names
feature_names = iris.feature_names
target_names = iris.target_names


# printing features and target names of our dataset
print("Feature names:", feature_names)
print("Target names:", target_names)


# X and y are numpy arrays
print("\nType of X is:", type(X))


# printing first 5 input rows
print("\nFirst 5 rows of X:\n", X[:5])
```

<a name="pandas-loading"/>

###### Loading with Pandas

```python
import pandas as pd

# reading csv file
data = pd.read_csv('weather.csv')

# shape of dataset
print("Shape:", data.shape)

# column names
print("\nFeatures:", data.columns)

# storing the feature matrix (X) and response vector (y)
X = data[data.columns[:-1]]
y = data[data.columns[-1]]

# printing first 5 rows of feature matrix
print("\nFeature matrix:\n", X.head())

# printing first 5 values of response vector
print("\nResponse vector:\n", y.head())
```

<a name="training-and-testing"/>

###### Training and Testing

```python
# load the iris dataset as an example
from sklearn.datasets import load_iris
iris = load_iris()

# store the feature matrix (X) and response vector (y)
X = iris.data
y = iris.target

# splitting X and y into training and testing sets
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=1)

# printing the shapes of the new X objects
print(X_train.shape)
print(X_test.shape)

# printing the shapes of the new y objects
print(y_train.shape)
print(y_test.shape)
```

The train_test_split function takes several arguments which are explained below:

- X, y: These are the feature matrix and response vector which need to be splitted.
- test_size: It is the ratio of test data to the given data. For example, setting test_size = 0.4 for 150 rows of X produces test data of 150 x 0.4 = 60 rows.
- random_state: If you use random_state = some_number, then you can guarantee that your split will be always the same. This is useful if you want reproducible results, for example in testing for consistency in the documentation (so that everybody can see the same numbers).

<a name="training-prediction-model"/>

###### Prediction Model Training

See: [More Examples](https://www.geeksforgeeks.org/learning-model-building-scikit-learn-python-machine-learning-library/)

```python
# load the iris dataset as an example
from sklearn.datasets import load_iris
iris = load_iris()

# store the feature matrix (X) and response vector (y)
X = iris.data
y = iris.target

# splitting X and y into training and testing sets
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=1)

# training the model on training set
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)

# making predictions on the testing set
y_pred = knn.predict(X_test)

# comparing actual response values (y_test) with predicted response values (y_pred)
from sklearn import metrics
print("kNN model accuracy:", metrics.accuracy_score(y_test, y_pred))

# making prediction for out of sample data
sample = [[3, 5, 4, 2], [2, 3, 5, 4]]
preds = knn.predict(sample)
pred_species = [iris.target_names[p] for p in preds]
print("Predictions:", pred_species)

# saving the model
from sklearn.externals import joblib
joblib.dump(knn, 'iris_knn.pkl')
```

<a name="matplotlib">

## MATPLOTLIB

<a name="plotting-graphs"/>

```python
# importing the required module
import matplotlib.pyplot as plt

# x axis values
x = [1,2,3]
# corresponding y axis values
y = [2,4,1]

# plotting the points
plt.plot(x, y)

# naming the x axis
plt.xlabel('x - axis')
# naming the y axis
plt.ylabel('y - axis')

# giving a title to my graph
plt.title('My first graph!')

# function to show the plot
plt.show()
```

<a name="two-functions-on-same-graph"/>

##### Two Functions on Same Graph

```python
import matplotlib.pyplot as plt

# line 1 points
x1 = [1,2,3]
y1 = [2,4,1]
# plotting the line 1 points
plt.plot(x1, y1, label = "line 1")

# line 2 points
x2 = [1,2,3]
y2 = [4,1,3]
# plotting the line 2 points
plt.plot(x2, y2, label = "line 2")

# naming the x axis
plt.xlabel('x - axis')
# naming the y axis
plt.ylabel('y - axis')
# giving a title to my graph
plt.title('Two lines on same graph!')

# show a legend on the plot
plt.legend()

# function to show the plot
plt.show()
```

<a name="decorating-output"/>

##### Decoration

```python

# plotting the points
plt.plot(x, y, color='green', linestyle='dashed', linewidth = 3,
         marker='o', markerfacecolor='blue', markersize=12)


# setting x and y axis range
plt.ylim(1,8)
plt.xlim(1,8)
```

<a name="bar-chart"/>

##### Bar Chart

Requests allows you to send HTTP/1.1 requests extremely easily. There’s no need to manually add query strings to your URLs.

```python
import matplotlib.pyplot as plt

# x-coordinates of left sides of bars
left = [1, 2, 3, 4, 5]

# heights of bars
height = [10, 24, 36, 40, 5]

# labels for bars
tick_label = ['one', 'two', 'three', 'four', 'five']

# plotting a bar chart
plt.bar(left, height, tick_label = tick_label,
        width = 0.8, color = ['red', 'green'])

# naming the x-axis
plt.xlabel('x - axis')Requests allows you to send HTTP/1.1 requests extremely easily. There’s no need to manually add query strings to your URLs.
# naming the y-axis
plt.ylabel('y - axis')

# plot title
plt.title('My bar chart!')

# function to show the plot
plt.show()
```

<a name="histogram"/>

##### Histogram

```python
import matplotlib.pyplot as plt

# frequencies
ages = [2,5,70,40,30,45,50,45,43,40,44,
        60,7,13,57,18,90,77,32,21,20,40]

# setting the ranges and no. of intervals
range = (0, 100)
bins = 10

# plotting a histogram
plt.hist(ages, bins, range, color = 'green',
        histtype = 'bar', rwidth = 0.8)

# x-axis label
plt.xlabel('age')
# frequency label
plt.ylabel('No. of people')
# plot title
plt.title('My histogram')

# function to show the plot
plt.show()
```

<a name="scatter-plot"/>

##### Scatter Plot

```python
import matplotlib.pyplot as plt

# x-axis values
x = [1,2,3,4,5,6,7,8,9,10]
# y-axis values
y = [2,4,5,7,6,8,9,11,12,12]

# plotting points as a scatter plot
plt.scatter(x, y, label= "stars", color= "green",
            marker= "*", s=30)

# x-axis label
plt.xlabel('x - axis')
# frequency label
plt.ylabel('y - axis')
# plot title
plt.title('My scatter plot!')
# showing legend
plt.legend()

# function to show the plot
plt.show()
```

<a name="pie-chart"/>

##### Pie-Chart

```python

import matplotlib.pyplot as plt
# defining labels
activities = ['eat', 'sleep', 'work', 'play']

# portion covered by each label
slices = [3, 7, 8, 6]

# color for each label
colors = ['r', 'y', 'g', 'b']

# plotting the pie chart
plt.pie(slices, labels = activities, colors=colors,
        startangle=90, shadow = True, explode = (0, 0, 0.1, 0),
        radius = 1.2, autopct = '%1.1f%%')


# plotting legend
plt.legend()

# showing the plot
plt.show()
```

<a name="requests"/>

## REQUESTS

```bash
pip install requests
```
Requests allows you to send HTTP/1.1 requests extremely easily. There’s no need to manually add query strings to your URLs.

```python
>>> import requests
>>> r = requests.get('https://api.github.com/user', auth=('user', 'pass'))
>>> r.status_code
200
>>> r.headers['content-type']
'application/json; charset=utf8'
>>> r.encoding
'utf-8'
>>> r.text
'{"type":"User"...'
>>> r.json()
{'disk_usage': 368627, 'private_gists': 484, ...}
```


<a name="colorama"/>

## COLORAMA

akes ANSI escape character sequences (for producing colored terminal text and cursor positioning) work under MS Windows.

```bash
pip install colorama
```

```python
# Applications should initialise Colorama using:
from colorama import init
init()

# Cross-platform printing of colored text can then be done using Colorama’s constant shorthand for ANSI escape sequences:
from colorama import Fore, Back, Style
print(Fore.RED + 'some red text')
print(Back.GREEN + 'and with a green background')
print(Style.DIM + 'and in dim text')
print(Style.RESET_ALL)
print('back to normal now')

# …or simply by manually printing ANSI sequences from your own code:
print('\033[31m' + 'some red text')
print('\033[39m') # and reset to default color
```

<a name="argparse"/>

## ARGPARSE

```python
def g_args():

    """""""""""""""
    |               # max space = 80, always one extra padding line, quotation quote # algorithm
    |
    |  add_argumnet()
    |
    |
    |___________________________________________________________________________________________________
    |  [-]----------------------------------------------------------------------------------------------|
    |  [1] name or flags :  Either a name or a list of option strings, e.g. foo or -f, --foo            |
    |  [+]______________________________________________________________________________________________|
    |  [2] action        :  Basic type of action to be taken when this argument is encountered at       |
    |  [+]                  the command line                                                            |
    |  [+]______________________________________________________________________________________________|
    |  [3] nargs         :  The number of command-line arguments that should be consumed                |
    |  [+]______________________________________________________________________________________________|
    |  [4] const         :  A constant value required by some action and nargs selections               |
    |  [+]______________________________________________________________________________________________|
    |  [5] default       :  The value produced if the argument is absent from the command line an       |
    |  [+]                  if it is absent from the namespace object                                   |
    |  [+]                  the argument is absentm the namespace object                                |
    |  [+]______________________________________________________________________________________________|
    |  [6] type          :  The type to which the command-line argument should be converted             |
    |  [+]______________________________________________________________________________________________|
    |  [7] choices       :  A container of the allowable values for the argument                        |
    |  [+]______________________________________________________________________________________________|
    |  [8] required      :  Whether or not the command-line option may be omitted (optionals only       |
    |  [+]______________________________________________________________________________________________|
    |  [9] help          :  A brief description of what the argument does                               |
    |  [+]______________________________________________________________________________________________|
    |  [a] metavar       :  A name for the argument in usage messages                                   |
    |  [+]______________________________________________________________________________________________|
    |  [b] dest          :  The name of the attribute to be added to the object returned by parse_args()|
    |  [+]______________________________________________________________________________________________|
    """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

    parser = argparse.ArgumentParser(prog="juice")

    # Positional
    parser.add_argument("path", nargs="?")
    # Adjustments
    parser.add_argument("--downscale", "-d", nargs="?", const=1, type=int, default=0, metavar=("increment"))
    parser.add_argument("--title","-t", nargs="?", metavar=("title/header string"), default="none")
    # Output
    parser.add_argument("--rewrite","-r", action="store_true", default=False)
    parser.add_argument("--no-backup", action="store_true", default=False)
    parser.add_argument("--output", "-o", nargs="?", metavar=("path/name"), type=str, default="__FORMATTER-OUTPUT.txt", const="__FORMATTER-OUTPUT.txt")
    parser.add_argument("--open", nargs="?", type=str, choices=["gedit","vim", "nano", "office","cat", "notepad", "notepad++", "vscode", "sublime", "geany", "emacs", "docviewer", "browser", "pdf", "meld", "diff", "$filetype$"], metavar=("program|filetype"), default="gedit", const="gedit")
    # Figlet Choices
    parser.add_argument("-fonts","-f", nargs=4, default=["auto", "auto", "auto", "auto"], metavar=("[header]", "[section-titles]", "[special]", "[table-titles]"))
    parser.add_argument("--title-font", nargs="?", type=str, default="auto", const="auto", metavar=("random|none|fontname"))
    parser.add_argument("--section-font", nargs="?", type=str, default="auto", const="auto", metavar=("random|none|fontname"))
    parser.add_argument("--special-font", nargs="?", type=str, default="auto", const="auto", metavar=("random|none|fontname"))
    parser.add_argument("--table-title-font", nargs="?", type=str, default="auto", const="auto", metavar=("random|none|fontname"))
    # Additional Help Dialogs
    parser.add_argument("--show-fonts", action="store_true", default=False)

    return parser.parse_args()


def main():
    options = vars(g_args())
```

<a name="beautiful-soup"/>

## BEAUTIFUL SOUP

```bash
pip install beautifulsoup4
```

Beautiful Soup is a library that makes it easy to scrape information from web pages. It sits atop an HTML or XML parser, providing Pythonic idioms for iterating, searching, and modifying the parse tree.

[docs](http://www.crummy.com/software/BeautifulSoup/bs4/doc/)

```python
>>> from bs4 import BeautifulSoup
>>> soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
>>> print(soup.prettify())
<html>
 <body>
  <p>
   Some
   <b>
    bad
    <i>
     HTML
    </i>
   </b>
  </p>
 </body>
</html>
>>> soup.find(text="bad")
'bad'
>>> soup.i
<i>HTML</i>
>>> soup = BeautifulSoup("<tag1>Some<tag2/>bad<tag3>XML", "xml")
>>> print(soup.prettify())
<?xml version="1.0" encoding="utf-8"?>
<tag1>
 Some
 <tag2/>
 bad
 <tag3>
  XML
 </tag3>
</tag1>
```

<a name="emoji"/>

## Emoji

```bash
pip install emoji
```

```python
>> import emoji
>> print(emoji.emojize('Python is :thumbs_up:'))
Python is �
>> print(emoji.emojize('Python is :thumbsup:', use_aliases=True))
Python is �
>> print(emoji.demojize('Python is �'))
Python is :thumbs_up:
>>> print(emoji.emojize("Python is fun :red_heart:"))
Python is fun ❤
>>> print(emoji.emojize("Python is fun :red_heart:",variant="emoji_type"))
Python is fun ❤️ #red heart, not black heart
```


The entire set of Emoji codes as defined by the [unicode consortium](http://www.unicode.org/Public/emoji/1.0/full-emoji-list.html) is supported in addition to a bunch of [aliases](http://www.emoji-cheat-sheet.com/). By default, only the official list is enabled but doing `emoji.emojize(use_aliases=True)` enables both the full list and aliases



<a name="termcolor"/>

## Termcolor

```bash
pip install termcolor
```

```python
import sys
from termcolor import colored, cprint

text = colored('Hello, World!', 'red', attrs=['reverse', 'blink'])
print(text)
cprint('Hello, World!', 'green', 'on_red')

print_red_on_cyan = lambda x: cprint(x, 'red', 'on_cyan')
print_red_on_cyan('Hello, World!')
print_red_on_cyan('Hello, Universe!')

for i in range(10):
    cprint(i, 'magenta', end=' ')

cprint("Attention!", 'red', attrs=['bold'], file=sys.stderr)
```

<a name="text-colors"/>

###### Text Colors

- grey
- red
- green
- yellow
- blue
- magenta
- cyan
- white

<a name="text-highlights"/>

###### Text Highlights

- on_grey
- on_red
- on_green
- on_yellow
- on_blue
- on_magenta
- on_cyan
- on_white

<a name="text-attributes"/>

###### Text Attributes

- bold
- dark
- underline
- blink
- reverse
- concealed



<a name="terminal-properties"/>

###### Terminal Properties

<table>
<colgroup>
<col>
<col>
<col>
<col>
<col>
<col>
<col>
</colgroup>
<tbody>
<tr><td>Terminal</td>
<td>bold</td>
<td>dark</td>
<td>underline</td>
<td>blink</td>
<td>reverse</td>
<td>concealed</td>
</tr>
<tr><td>xterm</td>
<td>yes</td>
<td>no</td>
<td>yes</td>
<td>bold</td>
<td>yes</td>
<td>yes</td>
</tr>
<tr><td>linux</td>
<td>yes</td>
<td>yes</td>
<td>bold</td>
<td>yes</td>
<td>yes</td>
<td>no</td>
</tr>
<tr><td>rxvt</td>
<td>yes</td>
<td>no</td>
<td>yes</td>
<td>bold/black</td>
<td>yes</td>
<td>no</td>
</tr>
<tr><td>dtterm</td>
<td>yes</td>
<td>yes</td>
<td>yes</td>
<td>reverse</td>
<td>yes</td>
<td>yes</td>
</tr>
<tr><td>teraterm</td>
<td>reverse</td>
<td>no</td>
<td>yes</td>
<td>rev/red</td>
<td>yes</td>
<td>no</td>
</tr>
<tr><td>aixterm</td>
<td>normal</td>
<td>no</td>
<td>yes</td>
<td>no</td>
<td>yes</td>
<td>yes</td>
</tr>
<tr><td>PuTTY</td>
<td>color</td>
<td>no</td>
<td>yes</td>
<td>no</td>
<td>yes</td>
<td>no</td>
</tr>
<tr><td>Windows</td>
<td>no</td>
<td>no</td>
<td>no</td>
<td>no</td>
<td>yes</td>
<td>no</td>
</tr>
<tr><td>Cygwin SSH</td>
<td>yes</td>
<td>no</td>
<td>color</td>
<td>color</td>
<td>color</td>
<td>yes</td>
</tr>
<tr><td>Mac Terminal</td>
<td>yes</td>
<td>no</td>
<td>yes</td>
<td>yes</td>
<td>yes</td>
<td>yes</td>
</tr>
</tbody>
</table>



<a name="firebase"/>

## FIREBASE

[How to Get Started with Firebase Using Python](https://www.freecodecamp.org/news/how-to-get-started-with-firebase-using-python/)

```bash
pip install firebase_admin
```

```python
import firebase_admin

cred_obj = firebase_admin.credentials.Certificate('....path to file')
default_app = firebase_admin.initialize_app(cred_object, {
	'databaseURL':databaseURL
	})


from firebase_admin import db

ref = db.reference("/")


{
	"Book1":
	{
		"Title": "The Fellowship of the Ring",
		"Author": "J.R.R. Tolkien",
		"Genre": "Epic fantasy",
		"Price": 100
	},
	"Book2":
	{
		"Title": "The Two Towers",
		"Author": "J.R.R. Tolkien",
		"Genre": "Epic fantasy",
		"Price": 100
	},
	"Book3":
	{
		"Title": "The Return of the King",
		"Author": "J.R.R. Tolkien",
		"Genre": "Epic fantasy",
		"Price": 100
	},
	"Book4":
	{
		"Title": "Brida",
		"Author": "Paulo Coelho",
		"Genre": "Fiction",
		"Price": 100
	}
}
```

```python
import json
with open("book_info.json", "r") as f:
	file_contents = json.load(f)
ref.set(file_contents)
```

<a name="writing-with-push"/>

###### Writing with `push()`

```python
ref = db.reference("/")
ref.set({
	"Books":
	{
		"Best_Sellers": -1
	}
})

ref = db.reference("/Books/Best_Sellers")
import json
with open("book_info.json", "r") as f:
	file_contents = json.load(f)

for key, value in file_contents.items():
	ref.push().set(value)
```

<a name="updating"/>

###### Updating

```python
ref = db.reference("/Books/Best_Sellers/")
best_sellers = ref.get()
print(best_sellers)
for key, value in best_sellers.items():
	if(value["Author"] == "J.R.R. Tolkien"):
		value["Price"] = 90
		ref.child(key).update({"Price":80})
```

<a name="reading"/>

###### Reading

```python
ref = db.reference("/Books/Best_Sellers/")
print(ref.order_by_child("Price").get())
```

```python
#T he return value of the method is an OrderedDict. To order by key, use order_by_key(). To get the book with maximum price, we use the limit_to_last() method as follows:
ref.order_by_child("Price").limit_to_last(1).get()

# Alternatively, to get the least priced book, we write this:
ref.order_by_child("Price").limit_to_first(1).get()

# To get books that are exactly priced at 80 units, we use this:
ref.order_by_child("Price").equal_to(80).get()
```

<a name="deleting"/>

###### Deleting

```python
ref = db.reference("/Books/Best_Sellers")

for key, value in best_sellers.items():
	if(value["Author"] == "J.R.R. Tolkien"):
		ref.child(key).set({})
```

<a name="python-fire"/>

## PYTHON-FIRE

- [Repo](https://github.com/google/python-fire)
- [Summary](https://github.com/google/python-fire/blob/master/docs/benefits.md#simple-cli)
- [Explore existing code; turn other people's code into a CLI](https://github.com/google/python-fire/blob/master/docs/benefits.md#exploring)
- [setting up the REPL with the modules and variables you'll need already imported and created](https://github.com/google/python-fire/blob/master/docs/benefits.md#repl)

<a name="setup"/>

###### Setup

```bash
pip install fire
```

```python
import fire
```

<a name="basic-usage"/>

###### Basic Usage

You can call Fire on any Python object:

functions, classes, modules, objects, dictionaries, lists, tuples, etc. They all work!

```python
import fire

def hello(name="World"):
  return "Hello %s!" % name

if __name__ == '__main__':
  fire.Fire(hello)
```

Then, from the command line, you can run:

```python
python hello.py  # Hello World!
python hello.py --name=David  # Hello David!
python hello.py --help  # Shows usage information.
```

Here's an example of calling Fire on a class.

```python
import fire

class Calculator(object):
  """A simple calculator class."""

  def double(self, number):
    return 2 * number

if __name__ == '__main__':
  fire.Fire(Calculator)
```

Then, from the command line, you can run:

```python
python calculator.py double 10  # 20
python calculator.py double --number=15  # 30
```

To learn how Fire behaves on functions, objects, dicts, lists, etc, and to learn about Fire's other features, see the Using a Fire CLI page.

<a name="python-cli-ui"/>

## CLI-UI

```bash
pip install python-cli-ui
```

```python
import ui

# coloring:
ui.info("This is", ui.red, "red",
        ui.reset, "and this is", ui.bold, "bold")

# enumerating:
list_of_things = ["foo", "bar", "baz"]
for i, thing in enumerate(list_of_things):
    ui.info_count(i, len(list_of_things), thing)

# progress indication:
ui.info_progress("Done",  5, 20)
ui.info_progress("Done", 10, 20)
ui.info_progress("Done", 20, 20)

# reading user input:
with_sugar = ui.ask_yes_no("With sugar?", default=False)

fruits = ["apple", "orange", "banana"]
selected_fruit = ui.ask_choice("Choose a fruit", fruits)
```




-----------------------------

<div align="center" style="font-size: 11px; margin: 0; opacity:.6"><a href="#table-of-contents">Top (目次)</a></div>
