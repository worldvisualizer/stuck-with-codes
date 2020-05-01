"use strict";

// Javascript Fundamentals - Advanced Functions

// Recursion and Stack --------------------------
// example:
pow(2,2); // 4
pow(2,3); // 8

function pow(x, n) {
  let result = 1;
  for (let i = 0; i < n; i++) {
    result *= x;
  }
  return result;
}

function pow(x, n) {
  if (n === 1) {
    return x;
  }
  return x * pow(x, n-1);
}

// Execution context holds information about
// the process of execution of a running function
// It is an internal data structure that contains details 
// about the execution of a function: where the control flow is now
// current variable, value of this, etc.


// Rest Parameters ... ----------------------------

function sumAll(...args) { // array
  let sum = 0;
  for (let arg of args)
    sum += arg;
  return sum;
}
// The rest parameters must be at the end

// there's something called "arguments" variable
function showName() {
  alert( arguments.length );
  alert( arguments[0] );
  alert( arguments[1] );
  // it's iterable
  // for(let arg of arguments) alert(arg);
}
// shows: 2, Julius, Caesar
showName("Julius", "Caesar");
// shows: 1, Ilya, undefined (no second argument)
showName("Ilya");

// Arrow functions do not have "arguments"
// If we access the arguments object from an arrow function,
// it takes them from the outer “normal” function.
function f() {
  let showArg = () => alert(arguments[0]);
  showArg();
}

f(1); // 1
// arrow functions don’t have their own this.
// they don’t have the special arguments object either.

// Spread Syntax Behaviors (cool for rest parameters) ----------
// The spread syntax internally uses iterators to gather elements,
// the same way as for..of does.
let arr1 = [1, -2, 3, 4];
let arr2 = [8, 3, -8, 1];
alert( Math.max(...arr1) );
// 4 (spread turns array into a list of arguments)
alert( Math.max(...arr1, ...arr2) );
// 8: pass multiple iterables
alert( Math.max(1, ...arr1, 2, ...arr2, 25) );
// doesn't matter for normal values as well

let merged = [0, ...arr1, 2, ...arr2];
alert(merged);
// 0,3,5,1,2,8,9,15 (0, then arr1, then 2, then arr2)

let str = "Hello";
alert( [...str] );
// H,e,l,l,o

let str = "Hello";
// Array.from converts an iterable into an array
alert( Array.from(str) );
// H,e,l,l,o : and string is iterable

let arr = [1, 2, 3];
let arrCopy = [...arr]; // spread the array into a list of parameters
                        // then put the result into a new array

// do the arrays have the same contents?
alert(JSON.stringify(arr) === JSON.stringify(arrCopy)); // true
// are the arrays equal?
alert(arr === arrCopy); // false (not same reference)
// modifying our initial array does not modify the copy:
arr.push(4);
alert(arr); // 1, 2, 3, 4
alert(arrCopy); // 1, 2, 3

let obj = { a: 1, b: 2, c: 3 };
let objCopy = { ...obj };
// spread the object into a list of parameters
// then return the result in a new object


// Variable scope









