const ws = require('ws');

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
