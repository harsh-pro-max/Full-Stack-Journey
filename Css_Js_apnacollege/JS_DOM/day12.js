// concept of call back
function one() {
    return 1;
}
function two(){
    return one()+one();
}
function three(){
    let ans=two()+one();
    console.log(ans);
}
// three();

// changeColors effects
// apply promises
function changeColor(color,delay){
    return new Promise((resolve,reject)=>{
        setTimeout(()=>{
        h1.style.color=color;
        resolve("color changed")
    },delay);
    });
} 

async function demo(){
    await changeColor("red",1000);
    await changeColor("pink",1000);
    await changeColor("yellow",1000)
}
changeColor("red",1000)
    .then(()=>{
        console.log("red color was completed");
        return changeColor("orange",1000);
    })
    .then(()=>{
        console.log("orange color was complted");
        return changeColor("green",1000);
    })
    .then(()=>{
        console.log("green color was complted");
        return changeColor("blue",1000);
    })
    .then(()=>{
        console.log("blue color was completed");
    })

 let h1=document.querySelector("h1");
// changeColor("red",2000);
// changeColor("blue",3000);
// changeColor("purple",4000);


// call back

function saveToDb(data, success, failure) {
  let internetSpeed = Math.floor(Math.random() * 10) + 1;
  if (internetSpeed > 4) {
    success();
  } else {
    failure();
  }
}
// using promises
function saveToDataBase(data){
    return new Promise((resolve,reject)=>{
        let internetSpeed = Math.floor(Math.random()*10)+1;
        if(internetSpeed > 4){
            resolve("succes : data was saved");
        }
        else {
            reject("failure: weak connection");
        }
    });
}
// saveToDataBase("apna college");
// Promise methord then & catch
saveToDataBase("apna college")
    .then(()=>{
        console.log("data1 saved");
        return saveToDataBase("helloworld")
    })
    .then(()=>{
        console.log("data2 saved");
    })
    .catch(()=>{
        console.log("promise was rejected");

});
// nesting of promises then



saveToDb(
  50,
  () => {
    console.log("your data was saved");
  },
  () => {
    console.log("weak connection. data not saved");
  }
);
