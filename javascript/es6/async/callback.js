"use strict";

// Javascript Fundamentals - Promises, async/await

// Callbacks
// if there's an asynchronous operation, next line will execute
function loadScript(src, callback) {
  let script = document.createElement('script');
  script.src = src;

  script.onload = () => callback(script);

  document.head.append(script);
}

loadScript('/my/script.js', function() {
  // the callback runs after the script is loaded
  newFunction(); // so now it works
  ...
});

// what follows is a callback hell.