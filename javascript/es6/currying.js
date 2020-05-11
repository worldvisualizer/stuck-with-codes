"use strict;"
// Javascript Fundamentals, Currying

// Currying:
// advanced technique of working with functions
// transformation of functions that translates 
// a function from `f(a,b,c) to f(a)(b)(c)`

function curry(f) {
  // curry(f) does currying transform
  return function(a) {
    return function(b) {
      return f(a,b);
    };
  };
}

function sum(a, b) {
  return a + b;
}

let curriedSum = curry(sum);
curriedSum(a)(b);
// function with a returns function with a,b 

// purpose:
// to make partial functions and conveniently use them
// freeze one parameter
function log(date, level, message) {
  return `[${date} ${level} ${message}]`;
}

log = _.curry(log);
let logNow = log(new Date());
logNow('INFO', 'message');

// this one more partial is possible!
let debugNow = logNow('DEBUG');
debugNow('message');

// question: currying function for multiarguments?
function curry(func) {
  return function curryMultiple(...args) {
    if (args.length >= func.length)
      return func.apply(this, args);
    else
      return function(...args2) {
        return curryMultiple.apply(this, args.concat(args2));
      }
  }  
}
// args and args2 are not related. 
// this is now possible:
function sum(a, b, c) {
  return a + b + c;
}

let curriedSum = curry(sum);
curriedSum(1,2,3); // 6
curriedSum(1,2)(3); // still 6
curriedSum(1)(2)(3); // still 6!
