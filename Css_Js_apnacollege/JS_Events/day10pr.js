// 1. try out the follwing events in Event Listner on your own: mouseout ,keypress , Scroll, load

// load event
let para=document.querySelector(".pageLoad");

window.addEventListener ("load",()=>{
    para.textContent="Page Loaded!!";
});

// keypress event
let countLen=document.querySelector(".countLen");
let para2=document.querySelector(".printLen");

// countLen.addEventListener("keypress", () => {
  // Update after the key is applied
//   setTimeout(() => {
//     const val = countLen.value;
//     para2.textContent = `Welcome ${val}, length is ${val.length}`;
//   }, 0);
// });

countLen.addEventListener("input", () => {
    const val = countLen.value;
    const len = val.length;
    para2.textContent = `Welcome ${val}, length is ${len}`;
  });

//mouseout,mosueover
let box=document.querySelector("#box");

box.addEventListener("mouseover",()=>{
    box.textContent="Mouse Over!!";
    box.style.backgroundColor="yellow";
    box.style.color="gray";
    box.style.width="250px";
    box.style.height="250px";
});

box.addEventListener("mouseout",()=>{
    box.textContent="Mouse Out!!";
    box.style.backgroundColor="purple"; 
})

//Scroll event


// 2. Create a button on the page using JavaScript. Add an event listener to the button that changes the button's color to gteen when it is clicked.

let btn=document.querySelector(".first");

btn.addEventListener("click",function(){
    btn.style.backgroundColor="green";
});

/*3.Qs3. Create an input element on the page with a placeholder ”enter your name” and an
H2 heading on the page inside HTML.
The purpose of this input element is to enter a user’s name so it should only input
letters from a-z, A-Z and space (all other characters should not be detected).
Whenever the user inputs their name, their input should be dynamically visible inside
the heading.
[Please note that no other character apart from the allowed characters should be
visible in the heading]*/

let userName=document.querySelector(".name");
let h2=document.querySelector(".namePrint");

userName.addEventListener("change",function(){
    h2.textContent=editInput();
});

function editInput() {
  const str = String(userName.value || "");
  let copy = "";
  for (let i = 0; i < str.length; i++) {
    const ch = str[i];
    if (
      (ch >= 'a' && ch <= 'z') ||
      (ch >= 'A' && ch <= 'Z') ||
      ch === ' '
    ) {
      copy += ch;
    }
  }
  return copy;
}




