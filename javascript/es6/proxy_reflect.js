"use strict";

// Javascript Fundamentals - Proxy and Reflect

// Proxy ------------
// wraps another object and intercepts operations
// and optionally handling them on its own

let proxy = new Proxy(target, handler);
// target: Object to wrap
// handler: Object with proxy functions
// trapping ones: get trap, set trap, and so on

let target = {};
let proxy = new Proxy(target, {}); // empty handler

proxy.test = 5; // writing to proxy (1)
alert(target.test); // 5, the property appeared in target!

alert(proxy.test); // 5, we can read it from proxy too (2)

for(let key in proxy) {
  alert(key); // test, iteration works (3)
}

// write operation proxy.test= sets value on target
// read operation proxy.test returns value from target
// iteration over proxy returns values from target.

// proxy does not have its own properties.

// default value array
let numbers = [0, 1, 2];

numbers = new Proxy(numbers, {
  get(target, prop) {
    if (prop in target) {
      return target[prop];
    } else {
      return 0; // default value
    }
  }
});

alert( numbers[1] ); // 1
alert( numbers[123] ); // 0 (no such item)

// type enforced array
let numbers = [];

numbers = new Proxy(numbers, { // (*)
  set(target, prop, val) { // to intercept property writing
    if (typeof val == 'number') {
      target[prop] = val;
      return true;
    } else {
      return false;
    }
  }
});

numbers.push(1); // added successfully
numbers.push(2); // added successfully
alert("Length is: " + numbers.length); // 2

numbers.push("test"); // TypeError ('set' on proxy returned false)

alert("This line is never reached (error in the line above)");

// there are method invariants.
// [[Set]] must return true if value was written successfully, otherwise false
// [[Delete]] as well.
// [[GetPrototypeOf]] reading prototype of the proxy must return the 
// prototype of the target object.

let user = { };

user = new Proxy(user, {
  // apparently, this is the object properties array.
  // preventing accessing "private" variable is possible
  ownKeys(target) { // called once to get a list of properties
    return Object.keys(target).filter(
      key => !key.startsWith('_'));
  },

  getOwnPropertyDescriptor(target, prop) { // called for every property
    return {
      enumerable: true,
      configurable: true
      /* ...other flags, probable "value:..." */
    };
  }

});

// you can wrap a proxy around a function as well.
function delay(f, ms) {
  // return a wrapper that passes the call to f after the timeout
  return function() { // (*)
    // simple function wrapper as a function.
    // using function scoping.
    setTimeout(() => f.apply(this, arguments), ms);
  };
}

function sayHi(user) {
  alert(`Hello, ${user}!`);
}
// after this wrapping, calls to sayHi will be delayed for 3 seconds
sayHi = delay(sayHi, 3000);
sayHi("John"); // Hello, John! (after 3 seconds)

// now using proxy. ermygod. why didn't I think of this
function delay(f, ms) {
  return new Proxy(f, {
    apply(target, thisArg, args) {
      setTimeout(() => target.apply(thisArg, args), ms);
    }
  });
}

function sayHi(user) {
  alert(`Hello, ${user}!`);
}

sayHi = delay(sayHi, 3000);

alert(sayHi.length); // 1 (*) proxy forwards "get length" operation to the target

sayHi("John"); // Hello, John! (after 3 seconds)


// reflect: built-in object that simplifies creation of Proxy.


