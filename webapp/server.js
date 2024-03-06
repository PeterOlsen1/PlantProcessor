const http = require('http');
const fp = require('fs');

const port = 3000;

const server = http.createServer((req, res) => {
    console.log(req);
    fp.readFile("/myPlants.html")
})

server.listen(port);