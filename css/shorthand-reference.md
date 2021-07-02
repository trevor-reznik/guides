# CSS Shorthand Reference


#### Place-items

```css
place-items: <align-items> <justify-items>
             /* <block> <inline> */
```

#### Animation

`name` | `duration` | `timing-function` | `delay` | `iteration-count` | `direction` | `fill-mode` | `play-state`

#### Background

`color` | `image` | `repeat` | `attachment` | `position`


#### Border / Outline

`width` | `style` (required) | `color`

#### Border-Block-End

`color` | `style` | `width`

#### Border Image

`outset` | `repeat` | `slice` | `source` | `width`

#### Flex

`grow` | `shrink` | `basis`

#### Font

`style` | `variant` | `weight` | `font-size`/`line-height` | `font-family`

#### Grid

`<'grid-template'> | <'grid-template-rows'> / [ auto-flow && dense? ] <'grid-auto-columns'>? | [ auto-flow && dense? ] <'grid-auto-rows'>? / <'grid-template-columns'>`

gap only

```css
gap : <row-gap> <column-gap>
```

#### Mask

`clip` | `composite` | `image` | `mode` | `origin` | `position` | `repeat` | `size`


#### Offset

`anchor` | `distance` | `path` | `position` | `rotate`

#### Place-Content

`align-content` | `justify-content`

#### Text-Decoration

`line` | `color` | `style` | `thickness`

#### Transition

`property` | `duration` | `timing-function` | `delay`




***NOTE*** A value which is not specified is set to its initial value. That sounds anecdotal, but it really means that it overrides previously set values.

Only the individual properties values can inherit. As missing values are replaced by their initial value, it is impossible to allow inheritance of individual properties by omitting them. The keyword inherit can be applied to a property, but only as a whole, not as a keyword for one value or another. That means that the only way to make some specific value to be inherited is to use the longhand property with the keyword inherit.

Shorthand properties try not to force a specific order for the values of the properties they replace. This works well when these properties use values of different types, as the order has no importance, but this does not work as easily when several properties can have identical values. Handling of these cases are grouped in several categories:
