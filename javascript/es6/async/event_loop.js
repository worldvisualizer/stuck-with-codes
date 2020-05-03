"use strict";

// Javascript Fundamentals - Promises, async/await

// Microtasks
let promise = Promise.resolve();
promise.then(() => alert("promise done!"));
alert("code finished"); // this alert shows first

// because promise runs on microtasks queue,
// normal code execution finishes first.

/*
JS has three "stacks":

    standard stack for all synchronous calls:
      (one function calls another, etc)
    microtask queue:
      (or job queue or microtask stack)
      for all async operations with higher priority
      (process.nextTick, Promises, Object.observe, MutationObserver)
    macrotask queue:
      (or event queue, task queue, macrotask queue)
      for all async operations with lower priority
      (setTimeout, setInterval, setImmediate, requestAnimationFrame, I/O, UI rendering)
*/

// task prioritization in an event loop
while (eventLoop.waitForTask()) {
  const taskQueue = eventLoop.selectTaskQueue()
  if (taskQueue.hasNextTask()) {
    taskQueue.processNextTask()
  }
  const microtaskQueue = eventLoop.microTaskQueue
  while (microtaskQueue.hasNextMicrotask()) {
    microtaskQueue.processNextMicrotask()
  }
}

/*
  1) takes the contents of the input file,
  2) wraps it in a function,
  3) associates that function as an event handler
     that is associated with the “start” or
     “launch” event of the program,
  4) performs other initialization,
  5) emits the program start event,
  6) the event gets added to the event queue,
  7) engine pulls that event off the queue
     and executes the registered handler,
  8) our program runs!
*/

// "script running" is the first macrotask queued

// example.js
console.log('script start'); // macrotask
setTimeout(function() {
  console.log('setTimeout'); // macrotask queued
}, 0);
Promise.resolve().then(function() {
  console.log('promise1'); // microtask
}).then(function() {
  console.log('promise2'); // microtask
});
console.log('script end'); // well, macrotask done.

// result
/*
script start
script end
promise1 // microtask
promise2 // microtask
setTimeout // macrotask
*/

// Microtasks queue
// Reference: https://tc39.es/ecma262/#sec-jobs-and-job-queues

// The queue is first-in-first-out: tasks enqueued first are run first.
// Execution of a task is initiated only when nothing else is running.
// In other words,
// When the JavaScript engine becomes free from the current code,
// it takes a task from the queue and executes it.

// Practices
let i = 0;
let start = Date.now();

function count() {
  // do a heavy job
  for (let j = 0; j < 1e9; j++) {
    i++;
  }
  alert("Done in " + (Date.now() - start) + 'ms');
}

count();
// browser unresponsive, script itself is macrotask
// and its entirety is being run.

let i = 0;
let start = Date.now();

function count() {
  // do a piece of the heavy job (*)
  do {
    i++;
  } while (i % 1e6 != 0);

  if (i == 1e9) {
    alert("Done in " + (Date.now() - start) + 'ms');
  } else {
    setTimeout(count); // schedule the new call (**)
  }
}

count();
// do the macrotask with i = 0 ~ 1e6 first
// setTimeout queues another macrotask

let i = 0;
let start = Date.now();

function count() {
  // move the scheduling to the beginning
  if (i < 1e9 - 1e6) {
    setTimeout(count); // schedule the new call
  }
  do {
    i++;
  } while (i % 1e6 != 0);

  if (i == 1e9) {
    alert("Done in " + (Date.now() - start) + 'ms');
  }
}

count();
// schedule macrotask first while previous one is running
// uses property of setTimeout() - min 4ms delay



