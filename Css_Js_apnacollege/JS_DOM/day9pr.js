// practice question 
// a <p> with red thext that says 'hey i'm red!';

let body=document.querySelector('body');
let p=document.createElement('p');
p.innerText="Hey I'm red!";
p.style.color='red';
body.append(p);

// an <h3> with blue text that says "I'm a blue h3!";
let h3=document.createElement('h3');
h3.innerText="I'm a blue h3!";
h3.style.color='blue';
body.append(h3);

// a <div> with a black border and pink background color with the following elements inside of it.
// another <h1> that says 'I'm in a div"
// a <p> that says 'ME TOO!
// 1) Elements banao
const div = document.createElement('div');
const h1 = document.createElement('h1');
const para2 = document.createElement('p');

// 2) Text set karo
h1.textContent = "I'm in a div";
para2.textContent = "ME TOO!";

// 3) Div ke andar elements daalo
div.append(h1, para2);

// 4) Style do (JS se)
div.style.backgroundColor = 'pink';
div.style.border = '2px solid black';
div.style.padding = '8px';

// 5) Page par add karo
document.body.append(div);

// practice assignment
//1. Create a new input and button element on the page using JavaScript only.Set the text of button to "Click me'".

//creating button 
const btn=document.createElement('button');
const input=document.createElement('input');

// add button in body 
body.append(input);
body.append(btn);

//set the text
btn.innerText="Click Me!";

// 2. Add following attributes to the element:
    //change placeholder value of input to username
    // change the id of button to 'btn',
input.placeholder="username";
btn.id="btn";

// 3. Access the btn using the querySelector and button id. change the button background color to blue and text color to white.
let selBtn=document.querySelector('button');

let myBtn=document.getElementById('btn');
selBtn.style.backgroundColor='blue';
myBtn.style.color='white';
selBtn.style.color='white';

// 4. Create an h1 element on the page and set its text to "DOM Practice " underlined. change its color to purple.
//create element h1
let heading=document.createElement('h1');

//adding in document
body.append(heading);

// add text
heading.innerText="DOM Practice";

// styling add
heading.style.textDecoration='underline';
heading.style.color='purple';

// 5. Create a p tag on the page and set its text to "Apna College Delta Practice", where Delta is bold.

// create a element 
let para1=document.createElement('p');

// add element in body
body.append(para1);

// add text 
para1.innerHTML="Apna College <b> Delta</b> Practice";
