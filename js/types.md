

# Types


<a name="table-of-contents"/>

###### Table of Contents

- [**ASYNC**](#async)
- [**CALLBACK FUNCTIONS**](#callback-functions)
  - [***Example***](#example)
- [**HIGHER ORDER FUNCTIONS**](#higher-order-functions)
- [**LAMBDA FUNCTIONS**](#lambda-functions)
  - [***`this`***](#this)
  - [***Differences & limitations:***](#differences-&-limitations)
  - [***Example breakdown***](#example-breakdown)
- [**VARIABLE TYPES**](#variable-types)
- [**DOM OVERVIEW**](#dom-overview)
  - [***Html tag components***](#html-tag-components)



<a name="reminders"/>

## Reminders

#### `forEach`

```javascript
// Arrow function
forEach((element) => { ... } )
forEach((element, index) => { ... } )
forEach((element, index, array) => { ... } )

// Callback function
forEach(callbackFn)
forEach(callbackFn, thisArg)

// Inline callback function
forEach(function callbackFn(element) { ... })
forEach(function callbackFn(element, index) { ... })
forEach(function callbackFn(element, index, array){ ... })
forEach(function callbackFn(element, index, array) { ... }, thisArg)
```

<a name="async"/>

## Async



```javascript
function resolveAfter2Seconds(x) {
  return new Promise(resolve => {
    setTimeout(() => {
      resolve(x);
    }, 2000);
  });
}

async function f1() {
  var x = await resolveAfter2Seconds(10);
  console.log(x); // 10
}

f1();
```


<a name="callback-functions"/>

## Callback Functions


```javascript
function greeting(name) {
  alert('Hello ' + name);
}

function processUserInput(callback) {
  var name = prompt('Please enter your name.');
  callback(name);
}

processUserInput(greeting);
```

The above example is a synchronous callback, as it is executed immediately.

Note, however, that callbacks are often used to continue code execution after an `asynchronous` operation has completed — these are called asynchronous callbacks. A good example is the callback functions executed inside a `.then()` block chained onto the end of a promise after that promise fulfills or rejects. This structure is used in many modern web APIs, such as `fetch()`


<a name="example"/>

#### Example

![dom](info-pics/fs-read-callback.png)

![dom](info-pics/fs-read-callback2.png)


<a name="higher-order-functions"/>

## Higher Order Functions

E.g., `Map`, `filter`, and `reduce`


```javascript
isEven = (num) => num % 2 === 0;
result = [1, 2, 3, 4].filter(isEven);

console.log(result); // [2, 4]
```

```javascript
totalAge = users.reduce((total, user) => user.age + total, 0);

console.log(totalAge);
// 75
```

With functions in JavaScript, you can

- Store them as variables
- Use them in arrays
- Assign them as object properties (methods)
- Pass them as arguments
- Return them from other functions


![dom](info-pics/higher-order-js-func.png)

![dom](info-pics/higher-order-js-func02.png)

<a name="lambda-functions"/>

## Lambda Functions


An arrow function expression is a compact alternative to a traditional function expression, but is limited and can't be used in all situations.


![lambda function](info-pics/js-lambda-1.png)

![lambda function](info-pics/js-lambda-2.png)

<a name="this"/>

#### `this`

![lambda function](info-pics/js-lambda-3.png)

<a name="differences-&-limitations:"/>

#### Differences & Limitations

- Does not have its own bindings to `this` or `super`, and should not be used as methods.
- Does not have `arguments`, or `new.target` keywords.
- Not suitable for `call`, `apply` and `bind` methods, which generally rely on establishing a scope.
- Can not be used as constructors.
- Can not use `yield`, within its body.

<a name="example-breakdown"/>

#### Example Breakdown

```javascript
// Traditional Function
function (a){
  return a + 100;
}

// Arrow Function Break Down

// 1. Remove the word "function" and place arrow between the argument and opening body bracket
(a) => {
  return a + 100;
}

// 2. Remove the body brackets and word "return" -- the return is implied.
(a) => a + 100;

// 3. Remove the argument parentheses
a => a + 100;
```

<a name="variable-types"/>

## Variable Types

![varaible types](info-pics/js-variables01.png)


<a name="dom-overview"/>

## DOM Overview

![dom](info-pics/dom01.png)

![dom](info-pics/dom02.png)

<a name="html-tag-components"/>

##### HTML Tag Components

![tag components](info-pics/html-tag.png)




-----------------------------

<div align="center" style="font-size: 11px; margin: 0; opacity:.6"><a href="#table-of-contents">Top (目次)</a></div>

