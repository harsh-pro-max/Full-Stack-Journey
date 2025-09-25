const express = require("express");
const app = express()
// console.dir(app);

// let port=3000;
let port=8080;

app.listen(port, ()=>{
    console.log(`app is listening on port ${port}`);
})

// app.get("/",(req,res)=>{
//     res.send("you contacted root path");
// })

// app.get("/apple",(req,res)=>{
//     res.send("you contacted apple path");
// })

// app.get("/orange",(req,res)=>{
//     res.send("you contacted orange path");
// })
app.get("/", (req,res) =>{
    res.send("hello, i am root");
});
app.get("/:username/:id",(req,res)=>{
    let { username, id }= req.params;
    res.send(`welcome to the pag of @${username}`);
});

app.get("/search",(req,res)=>{
    // console.log(req.query);
    let { q } = req.query;
    if (!q){
        res.send(`<h1>nothing search<h1>`);
    }
    res.send(`search results for query ${q}`);
})

// app.get('*', (req,res)=>{
//     res.send("this path does not exist");
// });

// app.post("/",(req,res)=>{
//     res.send("you sent a post request to root");
// })

// app.use((req,res)=>{
//     // console.log(req);
//     console.log("request received");
//     res.send(" <h1> hi harsh </h1> ");
// });

