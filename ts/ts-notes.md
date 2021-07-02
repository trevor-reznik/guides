

# Typescript

<a name="table-of-contents"/>

- [**SUMMARY**](#summary)
- [**SETUP**](#setup)
  - [***Declaration files***](#declaration-files)
- [**TYPE ASSERTIONS**](#type-assertions)
- [**SPECIAL TYPES**](#special-types)
  - [***Array***](#array)
  - [***Object***](#object)
  - [***Function***](#function)
  - [***Unknown***](#unknown)
  - [***Never***](#never)
  - [***Any***](#any)
  - [***Void***](#void)
- [**VARIABLE TYPES**](#variable-types)
- [**FUNCTION EXPRESSION TYPES**](#function-expression-types)
- [**FUNCTIONS WITH PROPERTIES TYPES**](#functions-with-properties-types)
- [**CONSTRUCTOR TYPES**](#constructor-types)
- [**PARAMTER TYPES**](#paramter-types)
  - [***Constraints***](#constraints)
  - [***Parameter destructuring***](#parameter-destructuring)
- [**RETURN TYPES**](#return-types)
- [**REST PARAMTERS AND ARGUMENTS**](#rest-paramters-and-arguments)
  - [***Rest paramters***](#rest-paramters)
  - [***Rest arguments***](#rest-arguments)
- [**GENERIC FUNCTION PARAMETER TYPES**](#generic-function-parameter-types)
  - [***Push type parameters down***](#push-type-parameters-down)
  - [***Using fewer type parameters***](#using-fewer-type-parameters)
  - [***Type parameters should appear twice***](#type-parameters-should-appear-twice)
- [**OBJECT TYPES**](#object-types)
  - [**TYPE ALIASES AND INTERFACES**](#type-aliases-and-interfaces)
    - [***Aliases***](#aliases)
    - [***Interfaces***](#interfaces)
    - [***Differences***](#differences)
    - [***Extending aliases***](#extending-aliases)
    - [***Extending interfaces***](#extending-interfaces)
  - [**PROPRETY MODIFIERS**](#proprety-modifiers)
    - [***Optional properties***](#optional-properties)
      - [Defaults](#defaults)
    - [***Readonly***](#readonly)
    - [***Index signatures***](#index-signatures)
    - [***Intersection types***](#intersection-types)
    - [***Union types***](#union-types)
    - [***Literal types***](#literal-types)
- [**TUPLE TYPES**](#tuple-types)
  - [***Optional tuple properties***](#optional-tuple-properties)
  - [***Rest tuple properties***](#rest-tuple-properties)
- [**ENUMS**](#enums)
- [**TYPE MANIPULATION**](#type-manipulation)
- [**NARROWING**](#narrowing)
  - [***Equality narrowing***](#equality-narrowing)
- [**GENERIC TYPES**](#generic-types)
  - [***Generic type aliases***](#generic-type-aliases)
- [**CLASSES**](#classes)
- [**MODULES**](#modules)
- [**REFERENCES**](#references)



<a name="summary"/>

## Summary

[TypeScript Deep Dive](https://basarat.gitbook.io/typescript/) | [The TypeScript Handbook](https://www.typescriptlang.org/docs/handbook/intro.html)

Static types systems describe the shapes and behaviors of what our values will be when we run our programs.  A type-checker like TypeScript uses that information and tells us when things might be going off the rails.

The type-checker has information to check things like whether we’re accessing the right properties on variables and other properties. Once it has that information, it can also start suggesting which properties you might want to use.

That means TypeScript can be leveraged for editing code too, and the core type-checker can provide error messages and code completion as you type in the editor. That’s part of what people often refer to when they talk about tooling in TypeScript.

TypeScript takes tooling seriously, and that goes beyond completions and errors as you type. An editor that supports TypeScript can deliver “quick fixes” to automatically fix errors, refactorings to easily re-organize code, and useful navigation features for jumping to definitions of a variable, or finding all references to a given variable. 



<a name="setup"/>

## Setup


1. install

```bash
npm i --save-dev typescript @types/node
```

2. config 

```bash
vim tsconfig.json
```

3. compile

```bash
tsc --noEmitOnError hello.ts
tsc --target es2015 hello.ts
```

4. run with `test` scripts

```bash
tsc --target es2015 hello.ts
```
<a name="declaration-files"/>

#### Declaration Files

[With Hyperlinks](https://www.typescriptlang.org/docs/handbook/declaration-files/introduction.html)

The Declaration Files section is designed to teach you how to write a high-quality TypeScript Declaration File. We need to assume basic familiarity with the TypeScript language in order to get started.

If you haven’t already, you should read the TypeScript Handbook to familiarize yourself with basic concepts, especially types and modules.

The most common case for learning how .d.ts files work is that you’re typing an npm package with no types. In that case, you can jump straight to Modules .d.ts.

The Declaration Files section is broken down into the following sections.

Declaration Reference
We are often faced with writing a declaration file when we only have examples of the underlying library to guide us. The Declaration Reference section shows many common API patterns and how to write declarations for each of them. This guide is aimed at the TypeScript novice who may not yet be familiar with every language construct in TypeScript.

Library Structures
The Library Structures guide helps you understand common library formats and how to write a proper declaration file for each format. If you’re editing an existing file, you probably don’t need to read this section. Authors of new declaration files are strongly encouraged to read this section to properly understand how the format of the library influences the writing of the declaration file.

In the Template section you’ll find a number of declaration files that serve as a useful starting point when writing a new file. If you already know what your structure is, see the d.ts Template section in the sidebar.

Do’s and Don’ts
Many common mistakes in declaration files can be easily avoided. The Do’s and Don’ts section identifies common errors, describes how to detect them, and how to fix them. Everyone should read this section to help themselves avoid common mistakes.

Deep Dive
For seasoned authors interested in the underlying mechanics of how declaration files work, the Deep Dive section explains many advanced concepts in declaration writing, and shows how to leverage these concepts to create cleaner and more intuitive declaration files.

Publish to npm
The Publishing section explains how to publish your declaration files to an npm package, and shows how to manage your dependent packages.

Find and Install Declaration Files
For JavaScript library users, the Consumption section offers a few simple steps to locate and install corresponding declaration files.


<a name="type-assertions"/>

## Type Assertions

Sometimes you will have information about the type of a value that TypeScript can’t know about.

For example, if you’re using document.getElementById, TypeScript only knows that this will return some kind of HTMLElement, but you might know that your page will always have an HTMLCanvasElement with a given ID.

In this situation, you can use a type assertion to specify a more specific type:

```typescript
const myCanvas = document.getElementById("main_canvas") as HTMLCanvasElement;
```

TypeScript only allows type assertions which convert to a more specific or less specific version of a type. 




<a name="special-types"/>

## Special Types

<a name="array"/>

#### Array

`number[]` = `Array<number>`

<a name="object"/>

#### Object

The special type object refers to any value that isn’t a primitive (string, number, boolean, symbol, null, or undefined).

Note that in JavaScript, function values are objects: They have properties, have Object.prototype in their prototype chain, are instanceof Object, you can call Object.keys on them, and so on. For this reason, function types are considered to be objects in TypeScript.


<a name="function"/>

#### Function

The global type Function describes properties like bind, call, apply, and others present on all function values in JavaScript. It also has the special property that values of type Function can always be called; these calls return any:

```typescript
function doSomething(f: Function) {
  f(1, 2, 3);
}
```


This is an untyped function call and is generally best avoided because of the unsafe any return type.

If you need to accept an arbitrary function but don’t intend to call it, the type `() => void` is generally safer.



<a name="unknown"/>

#### Unknown

The unknown type represents any value. This is similar to the any type, but is safer because it’s not legal to do anything with an unknown value:


<a name="never"/>

#### Never

```typescript
function fail(msg: string): never {
  throw new Error(msg);
}
```

The never type represents values which are never observed. In a return type, this means that the function throws an exception or terminates execution of the program.

`never` also appears when TypeScript determines there’s nothing left in a union.

```typescript
function fn(x: string | number) {
  if (typeof x === "string") {
    // do something
  } else if (typeof x === "number") {
    // do something else
  } else {
    x; // has type 'never'!
  }
}
```

<a name="any"/>

#### Any

```typescript
let obj: any = { x: 0 };
```

When you don’t specify a type, and TypeScript can’t infer it from context, the compiler will typically default to any.

You usually want to avoid this, though, because any isn’t type-checked. Use the compiler flag noImplicitAny to flag any implicit any as an error.

<a name="void"/>

#### Void

void represents the return value of functions which don’t return a value. It’s the inferred type any time a function doesn’t have any return statements, or doesn’t return any explicit value from those return statements:

In JavaScript, a function that doesn’t return any value will implicitly return the value undefined. However, void and undefined are not the same thing in TypeScript




<a name="variable-types"/>

## Variable Types

When you declare a variable using `const`, `var`, or `let`, you can optionally add a type annotation to explicitly specify the type of the variable:

```typescript
let myName: string = "Alice";
```

But, TypeScript tries to automatically infer the types in your code.



<a name="function-expression-types"/>

## Function Expression Types



```typescript
function greeter(fn: (a: string) => void) {
  fn("Hello, World");
}

function printToConsole(s: string) {
  console.log(s);
}

greeter(printToConsole);
```
`(a: string) => void` means “a function with one parameter, named a, of type string, that doesn’t have a return value”. 

Just like with function declarations, if a parameter type isn’t specified, it’s implicitly any.

```typescript
// or use a type alias to name a function type:

type GreetFunction = (a: string) => void;
function greeter(fn: GreetFunction) {
    ...
}
```

<a name="functions-with-properties-types"/>

## Functions with Properties Types

```typescript
type DescribableFunction = {
  description: string;
  (someArg: number): boolean;
};
function doSomething(fn: DescribableFunction) {
  console.log(fn.description + " returned " + fn(6));
}
```

<a name="constructor-types"/>

## Constructor Types


```typescript
type SomeConstructor = {
  new (s: string): SomeObject;
};
function fn(ctor: SomeConstructor) {
  return new ctor("hello");
}
```


Some objects, like JavaScript’s Date object, can be called with or without new. You can combine call and construct signatures in the same type arbitrarily:

```typescript
interface CallOrConstruct {
  new (s: string): Date;
  (n?: number): number;
}
```

<a name="generic-function-parameter-types"/>

## Generic Function Parameter Types

In TypeScript, generics are used when we want to describe a correspondence between two values. We do this by declaring a type parameter in the function signature:

```typescript
function firstElement<Type>(arr: Type[]): Type {
  return arr[0];
}
```


By adding a type parameter Type to this function and using it in two places, we’ve created a link between the input of the function (the array) and the output (the return value). Now when we call it, a more specific type comes out:

```typescript
// s is of type 'string'
const s = firstElement(["a", "b", "c"]);
// n is of type 'number'
const n = firstElement([1, 2, 3]);
```

```typescript
function map<Input, Output>(arr: Input[], func: (arg: Input) => Output): Output[] {
  return arr.map(func);
}

// Parameter 'n' is of type 'string'
// 'parsed' is of type 'number[]'
const parsed = map(["1", "2", "3"], (n) => parseInt(n));
```

<a name="push-type-parameters-down"/>

#### Push Type Parameters Down

Here are two ways of writing a function that appear similar:

```typescript
function firstElement1<Type>(arr: Type[]) {
  return arr[0];
}

function firstElement2<Type extends any[]>(arr: Type) {
  return arr[0];
}

// a: number (good)
const a = firstElement1([1, 2, 3]);
// b: any (bad)
const b = firstElement2([1, 2, 3]);
```

These might seem identical at first glance, but firstElement1 is a much better way to write this function. Its inferred return type is Type, but firstElement2’s inferred return type is any because TypeScript has to resolve the arr[0] expression using the constraint type, rather than “waiting” to resolve the element during a call.

*Rule*: When possible, use the type parameter itself rather than constraining it

<a name="using-fewer-type-parameters"/>

#### Using Fewer Type Parameters

Here’s another pair of similar functions:

```typescript
function filter1<Type>(arr: Type[], func: (arg: Type) => boolean): Type[] {
  return arr.filter(func);
}

function filter2<Type, Func extends (arg: Type) => boolean>(
  arr: Type[],
  func: Func
): Type[] {
  return arr.filter(func);
}
```

We’ve created a type parameter Func that doesn’t relate two values. That’s always a red flag, because it means callers wanting to specify type arguments have to manually specify an extra type argument for no reason. Func doesn’t do anything but make the function harder to read and reason about!

*Rule*: Always use as few type parameters as possible

<a name="type-parameters-should-appear-twice"/>

#### Type Parameters Should Appear Twice

Sometimes we forget that a function might not need to be generic:

```typescript
function greet<Str extends string>(s: Str) {
  console.log("Hello, " + s);
}

greet("world");
```

We could just as easily have written a simpler version:

```typescript
function greet(s: string) {
  console.log("Hello, " + s);
}
```

***Remember***, type parameters are for relating the types of multiple values. If a type parameter is only used once in the function signature, it’s not relating anything.


<a name="object-types"/>

## Object Types

In JavaScript, the fundamental way that we group and pass around data is through objects. In TypeScript, we represent those through object types.

```typescript
// anonymous
function greet(person: { name: string; age: number }) {
  return "Hello " + person.name;
}
```


```typescript
// using an interface

interface Person {
  name: string;
  age: number;
}

function greet(person: Person) {
  return "Hello " + person.name;
}
```

```typescript
// using a type alias.

type Person = {
  name: string;
  age: number;
};

function greet(person: Person) {
  return "Hello " + person.name;
}
```

<a name="proprety-modifiers"/>

## Proprety Modifiers


<a name="optional-properties"/>

#### Optional Properties

`variable?`

This is to make the variable of Optional type. Otherwise declared variables shows "undefined" if this variable is not used.

```typescript
export interface ISearchResult {  
  title: string;  
  listTitle:string;
  entityName?: string,
  lookupName?:string,
  lookupId?:string  
}
```

<a name="defaults"/>

###### Defaults

```typescript
interface PaintOptions {
  shape: Shape;
  xPos?: number;
  yPos?: number;
}

function paintShape(opts: PaintOptions) {
  let xPos = opts.xPos === undefined ? 0 : opts.xPos;
  let yPos = opts.yPos === undefined ? 0 : opts.yPos;
}
```

Or, destructure

```typescript
function paintShape({ shape, xPos = 0, yPos = 0 }: PaintOptions) {
    ...
}
```

<a name="readonly"/>

#### Readonly

While it won’t change any behavior at runtime, a property marked as readonly can’t be written to during type-checking.

```typescript
interface SomeType {
  readonly prop: string;
}
```


<a name="index-signatures"/>

#### Index Signatures

Sometimes you don’t know all the names of a type’s properties ahead of time, but you do know the shape of the values.

In those cases you can use an index signature to describe the types of possible values, for example:

```typescript
interface StringArray {
  [index: number]: string;
}

const myArray: StringArray = getStringArray();
const secondItem = myArray[1];
```

```typescript
interface NumberOrStringDictionary {
  [index: string]: number | string;
  length: number; // ok, length is a number
  name: string; // ok, name is a string
}
```

<a name="intersection-types"/>

#### Intersection Types

```typescript
interface Colorful {
  color: string;
}
interface Circle {
  radius: number;
}

type ColorfulCircle = Colorful & Circle;

draw({ color: "blue", radius: 42 });
```

<a name="union-types"/>

#### Union Types

The first way to combine types you might see is a union type. A union type is a type formed from two or more other types, representing values that may be any one of those types. We refer to each of these types as the union’s members.

```typescript
function printId(id: number | string) {
  console.log("Your ID is: " + id);
}
```

<a name="literal-types"/>

#### Literal Types

```typescript
function printText(s: string, alignment: "left" | "right" | "center") {
  // ...
}
printText("Hello, world", "left");
printText("G'day, mate", "centre");
// >> Argument of type '"centre"' is not assignable to parameter of type '"left" | "right" | "center"'.
```

```typescript
function compare(a: string, b: string): -1 | 0 | 1 {
  return a === b ? 0 : a > b ? 1 : -1;
}
```

```typescript
interface Options {
  width: number;
}
function configure(x: Options | "auto") {
  // ...
}
```

<a name="enums"/>

## Enums

[Enum Reference Page](https://www.typescriptlang.org/docs/handbook/enums.html)

<a name="narrowing"/>

## Narrowing

<a name="equality-narrowing"/>

#### Equality Narrowing
TypeScript also uses switch statements and equality checks like ===, !==, ==, and != to narrow types. For example:

```typescript
function example(x: string | number, y: string | boolean) {
  if (x === y) {
    // We can now call any 'string' method on 'x' or 'y'.
    x.toUpperCase();
    y.toLowerCase();
  } else {
    console.log(x);
    console.log(y);
  }
}
```

<a name="type-aliases-and-interfaces"/>

## Type Aliases and Interfaces


<a name="aliases"/>

#### Aliases

```typescript
type Point = {
  x: number;
  y: number;
};

// Exactly the same as the earlier example
function printCoord(pt: Point) {
  console.log("The coordinate's x value is " + pt.x);
  console.log("The coordinate's y value is " + pt.y);
}

printCoord({ x: 100, y: 100 });
```

A type alias also works with things other than just object types. For example, a type alias can name a union type:

type ID = number | string;


<a name="interfaces"/>

#### Interfaces

```typescript
interface Point {
  x: number;
  y: number;
}

function printCoord(pt: Point) {
  console.log("The coordinate's x value is " + pt.x);
  console.log("The coordinate's y value is " + pt.y);
}

printCoord({ x: 100, y: 100 });
```

<a name="differences"/>

#### Differences

Almost all features of an interface are available in type, the key distinction is that a type cannot be re-opened to add new properties vs an interface which is always extendable.

- Type aliases may not participate in declaration merging, but interfaces can.
- Interfaces may only be used to declare the shapes of object, not re-name primitives.
- Interface names will always appear in their original form in error messages, but only when they are used by name.

<a name="extending-aliases"/>

#### Extending Aliases

Extending a type via intersections

```typescript
type Animal = {
  name: string
}

type Bear = Animal & { 
  honey: Boolean 
}

const bear = getBear();
bear.name;
bear.honey;
```

<a name="extending-interfaces"/>

#### Extending Interfaces
Extending an interface

```typescript
interface Animal {
  name: string
}

interface Bear extends Animal {
  honey: boolean
}

const bear = getBear() 
bear.name
bear.honey
```

Adding new fields to an existing interface

```typescript
interface Window {
  title: string
}

interface Window {
  ts: TypeScriptAPI
}

const src = 'const a = "Hello World"';
window.ts.transpileModule(src, {});
```


<a name="generic-types"/>

## Generic Types


```typescript
interface Box<Type> {
  contents: Type;
}
```
You might read this as “A Box of Type is something whose contents have type Type”. Later on, when we refer to Box, we have to give a type argument in place of Type.


```typescript
let box: Box<string>;
```

Think of `Box` as a template for a real type, where `Type` is a placeholder that will get replaced with some other type. When TypeScript sees `Box<string>`, it will replace every instance of `Type` in `Box<Type>` with string. 

```typescript
interface Box<Type> {
  contents: Type;
}

let boxA: Box<string> = { contents: "hello" };
boxA.contents;
```

Box is reusable in that Type can be substituted with anything. That means that when we need a box for a new type, we don’t need to declare a new Box type at all (though we certainly could if we wanted to).


This also means that we can avoid overloads entirely by instead using generic functions.

```typescript
function setContents<Type>(box: Box<Type>, newContents: Type) {
  box.contents = newContents;
}
```

Much like the Box type above, Array itself is a generic type.

Whenever we write out types like `number[]` or `string[]`, that’s really just a shorthand for `Array<number>` and `Array<string>`

```typescript
interface Array<Type> {
  /**
   * Gets or sets the length of the array.
   */
  length: number;

  /**
   * Removes the last element from an array and returns it.
   */
  pop(): Type | undefined;

  /**
   * Appends new elements to an array, and returns the new length of the array.
   */
  push(...items: Type[]): number;

  // ...
}
```

<a name="generic-type-aliases"/>

#### Generic Type Aliases



```typescript
interface Box<Type> {
  contents: Type;
}
```

Using a type alias instead:

```typescript
type Box<Type> = {
  contents: Type;
};
```
Since type aliases, unlike interfaces, can describe more than just object types, we can also use them to write other kinds of generic helper types.

```typescript
type OrNull<Type> = Type | null;

type OneOrMany<Type> = Type | Type[];

type OneOrManyOrNull<Type> = OrNull<OneOrMany<Type>>;
           
type OneOrManyOrNullStrings = OneOrManyOrNull<string>;
```

<a name="tuple-types"/>

## Tuple Types

A tuple type is another sort of Array type that knows exactly how many elements it contains, and exactly which types it contains at specific positions.


```typescript
type StringNumberPair = [string, number];
```

We can also destructure tuples using JavaScript’s array destructuring.

```typescript
function doSomething(stringHash: [string, number]) {
  const [inputString, hash] = stringHash;

  console.log(inputString);
    >> const inputString: string

  console.log(hash);
    >> const hash: number
}
```

<a name="optional-tuple-properties"/>

#### Optional Tuple Properties

Another thing you may be interested in is that tuples can have optional properties by writing out a question mark (? after an element’s type). Optional tuple elements can only come at the end, and also affect the type of length.

<a name="rest-tuple-properties"/>

#### rest Tuple Properties

Tuples can also have rest elements, which have to be an array/tuple type.

type StringNumberBooleans = [string, number, ...boolean[]];
type StringBooleansNumber = [string, ...boolean[], number];
type BooleansStringNumber = [...boolean[], string, number];



<a name="rest-paramters-and-arguments"/>

## Rest Paramters and Arguments


rest parameters infer an unbounded number of arguments 

<a name="rest-paramters"/>

#### Rest Paramters

```typescript
function multiply(n: number, ...m: number[]) {
  return m.map((x) => n * x);
}
// 'a' gets value [10, 20, 30, 40]
const a = multiply(10, 1, 2, 3, 4);
```

<a name="rest-arguments"/>

#### Rest Arguments

```typescript
const arr1 = [1, 2, 3];
const arr2 = [4, 5, 6];
arr1.push(...arr2);
```


<a name="paramter-types"/>

## Paramter Types


```typescript
function greet(name: string) {
  console.log("Hello, " + name.toUpperCase() + "!!");
}
```

<a name="constraints"/>

#### Constraints


Sometimes we want to relate two values, but can only operate on a certain subset of values. In this case, we can use a constraint to limit the kinds of types that a type parameter can accept.

Let’s write a function that returns the longer of two values. To do this, we need a length property that’s a number. We constrain the type parameter to that type by writing an extends clause:

```typescript
function longest<Type extends { length: number }>(a: Type, b: Type) {
  if (a.length >= b.length) {
    return a;
  } else {
    return b;
  }
}

// longerArray is of type 'number[]'
const longerArray = longest([1, 2], [1, 2, 3]);
// longerString is of type 'string'
const longerString = longest("alice", "bob");
// Error! Numbers don't have a 'length' property
const notOK = longest(10, 100);
>> Argument of type 'number' is not assignable to parameter of type '{ length: number; }'.
```



<a name="parameter-destructuring"/>

#### Parameter Destructuring



```typescript
function sum({ a, b, c }: { a: number; b: number; c: number }) {
  console.log(a + b + c);
}

// is same as

type ABC = { a: number; b: number; c: number };
function sum({ a, b, c }: ABC) {
  console.log(a + b + c);
}
```


<a name="return-types"/>

## Return Types

```typescript
function getFavoriteNumber(): number {
  return 26;
}
```

Much like variable type annotations, you usually don’t need a return type annotation because TypeScript will infer the function’s return type based on its return statements. The type annotation in the above example doesn’t change anything. Some codebases will explicitly specify a return type for documentation purposes, to prevent accidental changes, or just for personal preference.



<a name="type-manipulation"/>

## Type Manipulation

TypeScript’s type system is very powerful because it allows expressing types in terms of other types.

The simplest form of this idea is generics, we actually have a wide variety of type operators available to us. It’s also possible to express types in terms of values that we already have.

By combining various type operators, we can express complex operations and values in a succinct, maintainable way. In this section we’ll cover ways to express a new type in terms of an existing type or value.

- [Generics](https://www.typescriptlang.org/docs/handbook/2/generics.html) - Types which take parameters 
- [Keyof Type Operator](https://www.typescriptlang.org/docs/handbook/2/keyof-types.html) - Using the keyof operator to create new types
- [Typeof Type Operator](https://www.typescriptlang.org/docs/handbook/2/typeof-types.html) - Using the typeof operator to create new types
- [Indexed Access Types](https://www.typescriptlang.org/docs/handbook/2/indexed-access-types.html) - Using Type['a'] syntax to access a subset of a type
- [Conditional Types](https://www.typescriptlang.org/docs/handbook/2/conditional-types.html) - Types which act like if statements in the type system
- [Mapped Types](https://www.typescriptlang.org/docs/handbook/2/mapped-types.html) - Creating types by mapping each property in an existing type
- [Template Literal Types](https://www.typescriptlang.org/docs/handbook/2/template-literal-types.html) - Mapped types which change properties via template literal strings


<a name="classes"/>

## Classes

https://www.typescriptlang.org/docs/handbook/2/classes.html

<a name="modules"/>

## Modules

https://www.typescriptlang.org/docs/handbook/2/modules.html

<a name="references"/>

## References

https://www.typescriptlang.org/docs/handbook/utility-types.html






-----------------------------

<div align="center" style="font-size: 11px; margin: 0; opacity:.6"><a href="#table-of-contents">Top (目次)</a></div>

