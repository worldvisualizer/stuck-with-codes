const express = require('express');
const ws = require('ws');

const app = express();

const generateRandomResponse = (apiMethod) => {
    return {
      "success": true,
      "method": apiMethod,
    }
}

// Set up a headless websocket server that prints any
// events that come in.
const wsServer = new ws.Server({ noServer: true });
wsServer.on('connection', socket => {
  socket.on('message', (message) => {
    msgStr = message.toString();
    apiRequest = JSON.parse(msgStr);
    console.log(apiRequest);
    response = generateRandomResponse(apiRequest.method);
    responseStr = JSON.stringify(response);
    socket.send(responseStr);
  });
});

// `server` is a vanilla Node.js HTTP server, so use
// the same ws upgrade process described here:
// https://www.npmjs.com/package/ws#multiple-servers-sharing-a-single-https-server

const rngFunc = (min, max) => {
  return Math.floor(Math.random() * (max - min + 1)) + min;
}

portNumber = rngFunc(3000, 3500);
const server = app.listen(portNumber);
console.log("ws server listening on port: ", portNumber);
server.on('upgrade', (request, socket, head) => {
  wsServer.handleUpgrade(request, socket, head, socket => {
    wsServer.emit('connection', socket, request);
  });
});

