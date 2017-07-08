
var express=require('express');
var router=express.Router();
var path=require('path');

var remote = require('remote'); 
var win = remote.getCurrentWindow();


router.get("/",function(req,res,next){
	var s=""
	var p=__dirname.split("/")
	for(var i=0;i<p.length-1;i++){
		s+=p[i]+"/"
	console.log(s)
	}
	
	console.log(s)
res.render('index.html')
});

router.get("/loginview",function(req,res,next){
res.render('login.html');
});

router.get("/registerview",function(req,res,next){
res.render('register.html');
});

router.get("/dashboard",function(req,res,next){
	console.log(req.query.EmailId)
	res.header('Cache-Control', 'no-cache, private, no-store, must-revalidate, max-stale=0, post-check=0, pre-check=0');
res.render('dashboard');
});

module.exports=router;