"use strict";

// Javascript Fundamentals - Advanced Functions

// Decorator --------------------------------------
// a special function that takes another function
// and alters its behavior.

function slow(x) {
  // there can be a heavy CPU-intensive job here
  alert(`Called with ${x}`);
  return x;
}

function cachingDecorator(func) {
  let cache = new Map();

  return function(x) {
    if (cache.has(x)) {    // if there's such key in cache
      return cache.get(x); // read the result from it
    }

    let result = func(x);  // otherwise call func

    cache.set(x, result);  // and cache (remember) the result
    return result;
  };
}
// reassigning this function with its decorator
slow = cachingDecorator(slow);

alert( slow(1) ); // slow(1) is cached
alert( "Again: " + slow(1) ); // the same

alert( slow(2) ); // slow(2) is cached
alert( "Again: " + slow(2) ); // the same as the previous line

// func.call, func.apply
// syntax: func.call(context, arg1, arg2, ...)
// syntax: func.apply(context, args)

let worker = {
  someMethod() {
    return 1;
  },

  slow(x) {
    alert("Called with " + x);
    return x * this.someMethod();
    // (*) this will be undefined if not set
    // and called like previously
    /* let result = func(x); */
  }
};

function cachingDecorator(func) {
  let cache = new Map();
  return function(x) {
    if (cache.has(x)) {
      return cache.get(x);
    }
    let result = func.call(this, x);
    // "this" is passed correctly now
    cache.set(x, result);
    return result;
  };
}

worker.slow = cachingDecorator(worker.slow);
// now make it caching

alert( worker.slow(2) );
alert( worker.slow(2) );
// works, doesn't call the original (cached)

// func.apply
// how about multi-argument?
