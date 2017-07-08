var express=require('express');

var bodyparser=require('body-parser');

var app=express();
var mainDirectory=__dirname
module.exports.mainD= mainDirectory

var session = require('express-session');

var path=require('path');


//var RedisStore = require('connect-redis')(express);
app.set('trust proxy', 1) 

// trust first proxy 

app.use(session({
  secret: 'keyboard cat',
  resave: false,
  saveUninitialized: true,
 

}))

var basics=require('./routes/basicsRoute.js');
var database=require('./routes/databaseRoute.js');
var stock=require('./routes/stockRoute.js');

app.use(express.static(path.join(__dirname,'public')));
var ejs=require('ejs');
app.set('view engine','ejs');
app.set('views',path.join(__dirname,'views'));
app.engine('html',ejs.renderFile);


app.use(bodyparser.json());
app.use(bodyparser.urlencoded({extended:false}));

app.use('/',basics);
app.use('/data',database);
app.use('/stock',stock);

var port=process.env.PORT || 3000	;
app.listen(port,function(){
console.log("Server Listening on port:3000");
});

module.exports=app;