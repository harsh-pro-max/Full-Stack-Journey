let btn=document.querySelector("button");

btn.addEventListener("click",()=>{
    console.log("generte random color");
    let h3=document.querySelector('h3');
    let randomColor =getRandomColor();
    h3.innerText=randomColor;

    let div=document.querySelector('div');
    div.style.backgroundColor=randomColor;

    console.log("color updated");
});

function getRandomColor(){
    let red=Math.floor(Math.random()*255);
    let green=Math.floor(Math.random()*255);
    let blue=Math.floor(Math.random()*255);

    let color=` rgb(${red},${green},${blue})`;
    return color;
}

let para=document.querySelector('p');
para.addEventListener("click",function(){
    let randomColor=getRandomColor();
    para.style.color=randomColor;
});
// selecting elements
let p=document.querySelector('.para');
let h1=document.querySelector('.h1');
let h2=document.querySelector('h2');

function chageColor(){
    console.dir(this.innerText);
    this.style.backgroundColor='blue';
}

let btnThis=document.querySelector('.this');
// btnThis.addEventListener("click",function(){
//     console.dir(this.innerText);
//     this.style.backgroundColor='blue';
// })
btnThis.addEventListener("click",chageColor);
p.addEventListener("click",chageColor);
h1.addEventListener("click",chageColor);
h2.addEventListener("click",chageColor);

let btnEvent=document.querySelector(".ev");
btnEvent.addEventListener("dblclick",function(event){
    console.log(event);
    console.log("button clicked");
});

//keyboard events 

let input=document.querySelector("input");

input.addEventListener("keydown",function(event){
    console.log("key",event.key);
    console.log("code",event.code);
    console.log("key was pressed");
    // console.log(event);
});
// characters moves games stero

input.addEventListener("keydown",function(event){
    console.log("code =",event.code);// arrowUp(u),arrowdown(d),arrowRight(r),arrowLeft(l)
    if(event.code=="KeyU"){
        console.log("character mvoes up");
    }
    else if(event.code=='KeyD'){
        console.log("character moves down");
    }
    else if(event.code=='KeyL'){
        console.log("character moves left");
    }else if(event.code=="keyR"){
        console.log("character move in right");
    }
});


// input.addEventListener("keyup",function(){
//     console.log("key was released");
// })


input.addEventListener("keyup",function(){
    console.log("key was pressed");
})

// form events

let form=document.querySelector("form");

// form.addEventListener("submit",function(event){
//     event.preventDefault();
//     console.log("form submitted");
//     alert("form submitted");
// });

// Extracting Form Data
form.addEventListener("submit",function(event){
    event.preventDefault();

    let inp=document.querySelector('.user');
    let pass=document.querySelector('.pass');
    // access form data 
    console.dir(inp);
    console.dir(inp.value);
    console.dir(pass);
    console.dir(pass.value);

    // access form data for form 
    let user=this.elements[0];
    let userPass=this.elements[1];

    console.dir(user.value);
    console.dir(userPass.value);

    console.dir(form);

    alert(`hi ${inp.value}, your password is ${pass.value}`);
});

// change events
let user=document.querySelector('.user');

user.addEventListener("change",function(){
    console.log("input changed");
    console.log("final value=,",user.value);
})

user.addEventListener("input",function(){
    console.log("input event");
    console.log("final value=",this.value);
})