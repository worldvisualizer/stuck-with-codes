"use strict";

// Javascript Fundamentals - Promises, async/await

// Promises
// a object that links producer and consumer:
// result of the producer relayed to consumer.

let promise = new Promise(function(resolve, reject) {
  // execute: function as a callback is called executor.
  // resolve(value): one of the callbacks to handle value
  // reject(error): handling error as well
})

// question: what about the execution during pending promise?

// consuming functions are .then, .catch, .finally
// they also return promises.
promise.then(
  function(result) {
    handleResult(result);
  },
  function(error) {
    handleError(error);
  });

// finally: we don't know whether the promise is successful or not
// passes through results and errors to next handler
new Promise((resolve, reject) => {
  setTimeout(() => resolve("result"), 2000)
})
  .finally(() => alert("Promise ready"))
  .then(result => alert(result)); // <-- .then handles the result

// question: promise inside a promise
// more accurately: chain and share prior results with Promises
// answer: https://stackoverflow.com/questions/28714298/how-to-chain-and-share-prior-results-with-promises
let parentPromise = new Promise(function(resolve, reject) {
  let data = {data: 'arbitrary'};
  resolve(data);
})

let childPromise = new Promise(function(resolve, reject) {
  let childData = {data: 'arbitrary'};
  resolve(childData);
})

parentPromise.then(
  function(result) {
    return childPromise.then(
      function(response) {
        return result;
      })
  })


// Practice
let promise = new Promise(function(resolve, reject) {
  resolve(1);

  setTimeout(() => resolve(2), 1000);
});
promise.then(alert);
// output is 1. second call to resolve is ignored

function delay(ms) {
  return new Promise(function(resolve, reject) {
    setTimeout(() => resolve(), ms);
  })
}

delay(3000).then(() => alert('runs after 3 seconds'));


// Promise Chaining
const value = new Promise(function(resolve, reject) {
  setTimeout(() => resolve(1), 1000); // (*)
})
.then(function(result) { // (**)
  alert(result); // 1
  return result * 2;
})
.then(function(result) { // (***)
  alert(result); // 2
  return result * 2;
})
.then(function(result) {
  alert(result); // 4
  return result * 2;
});
// the thens are synchronous in this respect.
// data flows, but handlers are by themselves, synchronous.

// this handles chaining asynchronous calls.
new Promise(function(resolve, reject) {
  setTimeout(() => resolve(1), 1000);
})
.then(function(result) {
  alert(result); // 1
  return new Promise((resolve, reject) => { // (*)
    setTimeout(() => resolve(result * 2), 1000);
  });
})
.then(function(result) { // (**)
  alert(result); // 2
  return new Promise((resolve, reject) => {
    setTimeout(() => resolve(result * 2), 1000);
  });
})
.then(function(result) {
  alert(result); // 4
});

// this is a mistake - don't do this.
let promise = new Promise(function(resolve, reject) {
  setTimeout(() => resolve(1), 1000);
});

promise.then(function(result) {
  alert(result); // 1
  return result * 2;
});

promise.then(function(result) {
  alert(result); // 1
  return result * 2;
});

promise.then(function(result) {
  alert(result); // 1
  return result * 2;
});
// this makes 3 independent handlers for one promise.

// example:
function loadScript(src) {
  // creates a <script> tag and append it to the page
  // this causes the script with given src to start loading and run when complete
  return new Promise(function(resolve) {
    let script = document.createElement('script');
    script.src = src;
    document.head.append(script);
  });
}

loadScript("/article/promise-chaining/one.js")
  .then(script => loadScript("/article/promise-chaining/two.js"))
  .then(script => loadScript("/article/promise-chaining/three.js"))
  .then(script => {
    // scripts are loaded, we can use functions declared there
    one();
    two();
    three();
  });

// thenables
// handler may also return thenable object.
// why? because they implement .then
class Thenable {
  constructor(num) {
    this.num = num;
  }

  then(resolve, reject) {
    alert(resolve); // function() { native code }
    // resolve with this.num*2 after the 1 second
    setTimeout(() => resolve(this.num * 2), 1000); // (**)
  }
}

new Promise(resolve => resolve(1))
  .then(result => {
    return new Thenable(result); // (*)
  })
  .then(alert); // shows 2 after 1000ms

// If an error occurs, and there’s no .catch,
// the unhandledrejection handler triggers,
// and gets the event object with the information about the error,
// so we can do something.

// Usually such errors are unrecoverable,
// so our best way out is to inform the user about the problem
// and probably report the incident to the server.

// 5 Promise APIs
/*
    Promise.all(promises):
      waits for all promises to resolve
      and returns an array of their results.
      If any of the given promises rejects,
      it becomes the error of Promise.all,
      and all other results are ignored.

    Promise.allSettled(promises):
      waits for all promises to settle
      and returns their results as an array of objects with:
        state: "fulfilled" or "rejected"
        value (if fulfilled) or reason (if rejected).

    Promise.race(promises):
      waits for the first promise to settle,
      and its result/error becomes the outcome.

    Promise.resolve(value):
      makes a resolved promise with the given value.

    Promise.reject(error):
      makes a rejected promise with the given error.
*/

