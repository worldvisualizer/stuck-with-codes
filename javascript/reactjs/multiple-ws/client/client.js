const ws = require('ws');

const generateRandomResponse = (apiMethod) => {
    return {
      "success": true,
      "method": apiMethod,
    }
}
/*
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
*/
// `server` is a vanilla Node.js HTTP server, so use
// the same ws upgrade process described here:
// https://www.npmjs.com/package/ws#multiple-servers-sharing-a-single-https-server

const ws1 = new ws.WebSocket("ws://localhost:3215");
const ws2 = new ws.WebSocket("ws://localhost:3032");

ws1.on('open', () => {
  mes = { message: 'hello', method: 'PreprocessWorkflow' };
  ws1.send(JSON.stringify(mes));
});

ws2.on('open', () => {
  mes = { message: 'hello world', method: 'RunWorkflow' };
  ws2.send(JSON.stringify(mes));
});

ws1.on('message', (response) => {
  console.log(response.toString());
});

ws2.on('message', (response) => {
  console.log(response.toString());
});
