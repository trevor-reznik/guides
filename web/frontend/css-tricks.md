<a name="table-of-contents"/>

![Pictures](banners/CSS-guide-banner.png)

---------------------


##### Table of Contents


- [Flex](#flex)
  - [Definitive Guide](https://css-tricks.com/snippets/css/a-guide-to-flexbox/)
- [Variables](#variables)
- [Keywords](#keywords)

- [Useful External Tools](#external-tools)
  - [visualizers](#visualizers)
  - [plugins](#plugins)
- [Preprocessing](#preprocessing)
- [Assets](#assets)
  - [Favorite Re-usable Components/Pens](#favorites)

--------------

###### Temporary 

https://fontawesome.com/v4.7.0/icons/

https://fontawesome.com/icons/video?style=solid

https://css-tricks.com/multiple-class-id-selectors/


Box sizing vs. Content Box: https://developer.mozilla.org/en-US/docs/Web/CSS/box-sizing 

https://www.w3schools.com/css/css_tooltip.asp



------------


<a name="systems"/>

# Systems



<a name="root"/>

### :root

`:root` is essentially equivalent to the `html` selector. In fact, the :root selector has more authority than html. This is because it’s actually considered a pseudo-class selector (like :first-child or :hover).


<a name="selectors"/>




|  Selector  |  Example  |  Example Example description  |
|------------|-----------|-------------------------------|
|`  .class  `  |`  .intro  `  |  .intro Selects all elements with class="intro"    |
|`  .class1.class2  `  |`  .name1.name2  `  |  .name1.name2 Selects all elements with both name1 and name2 set within its class attribute    |
|`  .class1  `  |`  .class2  `  |  .class2 .name1 .name2 Selects all elements with name2 that is a descendant of an element with name1    |
|`  #id  `  |`  #firstname  `  |  #firstname Selects the element with id="firstname"    |
|`  *  `  |`  *  `  |  * Selects all elements    |
|`  element  `  |`  p  `  |  p Selects all `<p>` elements    |
|`  element.class  `  |`  p.intro  `  |  p.intro Selects all `<p>` elements with class="intro"    |
|`  element,element  `  |`  div,  `  |  div, p Selects all `<div>` elements and all `<p>` elements    |
|`  element  element  `  |` div p `  | Selects all `<p>` elements inside `<div>` elements    |
|`  element>element  `  |`  div > p  `  |  div > p Selects all `<p>` elements where the parent is a `<div>` element    |
|`  element+element  `  |`  div + p  `  |   Selects the first `<p>` element that is placed immediately after `<div>` elements    |
|`  element1~element2  `  |`  p ~ ul  `  |  Selects every `<ul>` element that is preceded by a `<p>` element    |
|`  [attribute]  `  |`  [target]  `  |  [target] Selects all elements with a target attribute    |
|`  [attribute=value]  `  |`  [target=_blank]  `  |  [target=_blank] Selects all elements with target="_blank"    |
|`  [attribute~=value]  `  |`  [title~=flower]  `  |  [title~=flower] Selects all elements with a title attribute containing the word "flower"    |
|`  [attribute`  |`=value]  `  |  [lang  |
|`  [attribute^=value]  `  |`  a[href^="https"]  `  |  a[href^="https"] Selects every `<a>` element whose href attribute value begins with "https"    |
|`  [attribute$=value]  `  |`  a[href$=".pdf"]  `  |  a[href$=".pdf"] Selects every `<a>` element whose href attribute value ends with ".pdf"    |
|`  [attribute*=value]  `  |`  a[href*="w3schools"]  `  |  a[href*="w3schools"] Selects every `<a>` element whose href attribute value contains the substring "w3schools"    |
|`  :active  `  |`  a:active  `  |  a:active Selects the active link    |
|`  ::after  `  |`  p::after  `  |  p::after Insert something after the content of each `<p>` element    |
|`  ::before  `  |`  p::before  `  |  p::before Insert something before the content of each `<p>` element    |
|`  :checked  `  |`  input:checked  `  |  input:checked Selects every checked `<input>` element    |
|`  :default  `  |`  input:default  `  |  input:default Selects the default `<input>` element    |
|`  :disabled  `  |`  input:disabled  `  |  input:disabled Selects every disabled `<input>` element    |
|`  :empty  `  |`  p:empty  `  |  p:empty Selects every `<p>` element that has no children (including text nodes)    |
|`  :enabled  `  |`  input:enabled  `  |  input:enabled Selects every enabled `<input>` element    |
|`  :first-child  `  |`  p:first-child  `  |  p:first-child Selects every `<p>` element that is the first child of its parent    |
|`  ::first-letter  `  |`  p::first-letter  `  |  p::first-letter Selects the first letter of every `<p>` element    |
|`  ::first-line  `  |`  p::first-line  `  |  p::first-line Selects the first line of every `<p>` element    |
|`  :first-of-type  `  |`  p:first-of-type  `  |  p:first-of-type Selects every `<p>` element that is the first `<p>` element of its parent    |
|`  :focus  `  |`  input:focus  `  |  input:focus Selects the input element which has focus    |
|`  :fullscreen  `  |`  :fullscreen  `  |  :fullscreen Selects the element that is in full-screen mode    |
|`  :hover  `  |`  a:hover  `  |  a:hover Selects links on mouse over    |
|`  :in-range  `  |`  input:in-range  `  |  input:in-range Selects input elements with a value within a specified range    |
|`  :indeterminate  `  |`  input:indeterminate  `  |  input:indeterminate Selects input elements that are in an indeterminate state    |
|`  :invalid  `  |`  input:invalid  `  |  input:invalid Selects all input elements with an invalid value    |
|`  :lang(language)  `  |`  p:lang(it)  `  |  p:lang(it) Selects every `<p>` element with a lang attribute equal to "it" (Italian)    |
|`  :last-child  `  |`  p:last-child  `  |  p:last-child Selects every `<p>` element that is the last child of its parent    |
|`  :last-of-type  `  |`  p:last-of-type  `  |  p:last-of-type Selects every `<p>` element that is the last `<p>` element of its parent    |
|`  :link  `  |`  a:link  `  |  a:link Selects all unvisited links    |
|`  ::marker  `  |`  ::marker  `  |  ::marker Selects the markers of list items    |
|`  :not(selector)  `  |`  :not(p)  `  |  :not(p) Selects every element that is not a `<p>` element    |
|`  :nth-child(n)  `  |`  p:nth-child(2)  `  |  p:nth-child(2) Selects every `<p>` element that is the second child of its parent    |
|`  :nth-last-child(n)  `  |`  p:nth-last-child(2)  `  |  p:nth-last-child(2) Selects every `<p>` element that is the second child of its parent, counting from the last child    |
|`  :nth-last-of-type(n)  `  |`  p:nth-last-of-type(2)  `  |  p:nth-last-of-type(2) Selects every `<p>` element that is the second `<p>` element of its parent, counting from the last child    |
|`  :nth-of-type(n)  `  |`  p:nth-of-type(2)  `  |  p:nth-of-type(2) Selects every `<p>` element that is the second `<p>` element of its parent    |
|`  :only-of-type  `  |`  p:only-of-type  `  |  p:only-of-type Selects every `<p>` element that is the only `<p>` element of its parent    |
|`  :only-child  `  |`  p:only-child  `  |  p:only-child Selects every `<p>` element that is the only child of its parent    |
|`  :optional  `  |`  input:optional  `  |  input:optional Selects input elements with no "required" attribute    |
|`  :out-of-range  `  |`  input:out-of-range  `  |  input:out-of-range Selects input elements with a value outside a specified range    |
|`  ::placeholder  `  |`  input::placeholder  `  |  input::placeholder Selects input elements with the "placeholder" attribute specified    |
|`  :read-only  `  |`  input:read-only  `  |  input:read-only Selects input elements with the "readonly" attribute specified    |
|`  :read-write  `  |`  input:read-write  `  |  input:read-write Selects input elements with the "readonly" attribute NOT specified    |
|`  :required  `  |`  input:required  `  |  input:required Selects input elements with the "required" attribute specified    |
|`  :root  `  |`  :root  `  |  :root Selects the document's root element    |
|`  ::selection  `  |`  ::selection  `  |  ::selection Selects the portion of an element that is selected by a user    |
|`  :target  `  |`  #news:target  `  |  #news:target Selects the current active #news element (clicked on a URL containing that anchor name)    |
|`  :valid  `  |`  input:valid  `  |  input:valid Selects all input elements with a valid value    |
|`  :visited  `  |`  a:visited  `  |  a:visited Selects all visited links    |



<a name="shorthand-guide"/>

# Short Hand Reference


<a name="emmet"/>

# Emmet

[Emmet Cheatsheet](https://docs.emmet.io/cheat-sheet/)

###### Useful

generate # of words automatically

`lorem$NUMBER`

create tag.class

`tag.class`

fill doc with starter template

`!` 

. 

`link:css`



<a name="flex"/>

### Flex Boxes

[The Definitive Guide to Flex Boxes](https://css-tricks.com/snippets/css/a-guide-to-flexbox/)








<div align="center" style="font-size: 11px; margin: 0; opacity:.6"><a href="#table-of-contents">Top (目次)</a></div> 
------------------------------------



<a name="variables"/>


### Variables

###### Preprocessor Variables

```css
$variable: red;

color: $variable;
```

###### Custom Properties

```css
--custom-color: red;

color: var(--custom-color);
```

<div align="center" style="font-size: 11px; margin: 0; opacity:.6"><a href="#table-of-contents">Top (目次)</a></div> 
------------------------------------

<a name="keywords"/>

### Keywords

currentColor

```css
.link {
    border: 3px solid transparent;
    color: red;
}

.link:hover {
    border-color: currentColor;
}

/* currentColor is the default value of border-color */
```
*E.g., a button with an icon in it where you want the icon to match the text color*





<div align="center" style="font-size: 11px; margin: 0; opacity:.6"><a href="#table-of-contents">Top (目次)</a></div> 
------------------------------------




<a name="external-tools"/>

### Useful External Tools

- [Interactively generate values using responsive visual-aids/tools](https://www.cssportal.com/css-generators.php)
- [Beautifier](https://www.cleancss.com/css-beautify/)
- [Cleaner (remove all context/data when cloning a site/page)](https://html-cleaner.com/css/)
- [Check for unused CSS and purge automatically](https://purifycss.online/)
- [Put all style attributes inline (for attaching HTML into an email)](https://templates.mailchimp.com/resources/inline-css/)
- [CSS Portal Resources Collection](https://www.cssportal.com/css-resources.php)
- [CSS Portal Tools Collection](https://www.cssportal.com/css-tools.php)
- [Clean CSS | 20 CSS Cleanup Tools You Should Start Using](https://www.webdesigndev.com/clean-css-cleanup-tools/)


<a name="plugins"/>

##### Plugins 

###### Code Highlighting

```html
<link rel="stylesheet"
      href="//unpkg.com/@highlightjs/cdn-assets@11.0.1/styles/default.min.css">
<script src="//unpkg.com/@highlightjs/cdn-assets@11.0.1/highlight.min.js"></script>
```

Use these tags:

```html
<pre><code>
```

It tries to detect the language automatically. If automatic detection doesn’t work for you, or you simply prefer to be explicit, you can specify the language manually in the using the class attribute:

```html
<pre><code class="language-html">...</code></pre>
```

call highlight function

```javascript
$(document).ready( () => ) { hljs.highlightAll(); }
```

<a name="preprocessing"/>

### Preprocessing

CSS on its own can be fun, but stylesheets are getting larger, more complex, and harder to maintain. This is where a preprocessor can help. Sass lets you use features that don't exist in CSS yet like variables, nesting, mixins, inheritance and other nifty goodies that make writing CSS fun again.

Once you start tinkering with Sass, it will take your preprocessed Sass file and save it as a normal CSS file that you can use in your website.

The most direct way to make this happen is in your terminal. Once Sass is installed, you can compile your Sass to CSS using the sass command. You'll need to tell Sass which file to build from, and where to output CSS to. For example, running sass input.scss output.css from your terminal would take a single Sass file, input.scss, and compile that file to output.css.

You can also watch individual files or directories with the --watch flag. The watch flag tells Sass to watch your source files for changes, and re-compile CSS each time you save your Sass. If you wanted to watch (instead of manually build) your input.scss file, you'd just add the watch flag to your command, like so:

sass --watch input.scss output.css

You can watch and output to directories by using folder paths as your input and output, and separating them with a colon. In this example:

sass --watch app/sass:public/stylesheets

Sass would watch all files in the app/sass folder for changes, and compile CSS to the public/stylesheets folder.

###### Variables

Think of variables as a way to store information that you want to reuse throughout your stylesheet. You can store things like colors, font stacks, or any CSS value you think you'll want to reuse. Sass uses the $ symbol to make something a variable. Here's an example:
    • SCSS
    • Sass
    • CSS
SCSS SYNTAX
$font-stack:    Helvetica, sans-serif;
$primary-color: #333;

body {
  font: 100% $font-stack;
  color: $primary-color;
}
CSS OUTPUT
body {
  font: 100% Helvetica, sans-serif;
  color: #333;
}



When the Sass is processed, it takes the variables we define for the $font-stack and $primary-color and outputs normal CSS with our variable values placed in the CSS. This can be extremely powerful when working with brand colors and keeping them consistent throughout the site.

#### Bundling

https://www.npmjs.com/package/tinyify -- a browserify plugin that runs various optimizations, so you don't have to install them all manually.

Webpack
Beginniner Guide: https://www.sitepoint.com/webpack-beginner-guide/
https://medium.com/better-programming/modern-approach-of-javascript-bundling-with-webpack-3b7b3e5f4e7 



<div align="center" style="font-size: 11px; margin: 0; opacity:.6"><a href="#table-of-contents">Top (目次)</a></div> 
------------------------------------




<a name="favorites"/>

### Favorites

###### VHS Aesthetic
- [Distortion Effect](https://codemyui.com/tag/distortion-effect/)
- [VHS Overlay](https://codepen.io/nikma/pen/PagzvV)

###### Animations
- [15 Awesome Animated Background Effects](https://1stwebdesigner.com/15-css-background-effects/)


###### Misc
 - [Dark Mode - Material Design - Interactive Widget Board](https://codepen.io/8aev/pen/bGBWoqG)




<div align="center" style="font-size: 11px; margin: 0; opacity:.6"><a href="#table-of-contents">Top (目次)</a></div> 
------------------------------------

