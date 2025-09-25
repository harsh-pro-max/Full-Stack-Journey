const { faker } = require('@faker-js/faker');
const mysql = require('mysql2');
const express = require("express");
const app = express();
const path = require("path");
const methodOverride = require("method-override");


app.use(methodOverride("_method"));
app.use(express.urlencoded({extended:true}));
app.set("view engine" , "ejs");
app.set("views",path.join(__dirname,"/views"));

const connection = mysql.createConnection({
    host : 'localhost',
    user : 'root',
    database : 'delta_app',
    password: 'Harshpro'
});


let getRandomUser = ()=> {
  return [
     faker.string.uuid(),
     faker.internet.username(),
     faker.internet.email(),
     faker.internet.password(),
]
}

// inserting new data
let q = "INSERT INTO user(id,username,email,password) values ?";
// let users= [["123b","123_newuserb","abc@gamil.comb","abcb"],
//             ["123c","123_newuserc","abc@gmial.comc","abcc"],
//             ];

// let data=[];
// for (let i=1;i<=100;i++){
//   data.push(getRandomUser());//100 fake data users
// }

// try{
//     connection.query(q,[data],(err,result)=>{
//     if(err) throw err;
//     console.log(result);
//     // console.log(result.length);
//     // console.log(result[0]);
//     // console.log(result[1]);
//     });
// }
// catch (err) {
//     console.log(err);
// }
// connection.end();

let createRandomUser = ()=> {
  return {
    Id: faker.string.uuid(),
    username: faker.internet.username(),
    email: faker.internet.email(),
    avatar: faker.image.avatar(),
    password: faker.internet.password(),
    birthdate: faker.date.birthdate(),
    registeredAt: faker.date.past(),
  };
}


// console.log(createRandomUser());
// console.log(getRandomUser());

// home route
app.get("/",(req,res)=>{
  let q= `select count(*) from user`;
  
  try{
      connection.query(q,(err,result)=>{
      if(err) throw err;
      let count=result[0]["count(*)"];
      res.render("home.ejs" , {count});
      });
  }
  catch (err) {
      console.log(err);
      console.log("some error in database");
  }
});


// show user route
app.get("/user",(req,res)=>{
  // res.send("success");
  let q= `select * from user`;

  try{
      connection.query(q,(err,users)=>{
      if(err) throw err;
      
      // console.log(result); 
      // res.send(result);
      res.render("showusers.ejs" , {users});
      });
  }
  catch (err) {
      console.log(err);
      console.log("some error in database");
  }
});

// edit route
app.get("/user/:id/edit", (req,res)=>{
  let {id} = req.params;
  let  q=`select * from user where id= '${id}'`;

  try{
      connection.query(q,(err,result)=>{
      if(err) throw err;
      let user = result[0];
      res.render("edit.ejs",{user});
      });
  }
  catch (err) {
      console.log(err);
      console.log("some error in database");
  }

})
// UPDATE (DB) ROUTE
app.patch("/user/:id",(req,res)=>{
  let {id} = req.params;
  let {password:formPass, username: newUsername}=req.body;
  let  q=`select * from user where id= '${id}'`;

  try{
      connection.query(q,(err,result)=>{
      if(err) throw err;
      let user = result[0];
      if(formPass != user.password){
        res.send("wrong password");
      }else{
        let q2 = `update user SET username='${newUsername}' where id='${id}'`;
        connection.query(q2,(err,result)=>{
          if(err) throw err;
          res.redirect("/user");
        });
      }
      });
  }
  catch (err) {
      console.log(err);
      console.log("some error in database");
  }
});

// ADD A NEW USER (FORM) ROUTE
app.get("/user/new", (req, res) => {
    res.render("new.ejs");

});

// ADD A NEW USER (DB) ROUTE
app.post("/user", (req, res) => {
    let { username, email, password } = req.body;
    let id = faker.string.uuid(); 
    
    let q = `INSERT INTO user (id, username, email, password) VALUES ('${id}', '${username}', '${email}', '${password}')`;

    try {
        connection.query(q, (err, result) => {
            if (err) throw err;
            console.log("New user added successfully!");
            res.redirect("/user"); 
        });
    } catch (err) {
        console.log(err);
        res.send("Error adding new user to the database.");
    }
});

// DELETE (DB) ROUTE
app.delete("/user/:id", (req, res) => {
    let { id } = req.params;
    let q = `DELETE FROM user WHERE id = ?`;

    try {
        connection.query(q, [id], (err, result) => {
            if (err) throw err;
            console.log("User deleted successfully!");
            res.redirect("/user"); // Redirect back to the user list
        });
    } catch (err) {
        console.log(err);
        res.send("Error deleting the user from the database.");
    }
});



app.listen("8080",()=>{
  console.log("server is listening to port 8080.");
});
