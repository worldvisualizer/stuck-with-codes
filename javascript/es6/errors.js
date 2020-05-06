"use strict;"
// Javascript Fundamentals, Error Handling

// "try..catch"

try {
  // code should be syntactically correct
  // works synchronously. 
  // - because function itself is executed later
  // when engine has already left the try..catch
} catch (err) {
  // error handling
  /*
      Error: {
        name: error name,
        message: textual message about details,
        stack: current call stack,
      }
  */
  // Catch should only process errors that it knows
  // and “rethrow” all others.
} finally {
  // execute always
  // just before the control returns to the outer code.
  // that means explicit "return" in try is not affected.
}

// question: how about this?
function returnFinally() {
  let i = 5;
  try {
    i = 6;
    return i;
  } catch (err) {
    console.log('this is not possible?');
  } finally {
    i = 7; // if we do just this, i = 6.
    return i; // if we do this, i = 7.
  }
}

console.log(returnFinally());

// Global catch
// environments usually provide it, because it’s really useful
// Node.js:
process.on("uncaughtException");
// browser:
window.onerror = function(message, url, line, col, error) {
  // ...
}; 
/*
  1. We register at the service and get a piece of JS
     (or a script URL) from them to insert on pages.
  2. That JS script sets a custom window.onerror function.
  3. When an error occurs, it sends a network request
     about it to the service.
  4. We can log in to the service web interface and see errors.
*/

// Custom Errors
// errors should support basic error properties
// like message, name, stack
class PropertyRequiredError extends Error {
  constructor(property) {
    super("No property: " + property);
    this.name = "PropertyRequiredError"; // (2)
    this.property = property;
  }
}
// We can use instanceof to check for particular errors.




