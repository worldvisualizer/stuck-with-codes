"use strict";

// Javascript Fundamentals - Promises, async/await

// Async/await

// async function

// The word “async” before a function means
// a function always returns a promise.
// Other values are wrapped in a resolved promise
// automatically.
async function f() {
  return 1;
}
f().then(alert); // 1

// await
// await makes javascript wait until the promise settles
// It’s just a more elegant syntax of getting the promise
// result than promise.then, easier to read and write.
// await only works inside an async function.
async function f() {
  let promise = new Promise((resolve, reject) => {
    setTimeout(() => resolve("done!"), 1000)
  });
  let result = await promise; // wait until the promise resolves (*)
  alert(result); // "done!"
}

f();

// error handling
async function f() {
  let response = await fetch('http://no-such-url');
}

// f() becomes a rejected promise
f().catch(alert);
// TypeError: failed to fetch // (*)

/*
The async keyword before a function has two effects:
  - Makes it always return a promise.
  - Allows await to be used in it.

The await keyword before a promise makes JavaScript wait until that promise settles, and then:
  - If it’s an error, the exception is generated — same as if throw error were called at that very place.
  - Otherwise, it returns the result.
*/

// Practice
function loadJson(url) {
  return fetch(url)
    .then(response => {
      if (response.status == 200) {
        return response.json(); // this is also a promise
      } else {
        throw new Error(response.status);
      }
    })
}

loadJson('no-such-user.json')
  .catch(alert); // Error: 404

// => rewrite
async function loadJson(url) {
  let response = await fetch(url);
  if (response.status == 200) {
    let json = response.json();
    return json;
  }
  throw new Error(response.status);
}

loadJson('no-such-user.json')
  .catch(alert); // Error: 404


// call async from non-async
async function wait() {
  await new Promise(resolve => setTimeout(resolve, 1000));
  return 10;
} // returns promise.

function f() {
  // ...what to write here?
  // we need to call async wait() and wait to get 10
  // remember, we can't use "await"
  wait().then(result => console.log(result));
}

f();




