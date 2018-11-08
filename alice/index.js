const request = require('request').defaults({jar: true});

const server = "sec-commerce.seclab.space"

const data = {username: 'alice', password: '4l1c343v3R', cc: '5555555555554444', exp: '07/22', code: '812'};

var do_request = function(){
    var j = request.jar();
    request.get({url: "http://" + server + "/home?lang=en", timeout: 5000, jar: j}, function (err, response, body) {
        if (err) return console.log(err);
        let protocol = response.request.uri.protocol.slice(0, -1);
        if (response.statusCode !== 200) return console.log("[" + protocol + "] [" + response.statusCode + "] " + body);
        console.log("[" + protocol + "] GET response received");
        request.post(protocol + "://" + server + "/login", {form: {username: data.username, password: data.password}, timeout: 5000}, function (err, response, body) {
            if (err) return console.log(err);
            if (response.statusCode !== 200) return console.log("[" + protocol + "] [" + response.statusCode + "] " + body);
            protocol = response.request.uri.protocol.slice(0, -1);
            console.log("[" + protocol + "] POST response received");
            request.put(protocol + "://" + server + "/buy?item=lamp&currency=CAD", {form: {cc: data.cc, exp: data.exp, code: data.code}, timeout: 5000}, function (err, response, body){
                if (err) return console.log(err);
                if (response.statusCode !== 200) return console.log("[" + protocol + "] [" + response.statusCode + "] " + body);
                protocol = response.request.uri.protocol.slice(0, -1);
                console.log("[" + protocol + "] PUT response received");
                request.get({url: protocol + "://" + server + "/check", timeout: 5000}, function (err, response, body) {
                    if (err) return console.log(err);
                    protocol = response.request.uri.protocol.slice(0, -1);
                    if (response.statusCode !== 200) return console.log("[" + protocol + "] [" + response.statusCode + "] " + body);
                    console.log("[" + protocol + "] GET response received");
                });
            });
        });
    });
};

do_request();
setInterval(do_request, 5000);