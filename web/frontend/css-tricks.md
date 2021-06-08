<a name="table-of-contents"/>

![Pictures](banners/CSS-guide-banner.png)

---------------------


##### Table of Contents

- [Useful External Tools](#external-tools)
- [Preprocessing](#preprocessing)
- [Favorite Re-usable Components/Pens](#favorites)
- [Flex](#flex)
  - [Definitive Guide](https://css-tricks.com/snippets/css/a-guide-to-flexbox/)
- [Variables](#variables)


--------------

https://fontawesome.com/v4.7.0/icons/

https://fontawesome.com/icons/video?style=solid

https://css-tricks.com/multiple-class-id-selectors/


Box sizing vs. Content Box: https://developer.mozilla.org/en-US/docs/Web/CSS/box-sizing 

https://www.w3schools.com/css/css_tooltip.asp



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