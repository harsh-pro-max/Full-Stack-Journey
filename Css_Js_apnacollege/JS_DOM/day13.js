/*
// Async Keyword 

async function greet(){
    throw "404 page found";

    return "hello";
}

greet()
    .then((result)=>{
        console.log("promise was resolved");
        console.log("result was:",result);
    })
    .catch((err)=>{
        console.log("promise was rejected with err:",err);
    })

// Await Keyword
function getNum(){
    return new Promise((resolve,reject)=>{
        setTimeout(()=>{
            let num= Math.floor(Math.random()*10)+1;
            console.log(num);
            resolve();
        },1000);
    });
}

async function demo() {
    await getNum();
    getNum();
    getNum();
}

let jsonRes ='{"fact":"Cats can judge within 3 inches the precise location of a sound being made 1 yard away.","length":86}'

// console.log(jsonRes);

let validRes=JSON.parse(jsonRes);
console.log(validRes.fact);

let student={
    name:"shradha",
    marks:95,
}
*/

// creating first request
let url="https://catfact.ninja/fact";

factch(url)
    .then((response)=>{
        console.log(response);
    })

    .catch((err)=>{
        console.log("error-",err);
    });