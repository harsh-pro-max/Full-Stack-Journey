const express = require("express");
const app = express();
const port = 8080;
const path = require("path");
// generate a universal id
const {v4:uuidv4} = require("uuid");

 

app.use(express.urlencoded({extended: true}));

app.set("view engine" , "ejs");
app.set("views", path.join(__dirname, "views"));

app.use(express.static(path.join(__dirname,"public")));

let posts = [
    {
        id:uuidv4(),
        username:"apnacollege",
        content:"I love coding"
    },
    {
        id:uuidv4(),
        username:"harshpro",
        content:"hardwork is important to achieve success"
    },
    {
        id:uuidv4(),
        username:"rahulkumr",
        content:"I got selected for my 1st internship"
    }
];

app.get("/posts" , (req,res)=> {
    // res.send("serving working well!");
    res.render("index.ejs", {posts});
});



app.get("/posts/new", (req,res)=>{
    res.render("new.ejs");
})


app.post("/posts",(req,res) =>{
    // console.log(req.body);
    let {username,content } = req.body;
    let id=uuidv4();
    posts.push ({id,username,content});
    // res.send("post request working");
    res.redirect("/posts");
});

app.get("/posts/:id", (req,res)=>{
    let {id} = req.params;
    // console.log(id);
    let post=posts.find((p)=> id ===p.id)
    // console.log(post);
    res.render("show.ejs",{post});
});

app.patch("/posts/:id",(req,res)=>{
    let {id}=req.params;
    let newContent = req.body.content;
    // console.log(newContent);
    let post=posts.find((p)=> id ===p.id);
    post.content= newContent;
    res.send("patch request working");
});

app.get("/posts/:id/edit",(req,res)=>{
    let {id} = req.params;
    let post = posts.find((p)=> id === p.id);
    res.render("edit.ejs");
});

app.listen(port, () =>{
    console.log("listening to port : 8080");
});