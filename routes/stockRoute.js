var express=require('express');
var router=express.Router();
var path=require('path');


router.get("/table",function(req,res,next){

res.render('getQt')
});

router.get("/getQuotes",function(req,res,next){
console.log("hii")


 var python = require('child_process').spawn(
     'python',
     // second argument is array of parameters, e.g.:
     ["/home//hatim/Documents/workspace/MajorProject/fetch.py"]);
     var output = "";
     python.stdout.on('data', function(data){ output += data });
     python.on('close', function(code){ 
       if (code !== 0) {  
       		console.log(code)
           return res.send(code); 
       }
       console.log("hey")
       console.log(output)

      return res.json(output);
     });
   
  });

router.get("/predictStock",function(req,res,next){
	//res.redirect("/dashboard");

console.log(req.query.symbol);

 var python = require('child_process').spawn(
     'python',
     // second argument is array of parameters, e.g.:
     ["/home//hatim/Documents/workspace/MajorProject/stock.py",req.query.symbol]);
     var output = "";
     python.stdout.on('data', function(data){ output += data });
     python.on('close', function(code){ 
       if (code !== 0) {  
       		console.log(code)
           return res.send(code); 
       }
       console.log("hey")
       console.log(output)
    res.send(output)
      
     });
   
console.log(req.query.symbol);

});
module.exports=router;