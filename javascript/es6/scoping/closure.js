"use strict";

// Javascript Fundamentals - Advanced Functions

// Variable Scope
// Consideration to lexical environment

// 1) when function is created, execution context gets associated with it.
// 2) those execution contexts include all the local variables and parameters about it.
// 3) when searching for variable, resolution goes:
//    immediately outer -> more outer -> ... -> global
function makeCounter() {
  let count = 0; // outer variable.
  return function() {
    return count++;
  };
}

let counter = makeCounter();
// return value => function() with reference to environment.

alert( counter() ); // 0
alert( counter() ); // 1
alert( counter() ); // 2

// 1)
let phrase; // 2)
phrase = "hello"; // 3)
phrase = 'bye'; // 4)

/* 
   Lexical environment is different from runtime environment.
   Lexical Environment is pre-populated with all declared variables.
   1) Initially, they are in the “Uninitialized” state.
      That’s a special internal state,
      it means that the engine knows about the variable,
      but it cannot be referenced until it has been
      declared with let. (dead zone)
      It’s almost the same as if the variable didn’t exist. 
   2) Then let phrase definition appears.
      There’s no assignment yet, so its value is undefined. 
      We can use the variable since this moment.
   3) phrase is assigned a value.
   4) phrase changes the value.
*/

// all javascript functions support closure.
// closure: function that remembers its outer variables and can access them. 

// Closure Practice
function alert(str) {
  console.log(str);
}

let name = "John";
function sayHi() {
  alert("Hi, " + name);
}
name = "Pete";
sayHi(); // Answer: Hi Pete


function makeWorker() {
  let name = "Pete";
  return function() {
    alert(name);
  };
}
let name = "John";
// create a function
let work = makeWorker();
// call it
work(); // Answer: Pete


function makeCounter() {
  let count = 0;
  return function() {
    return count++;
  };
}
let counter = makeCounter();
let counter2 = makeCounter();
alert( counter() ); // 0
alert( counter() ); // 1
alert( counter2() ); // Answer: 0
alert( counter2() ); // Answer: 1
// counter and counter2 are separate function.


sum(1)(2) = 3
sum(5)(-1) = 4
function sum(a) { // parameters are part of the scope you know
  return function(b) {
    return a + b;
  }
}


let x = 1;
function func() {
  console.log(x); // x not defined. because of dead zone.
  let x = 2; // until the runtime reaches this line, x cannot be used
}
func();


/* 
  inBetween(a, b) – between a and b or equal to them (inclusively).
  inArray([...]) – in the given array.
*/
function inBetween(start, end) {
  return function(x) {
    return x >= start && x <= end; 
    // when in doubt, make a function that accepts parameter it needs
    // and accessing outer variables declared outside.
  };
}

function inArray(arr) {
  return function(x) {
    return arr.includes(x);
  }
}

let arr = [1, 2, 3, 4, 5, 6, 7];
alert( arr.filter(inBetween(3, 6)) ); // 3,4,5,6
alert( arr.filter(inArray([1, 2, 10])) ); // 1,2


// nested setTimeout
/** instead of:
let timerId = setInterval(() => alert('tick'), 2000);
*/
let timerId = setTimeout(function tick() {
  alert('tick');
  timerId = setTimeout(tick, 2000); // (*)
}, 2000);
