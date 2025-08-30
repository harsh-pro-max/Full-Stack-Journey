let btn=document.querySelector("button");
console.dir(btn);

btn.onclick=function(){
    console.log("button was clicked");
    alert("button was clicked");
}

function sayHello(){
    alert("hello!");
}

function sayName(){
    alert("Harsh kushwaha");
}
// btn.onclick=sayHello();

let allbtn=document.querySelectorAll("button");

for( e of allbtn){
    // e.onclick=sayHello;
    // console.dir(e);
    // e.onmouseenter=function(){
    //     console.log("you entered a button");
    // }
    // e.addEventListener('click',sayHello);
    // e.addEventListener('click',sayName);
    e.addEventListener('dblclick',function(){
        console.log("doble clicked hit");
    });
}
