const express = require("express");
const app = express();
const path = require("path");
const port = 8080;

app.set("view engine", "ejs");
app.set("views", path.join(__dirname, "/views"));

// YEH LINE ADD KARNI HAI
// Isse Express 'public' folder ko serve karega
app.use(express.static(path.join(__dirname, "public")));

// use of ejs res ko render karte hai
app.get("/", (req, res) => {
    // res.send("this is root");
    res.render("home.ejs");
});

app.get("/hello", (req, res) => {
    res.send("hello harsh");
});

app.get("/rolldice", (req, res) => {
    // res.render("rolldice.ejs");
    let diceVal = Math.floor(Math.random() * 6) + 1;
    res.render("rolldice.ejs", { diceVal });
});

// instagram data
app.get("/ig/:username", (req, res) => {
    let { username } = req.params;
    const instaData = require("./data.json");
    
    const data = instaData[username];
    if (data) { // Check karein ki user data mila ya nahi
        console.log(data);
        res.render("instagram.ejs", { data });
    } else {
        res.render("error.ejs"); // Agar user na mile to error page dikhayein
    }
});

app.listen(port, () => {
    console.log(`listening on port ${port}`);
});
