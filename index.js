let express = require('express');
let app = express();
let path = require('path');
let fs = require('fs');

app.listen(3000, function(){
  console.log("hosting server start");
});

app.get('/', function(req, res){
  console.log('index.html open');
  res.sendFile(path.join(__dirname, "./index.html"));
});

app.get('/frames', function(req, res){
  fs.readFile('./frames/1.jpg', function(error, data){
    res.writeHead(200, {'Content-Type' : 'text/html'});
    res.end(data);
  })
});

app.use('/js', express.static(__dirname + '/node_modules/jquery/dist')); // redirect JS jQuery
app.use('/frames', express.static(__dirname + '/frames'));
