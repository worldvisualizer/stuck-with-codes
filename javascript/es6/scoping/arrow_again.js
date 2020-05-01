"use strict";

// Javascript Fundamentals - Advanced Functions

// Arrow Function
// we usually don’t want to leave the current context.

/*
    - Do not have this
    - Do not have arguments
    - Can’t be called with new
    - They also don’t have super, but we didn’t study it yet.
      We will on the chapter Class inheritance
*/

// same without arrow function
function defer(f, ms) {
  return function(...args) {
    let ctx = this;
    setTimeout(function() {
      return f.apply(ctx, args);
    }, ms);
  };
}

// with arrow function
function defer(f, ms) {
	// arrow functions do not have arguments variable
	// so we can use arguments from defer.
  return function() {
    setTimeout(() => f.apply(this, arguments), ms)
  };
}

function sayHi(who) {
  alert('Hello, ' + who);
}

let sayHiDeferred = defer(sayHi, 2000);
sayHiDeferred("John"); // Hello, John after 2 seconds
