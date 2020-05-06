"use strict;"
// Javascript Fundamentals, Networks

// Fetch
let promise = fetch(url, [options]);

let response = await fetch(url);
if (response.ok) {
  let json = await response.json();
  // response.text, .json, .formData, .blob, .arrayBuffer
}

let response = await fetch('/article/fetch/logo-fetch.svg');
let blob = await response.blob();

let img = document.createElement('img');
img.style = 'position:fixed;top:10px';
document.body.append(img);

img.src = URL.createObjetURL(blob);

setTimeout(() => {
  img.remove();
  URL.revokeObjectURL(img.src);
}, 3000);

let response = await fetch('...');
response.headers.get('Content-Type'); 

// POST
let user = {
  name: 'Joseph',
  surname: 'Smith',
};

let response = await fetch('/article/fetch/user', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json;charset=utf-8',
  },
  body: JSON.stringify(user),
});

let result = await response.json(); // why await here?

// CORS
// requesting for other sites, from a certain website
// why? getting third-party site information
// any non-simple requests require preflight request

// Step 1: preflight request
/*
  OPTIONS /service.json
  Host: site.com
  Origin: https://javascript.info
  Access-Control-Request-Method: PATCH
  Access-Control-Request-Headers: Content-Type,API-Key
*/

// Step 2: preflight response
/*
  Access-Control-Allow-Methods: PATCH
  Access-Control-Allow-Headers: Content-Type,API-Key
*/

// Step 3: actual request
/*
  PATCH /service.json
  Host: site.com
  Content-Type: application/json
  API-Key: secret
  Origin: https://javascript.info
*/

// Step 4: actual response
/*
  Access-Control-Allow-Origin: https://javascript.info
*/


// Resuming File Upload
// upload.onprogress is only useful for keeping track
// because to resume upload, we need how many number of bytes received
let field = file.name + '-' + file.size + '-' + file.lastModifiedDate;

let response = await fetch('status', {
  headers: {
    'X-File-Id': fileId,
  }
});

// so this comes down to fetching received bytes from the server
let startByte = +await response.text();





