
var express=require('express');
var router=express.Router();
var path=require('path');


router.get("/",function(req,res,next){
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