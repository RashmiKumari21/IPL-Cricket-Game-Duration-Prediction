//import the require dependencies
//References
//https://www.geeksforgeeks.org/run-python-script-node-js-using-child-process-spawn-method/

var express = require('express');
var app = express();
var bodyParser = require('body-parser');
var session = require('express-session');
var cookieParser = require('cookie-parser');
var cors = require('cors');
// var mysql = require('mysql');
const csv = require('csv-parser');
const fs = require('fs');
// arry=[]
dict={
    "team1":[],
    "team2":[]
}
  
//use cors to allow cross origin resource sharing
app.use(cors({ origin: 'http://localhost:3000', credentials: true }));

//use express session to maintain session data
app.use(session({
    secret              : 'cmpe273_kafka_passport_mongo',
    resave              : false, // Forces the session to be saved back to the session store, even if the session was never modified during the request
    saveUninitialized   : false, // Force to save uninitialized session to db. A session is uninitialized when it is new but not modified.
    duration            : 60 * 60 * 1000,    // Overall duration of Session : 30 minutes : 1800 seconds
    activeDuration      :  5 * 60 * 1000
}));

// app.use(bodyParser.urlencoded({
//     extended: true
//   }));
app.use(bodyParser.json());

//Allow Access Control
app.use(function(req, res, next) {
    res.setHeader('Access-Control-Allow-Origin', 'http://localhost:3000');
    res.setHeader('Access-Control-Allow-Credentials', 'true');
    res.setHeader('Access-Control-Allow-Methods', 'GET,HEAD,OPTIONS,POST,PUT,DELETE');
    res.setHeader('Access-Control-Allow-Headers', 'Access-Control-Allow-Headers, Origin,Accept, X-Requested-With, Content-Type, Access-Control-Request-Method, Access-Control-Request-Headers');
    res.setHeader('Cache-Control', 'no-cache');
    next();
  });


//Route to handle Post Request Call

app.post('/getTeamAnalysis', function(req,res){
    console.log("Inside Team Based Get Analysis",req.body);    
    var spawn = require("child_process").spawn; 
    var process = spawn('python',["get_team_based_analysis.py", 
                            req.body.team1, 
                            req.body.team2,
                            ] ); 

    process.stdout.on('data', function(data) { 
        console.log(data.toString())
        res.send(data.toString());
    })
    
})


app.post('/getPlayerAnalysis', function(req,res){
    console.log("Inside Player Based Get Analysis",req.body);    
    // res.writeHead(200,{
    //     'Content-Type' : 'application/json'
    // });
    // console.log("Books : ",JSON.stringify(books));
    // res.end(JSON.stringify(books));
    var spawn = require("child_process").spawn; 
    var process = spawn('python',["script.py", 
                            req.body.team1, 
                            req.body.team2,
                            req.body.season] ); 

    process.stdout.on('data', function(data) { 
        // res.send(data.toString()); 
        console.log("data from python",data.toString())
        dict1={
            "team1":[],
            "team2":[],
            "totalTeam1":[],
            "totalTeam2":[]
        }
    
        fs.createReadStream('team_avg_balls_played.csv')
        .pipe(csv())
        .on('data', (row) => {
            // console.log(row);
            dict1["team1"].push({"name":row[req.body.team1],"balls":row.BallsTeam1,"total":row.TotalBallsTeam1})
            dict1["team2"].push({"name":row[req.body.team2],"balls":row.BallsTeam2})
            dict1["totalTeam1"]=row.TotalBallsTeam1
            dict1["totalTeam2"]=row.TotalBallsTeam2
            // dict["team1"].push(row[req.body.team1])
            // dict["team2"].push(row[req.body.team2])
        })
        .on('end', () => {
            // console.log('CSV file successfully processed',Object.keys(dict).length);
            console.log('CSV file successfully processed',dict1);
            res.end(JSON.stringify(dict1));
        });
    } ) 
    
})

app.post('/fetchTeams', function(req,res){
    console.log("Inside Fetch Teams Request",req.body); 
    
    var spawn = require("child_process").spawn; 
    var process = spawn('python',["get_team_players.py", 
                            req.body.team1, 
                            req.body.team2,
                            req.body.season] ); 

    process.stdout.on('data', function(data) { 

        dict={
            "team1":[],
            "team2":[]
        }
    
        fs.createReadStream('team_players.csv')
        .pipe(csv())
        .on('data', (row) => {
            // console.log(row);
            // arry.push([row["PassengerId"],row["Pclass"]])
            dict["team1"].push({"name":row[req.body.team1]})
            dict["team2"].push({"name":row[req.body.team2]})
            
            // dict["team1"].push(row[req.body.team1])
            // dict["team2"].push(row[req.body.team2])
        })
        .on('end', () => {
            // console.log('CSV file successfully processed',Object.keys(dict).length);
            console.log('CSV file successfully processed',dict);
            res.end(JSON.stringify(dict));
        });

    })
   
})


app.post('/getDynamicAnalysis', function(req,res){
    console.log("Inside Get Dynamic Analysis Teams Request",req.body); 
    
    var spawn = require("child_process").spawn; 
    var process = spawn('python',["get_dynamic_analysis.py", 
                            req.body.batsman, 
                            req.body.bowler,
                            ] ); 

    process.stdout.on('data', function(data) { 
        console.log(data.toString())
        res.send(data.toString());
    })
   
})


app.post('/getBowlerBasedAnalysis', function(req,res){
    console.log("Inside Bowler Based Analysis Teams Request",req.body);    
    var spawn = require("child_process").spawn; 
    var process = spawn('python',["get_bowler_based_analysis.py", 
                            req.body.team1, 
                            req.body.team2,
                            ] ); 

    process.stdout.on('data', function(data) { 
        console.log(data.toString())
        res.send(data.toString());
    }) 
      
})

//start your server on port 3001
app.listen(3001);
console.log("Server Listening on port 3001");