"use strict";

// Javascript Fundamentals - Advanced Functions
// Function Binding -----------------------------------

// Losing "this" is a problem
let user = {
  firstName: "John",
  sayHi() {
    alert(`Hello, ${this.firstName}!`);
    // Once a method is passed somewhere
    // separately from the object – "this" is lost.
  }
};

setTimeout(user.sayHi, 1000); // Hello, undefined!

// func.bind
let boundFunc = func.bind(context);

let user = {
  firstName: "John",
  sayHi() {
    alert(`Hello, ${this.firstName}!`);
  }
};

let sayHi = user.sayHi.bind(user); // (*)

// can run it without an object
sayHi(); // Hello, John!

setTimeout(sayHi, 1000); // Hello, John!

// even if the value of user changes within 1 second
// sayHi uses the pre-bound value
user = {
  sayHi() { alert("Another user in setTimeout!"); }
};

// We can bind not only this, but also arguments. 
// full-syntax: let bound = func.bind(context, [arg1], [arg2], ...);
function mul(a, b) {
  return a * b;
}

let double = mul.bind(null, 2);
// fixing null as the context and 2 as the first argument.
// Further arguments are passed “as is”.
// this practice is called 'partial function'

alert( double(3) ); // = mul(2, 3) = 6
alert( double(4) ); // = mul(2, 4) = 8
alert( double(5) ); // = mul(2, 5) = 10


// Binding practice

function f() {
  alert(this.name);
}
f = f.bind( {name: "John"} ).bind( {name: "Pete"} );
f(); // John
// a function cannot be rebound.


function sayHi() {
  alert( this.name );
}
sayHi.test = 5;

let bound = sayHi.bind({
  name: "John"
});

alert( bound.test ); // result of "bind" is another object.


// partial application for login
function askPassword(ok, fail) {
  let password = prompt("Password?", '');
  if (password == "rockstar") ok();
  else fail();
}

let user = {
  name: 'John',
  login(result) {
    alert( this.name + (result ? ' logged in' : ' failed to log in') );
  }
};
askPassword(
  user.login.bind(user, true),
  user.login.bind(user, false),
); // use partial binding