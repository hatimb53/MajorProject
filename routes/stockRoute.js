var express=require('express');
var router=express.Router();
var path=require('path');





router.get("/",function(req,res,next){
res.render('front');
});

router.get("/loginview",function(req,res,next){
res.render('login');
});

router.get("/registerview",function(req,res,next){
res.render('register');
});


module.exports=router;