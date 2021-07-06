
# Express


<a name="setup"/>

## Setup

1. install

```bash
npm install express  
npm install @types/express
```

2. import
```typescript
import express from "express"
```

3. construct

```typescript
const app = express();
```

4. set endpoints

```typescript
app.get("/", (req, res) => {
  res.send("hello world")
})
```

5. listen

```typescript
app.listen(4000, () => {

});
```

<a name="usage"/>

## Usage


<a name="session"/>

## Express-Session

##### Step 1

redis stores kv 

`sess:safdsafewrwsad` -> `{ userId: 32 }`

##### Step 2

`Express-Session` sets cookie on browser as a signed version of key in kv pair


e.g., `sdaf2349dfsa@3edsa`

##### Step 3

cookie id send to server on req

##### Step 4

server decrypts cookie using secret to get unsigned key 

##### Step 5

req sent to redis using the decrypted key -> receive corresponding value

##### Step 6

on every request, getting key for kv pair and accessing it again

##### Step 7

any user data that won't change you can store in session obj and it will persist as long as cookie is not cleared.

For data that is variable, you can store the id and then reference database.


## Application Generator


The Express Application Generator tool generates an Express application "skeleton". Install the generator using NPM as shown:

```bash
npx express-generator helloworld

# Install all the dependencies for the helloworld app using NPM as shown:
cd helloworld
npm install

npm start
xdg-open http://localhost:3000
```

NPM will create the new Express app in a sub folder of your current location, displaying build progress on the console. On completion, the tool will display the commands you need to enter to install the Node dependencies and start the app.

## Simple HTTP Server

#### Node HTTP Module

https://nodejs.org/api/http.html

```bash
npm install http-server

http-server -p PORT

xdg-open http://localhost:PORT
```

###### Init Server Obj

The HTTP Server object makes your computer behave as an HTTP server.

```javascript
var http = require('http');
http.createServer(function (req, res) {
  res.writeHead(200, {'Content-Type': 'text/plain'});
  res.write('Hello World!');
  res.end();
}).listen(8080);
```

###### listen method

The server.listen() method creates a listener on the specified port or path.

`server.listen(port, hostname, backlog, callback);`


###### other methods

`close()` `listening` `maxHeadersCount` `setTimeout()` `timeout`


###### URL Module


```javascript
var url = require('url');
var adr = 'http://localhost:8080/default.htm?year=2017&month=february';
var q = url.parse(adr, true);

console.log(q.host); //returns 'localhost:8080'
console.log(q.pathname); //returns '/default.htm'
console.log(q.search); //returns '?year=2017&month=february'

var qdata = q.query; //returns an object: { year: 2017, month: 'february' }
console.log(qdata.month); //returns 'february'
```

```javascript
var http = require('http');
var url = require('url');
var fs = require('fs');

http.createServer(function (req, res) {
  var q = url.parse(req.url, true);
  var filename = "." + q.pathname;
  fs.readFile(filename, function(err, data) {
    if (err) {
      res.writeHead(404, {'Content-Type': 'text/html'});
      return res.end("404 Not Found");
    } 
    res.writeHead(200, {'Content-Type': 'text/html'});
    res.write(data);
    return res.end();
  });
}).listen(8080);
```

###### Events


Objects in Node.js can fire events, like the readStream object fires events when opening and closing a file:

```javascript
var fs = require('fs');
var rs = fs.createReadStream('./demofile.txt');
rs.on('open', function () {
  console.log('The file is open');
});
```

```javascript
var events = require('events');
var eventEmitter = new events.EventEmitter();

var events = require('events');
var eventEmitter = new events.EventEmitter();

//Create an event handler:
var myEventHandler = function () {
  console.log('I hear a scream!');
}

//Assign the event handler to an event:
eventEmitter.on('scream', myEventHandler);

//Fire the 'scream' event:
eventEmitter.emit('scream');
```


###### Formidable (file upload)

```javascript
var formidable = require('formidable');
var http = require('http');
```

1. Create a Node.js file that writes an HTML form, with an upload field:


```javascript
http.createServer(function (req, res) {
  res.writeHead(200, {'Content-Type': 'text/html'});
  res.write('<form action="fileupload" method="post" enctype="multipart/form-data">');
  res.write('<input type="file" name="filetoupload"><br>');
  res.write('<input type="submit">');
  res.write('</form>');
  return res.end();
}).listen(8080);
```

2. Include the Formidable module to be able to parse the uploaded file once it reaches the server. When the file is uploaded and parsed, it gets placed on a temporary folder on your computer.


