document.getElementById("mainImg");
let smallImages=document.getElementsByClassName("oldImg");

for(let i=0;i<smallImages.length;i++){
    console.dir(smallImages[i].src);
}

// qurey selector
//select element by tag name
console.log(document.querySelector("h1"));

// select element by id
console.log(document.querySelector("#description"));

// slect element by class name
console.dir(document.querySelector(".oldImg"))
// select element by div a 
console.dir(document.querySelector("div a"))

// select element by all querySelectorAll()
console.log(document.querySelectorAll("div a"))

// manupulation of properties and methord
// select p and change it
let para=document.querySelector('p');
// para.innerText='hello harsh';
// para.innerHTML='<h1>hallo harsh</h1>';

let heading=document.querySelector('h1');
// heading.innerHTML='<u>Spider harsh Man</u>';
heading.innerHTML=`<u>${heading.innerText}</u>`;

para.innerHTML= `<u> ${para.innerText}</u>`;

// getters and setters in js
let img=document.querySelector('img');
console.log(img.getAttribute('id'));
//output img id: mainImg
//set attribut change the id 
// console.log(img.setAttribute('id',"spiderMan"));
// id change to spiderMan

//change stying with style tag
let links=document.querySelectorAll('.box a');
for(let i=0;i<links.length;i++){
    links[i].style.color='yellow'; 
}

// nevigataiton paranent child relation
let h4=document.querySelector('h4')
console.log(h4.parentElement);

let box=document.querySelector('.box');
console.log(box.children);

// adding element
let newP=document.createElement('p');
newP.innerText="hi am a new paragraph";
//create document in p but not show after create we append the value
let body=document.querySelector('body');
body.append(newP);

let btn=document.createElement('button');
box.append(btn);
btn.innerText="Click me";

btn.innerHTML="new Button";
let p=document.querySelector('p');
p.insertAdjacentElement('afterbegin',btn);
p.remove();

 