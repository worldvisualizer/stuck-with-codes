"use strict";

// Javascript Fundamentals - All the Functions

// function basics and scoping

let userName = "John";

function showMessage() {
	userName = "Bob"; // modifying outer variable possible
	let message = `Hello ${userName}`;
	// outer variable from the function accessible
	return message;
}

function showMessage() {
	let userName = "Bob"; // inner variable eclipses outer.
	let message = `Hello ${userName}`;
	// outer variable from the function accessible
	return message;
}

function showMessage(from, text) {
  from = '*' + from + '*'; // parameter is part of local var.
  alert( from + ': ' + text );
}

let from = "Ann";
showMessage(from, "Hello"); // *Ann*: Hello
// the value of "from" is the same,
// the function modified a local copy
alert( from ); // Ann

// function expressions

// several ways to define function
function foo() {
	//
}

let foo2 = function() {
	//
};

let foo3 = (arg1, arg2) => expression;
// e.g.)
let double = n => n * 2;
let foo4 = (arg3, arg4) => {
    // appropriate scoping
    statement(arg3, arg4);
}

let func = foo;
func();
foo(); // both are the same

// arrow functions are special and do not have their own this.
let user = {
  firstName: "Ilya",
  sayHi() {
    let arrow = () => alert(this.firstName);
    arrow(); // this is from outer user.sayHi() method
  }
};


// The value of this is defined at run-time.
// A function can be copied between objects.
// When a function is called in the “method” syntax:
//    object.method(), the value of this during the call 
//    is object.