```javascript
var http = require('http');
var formidable = require('formidable');

http.createServer(function (req, res) {
  if (req.url == '/fileupload') {
    var form = new formidable.IncomingForm();
    form.parse(req, function (err, fields, files) {
      res.write('File uploaded');
      res.end();
    });
  } else {
    res.writeHead(200, {'Content-Type': 'text/html'});
    res.write('<form action="fileupload" method="post" enctype="multipart/form-data">');
    res.write('<input type="file" name="filetoupload"><br>');
    res.write('<input type="submit">');
    res.write('</form>');
    return res.end();
  }
}).listen(8080);
```



3. When a file is successfully uploaded to the server, it is placed on a temporary folder. The path to this directory can be found in the "files" object, passed as the third argument in the parse() method's callback function. To move the file to the folder of your choice, use the File System module, and rename the file:


```javascript
var http = require('http');
var formidable = require('formidable');
var fs = require('fs');

http.createServer(function (req, res) {
  if (req.url == '/fileupload') {
    var form = new formidable.IncomingForm();
    form.parse(req, function (err, fields, files) {
      var oldpath = files.filetoupload.path;
      var newpath = 'C:/Users/Your Name/' + files.filetoupload.name;
      fs.rename(oldpath, newpath, function (err) {
        if (err) throw err;
        res.write('File uploaded and moved!');
        res.end();
      });
 });
  } else {
    res.writeHead(200, {'Content-Type': 'text/html'});
    res.write('<form action="fileupload" method="post" enctype="multipart/form-data">');
    res.write('<input type="file" name="filetoupload"><br>');
    res.write('<input type="submit">');
    res.write('</form>');
    return res.end();
  }
}).listen(8080);
```


###### Nodemailer Module


```javascript
var nodemailer = require('nodemailer');

var nodemailer = require('nodemailer');

var transporter = nodemailer.createTransport({
  service: 'gmail',
  auth: {
    user: 'youremail@gmail.com',
    pass: 'yourpassword'
  }
});

var mailOptions = {
  from: 'youremail@gmail.com',
  to: 'myfriend@yahoo.com',
  subject: 'Sending Email using Node.js',
  text: 'That was easy!'
};

transporter.sendMail(mailOptions, function(error, info){
  if (error) {
    console.log(error);
  } else {
    console.log('Email sent: ' + info.response);
  }
});
```


send HTML
```javascript
var mailOptions = {
  from: 'youremail@gmail.com',
  to: 'myfriend@yahoo.com',
  subject: 'Sending Email using Node.js',
  html: '<h1>Welcome</h1><p>That was easy!</p>'
}
```

send to multiple recipients

```javascript
var mailOptions = {
  from: 'youremail@gmail.com',
  to: 'myfriend@yahoo.com, myotherfriend@yahoo.com',
  subject: 'Sending Email using Node.js',
  text: 'That was easy!'
}
```


###### CLI Options


```bash
usage: http-server [path] [options]

options:
  -p --port    Port to use [8080]
  -a           Address to use [0.0.0.0]
  -d           Show directory listings [true]
  -i           Display autoIndex [true]
  -g --gzip    Serve gzip files when possible [false]
  -b --brotli  Serve brotli files when possible [false]
               If both brotli and gzip are enabled, brotli takes precedence
  -e --ext     Default file extension if none supplied [none]
  -s --silent  Suppress log messages from output
  --cors[=headers]   Enable CORS via the "Access-Control-Allow-Origin" header
                     Optionally provide CORS headers list separated by commas
  -o [path]    Open browser window after starting the server.
               Optionally provide a URL path to open the browser window to.
  -c           Cache time (max-age) in seconds [3600], e.g. -c10 for 10 seconds.
               To disable caching, use -c-1.
  -t           Connections timeout in seconds [120], e.g. -t60 for 1 minute.
               To disable timeout, use -t0
  -U --utc     Use UTC time format in log messages.
  --log-ip     Enable logging of the client's IP address

  -P --proxy         Fallback proxy if the request cannot be resolved. e.g.: http://someurl.com

  --username   Username for basic authentication [none]
               Can also be specified with the env variable NODE_HTTP_SERVER_USERNAME
  --password   Password for basic authentication [none]
               Can also be specified with the env variable NODE_HTTP_SERVER_PASSWORD

  -S --ssl     Enable https.
  -C --cert    Path to ssl cert file (default: cert.pem).
  -K --key     Path to ssl key file (default: key.pem).

  -r --robots        Respond to /robots.txt [User-agent: *\nDisallow: /]
  --no-dotfiles      Do not show dotfiles
  -h --help          Print this list and exit.
  -v --version       Print the version and exit.
```

#### Python HTTP Module

```bash
python -m http-server
```