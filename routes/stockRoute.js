var express=require('express');
var router=express.Router();
var path=require('path');
var s=""
  var p=__dirname.split("/")
  for(var i=0;i<p.length-1;i++){
    s+=p[i]+"/"
  console.log(s)
  }
  
  console.log(s)

router.get("/table",function(req,res,next){

res.render('getQt')
});

router.get("/getQuotes",function(req,res,next){
console.log("hii")
console.log(s)

console.log(path.join(s,'python/fetch.py'))
 var pr=s+"python/fetch.py"
 console.log("pr ",pr)
 var t="/home/hatim/Documents/workspace/MajorProject/python/fetch.py"
 var python = require('child_process').spawn(
     'python',
     // second argument is array of parameters, e.g.:

     [""+t+""]);


     var output = "";
      console.log("hey")
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
     [path.join(s,'python/predict.py'),req.query.symbol]);
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