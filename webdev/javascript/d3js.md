# D3JS Basics

D3JS is a powerful document manipulation tool

## Getting Started

```html
<script src="https://d3js.org/d3.v7.min.js"></script>
```

## Fundamentals 

```javascript
d3.select('div')                        // Select all div elements. 1) Use .className for class selection 2) Use #idName for id selection
  .selectAll('p')                       // Select all p elements within selected div elements
  .data([1, 2, 3])                      // Bind all p elements to data 
  .enter()                              // Return all non-data-binded elements
  .append('p')                          // Append p to all non-databinded 
  .text(dta => dta)                     // Specify text of the selected
  .style('border', '1px solid red')     // Set css style
```
