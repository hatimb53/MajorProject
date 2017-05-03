var express=require('express');
var router=express.Router();
var path=require('path');
var MongoClient = require('mongodb').MongoClient;
var assert = require('assert');
var ObjectId = require('mongodb').ObjectID;
//var url = 'mongodb://HbMongo:786_Hatim#mlab@ds137760.mlab.com:37760/user';

var url ='mongodb://localhost:27017/user';

router.post("/register",function(req,res,next){

console.log(req.body.Name)
var detailes={Name:req.body.Name,LastName:req.body.LastName,Password:req.body.Password,Address:req.body.Address ,MobileNo:req.body.MobileNo ,EmailId:req.body.EmailId,Country:req.body.Country,City:req.body.City};


var insertdoc = function(db, callback) {
   var cursor =db.collection('Profile').insert(detailes,function(err, doc){
    console.log(doc)
   });
};

MongoClient.connect(url, function(err, db) {
  assert.equal(null, err);
  insertdoc(db, function() {
      db.close();
  });

});
});



router.post("/update",function(req,res,next){
  console.log("update");


console.log(req.session.EmailId);

var detailes={Name:req.body.Name,LastName:req.body.LastName,Password:req.body.Password,Address:req.body.Address ,MobileNo:req.body.MobileNo ,EmailId:req.body.EmailId,Country:req.body.Country,City:req.body.City};
console.log(req.body.Name);
var insertdoc = function(db, callback) {
   var cursor =db.collection('Profile').update({EmailId:req.session.EmailId},{$set : detailes},function(err, doc){
  //  console.log(doc)
   });
};

MongoClient.connect(url, function(err, db) {
  assert.equal(null, err);
  insertdoc(db, function() {
      db.close();
  });

});
});


router.post("/login",function(req,res,next){
console.log("Asdf")
var id = req.body.EmailId;
console.log("email",id)
var pass= req.body.Password
console.log("pass",pass)
count=0;
var verify= function(db, callback) {
   var cursor =db.collection('Profile').find({$and :[{'EmailId':id},{"Password":pass}]}).each(function(err, doc){
   console.log("doc",doc);
   console.log("count",count);
   count++;
   if(count==2&&doc==null){
     res.redirect('/dashboard?EmailId='+req.body.EmailId);
    req.session.EmailId=req.body.EmailId;
   console.log('complete')

  }
  else if(count==1&&doc==null){
    res.redirect('/');
  }
  
   });

   console.log("cursor",cursor);
};


MongoClient.connect(url, function(err, db) {
  assert.equal(null, err);
 verify(db, function() {
      db.close();
  });
});

});


module.exports=router;
