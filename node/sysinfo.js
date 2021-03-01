var fs = require("fs");
var http = require("http"); 
var os = require("os");
var ip = require("ip");
const { uptime } = require("process");
var freeMemory = (os.freemem / 1000000);
var totalMemory = (os.totalmem / 1000000);
var cpuNum = os.cpus().length;
var sysUptime = os.uptime();
var uptimeHours = Math.floor((sysUptime / 3600) % 24);
var uptimeDays = Math.floor(sysUptime/86400);
var uptimeMinutes = Math.floor(sysUptime % 3600 / 60); 
var uptimeSeconds = Math.floor(sysUptime % 60);

var server = http.createServer(function(req, res) {
    if (req.url === "/" ) {
        fs.readFile("./public/index.html", "UTF-8", function(err, body){
            res.writeHead(200, {"Content-Type": "text/html"});
            res.end(body);
        });
    }

    else if(req.url.match("/sysinfo")) {
        myHostName=os.hostname();
        html=`
        <!DOCTYPE html>
        <head>
            <title>Node JS Response</title>
        </head>
        <body>
            <p>Hostname: ${myHostName}</p>
            <p>IP: ${ip.address()}</p>
            <p>Server Uptime: ${uptimeDays} days ${uptimeHours} hours ${uptimeMinutes} minutes ${uptimeSeconds} seconds</p>
            <p>Total Memory: ${totalMemory} MB</p>
            <p>Free Memory: ${freeMemory} MB</p>
            <p>Number of CPUs: ${cpuNum}</p>
        </body>
        </html>
        `
        res.writeHead(200, {"Content-Type" : "text/html"});
        res.end(html);
    }

    else {
        res.writeHead(404, {"Content-Type":"text/plain"});
        res.end(`404 File Not Found at ${req.url}`);
    }

});

server.listen(3000);
console.log("Server listening on port 3000");