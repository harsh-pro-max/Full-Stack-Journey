// 1) Page par ek ul banao aur uske andar 3 li add karo: "Apple", "Banana", "Cherry".
let body=document.querySelector('body');
const ul = document.createElement('ul');
ul.innerHTML = `
  <li>Apple</li>
  <li>Banana</li>
  <li>Cherry</li>
`;
document.body.append(ul);

// 2) Kisi existing p tag ka textContent ko “Updated via JS!” karo aur uska color green set karo.
// Use the pre-existing paragraph from the HTML: <p id="existing-paragraph">
const existingP = document.getElementById('existing-paragraph');
if (existingP) {
  existingP.textContent = 'Updated via JS!';
  existingP.style.color = 'green';
} else {
  // Fallback if not present
  const p = document.createElement('p');
  p.textContent = 'Updated via JS!';
  p.style.color = 'green';
  document.body.append(p);
}

// 3) Body ke end me ek hr tag add karo (createElement + append).
const hr = document.createElement('hr');
document.body.append(hr);

//Selectors & Styling

//4) Page par sabhi p tags ko querySelectorAll se select karke unka color gray karo.
let SelectAllPara=document.querySelectorAll('p');
for(let i=0;i<SelectAllPara.length;i++){
    SelectAllPara[i].style.color='gray';
}
//5)Sabhi buttons ka background yellow aur border radius 8px karo.

let allBtn=document.querySelectorAll('button');
for(let i=0;i<allBtn.length;i++){
    allBtn[i].style.backgroundColor='yellow';
    allBtn[i].style.borderRadius='8px';
}
//6) Jis element ka id="title" hai, uska fontSize 32px aur text ko uppercase karo.

let title=document.getElementById("title");
title.style.fontSize='2rem';
title.innerText=title.innerText.toUpperCase();

//Events (Interactive)

// Ek button banao: click par body ka background random color me change ho.
// 1) Button create + label
const btn = document.createElement('button');
btn.textContent = 'ChangeColor';
body.append(btn);

// 2) Random integer helper (0..255)
const rand255 = () => Math.floor(Math.random() * 256);

// 3) Random RGB color string
const randomRGB = () => `rgb(${rand255()}, ${rand255()}, ${rand255()})`;

// 4) Click par body background change
btn.addEventListener('click', () => {
  const color = randomRGB();
  document.body.style.backgroundColor = color;
  // Optional: button text me current color dikhana
  btn.textContent = `ChangeColor (${color})`;
});



// Ek input + button banao: button click par input ka value ek nayi li me ul ke andar add ho.



// Ek h1 banao: uspe mouseenter par color blue aur mouseleave par color black ho.

// Attributes & Classes

// Ek image element banao, src set karo, width=200px karo, alt set karo “Sample Image”.
// let img=document.createElement('img');
// body.append(img);
// img.src='spider_man.jpg';
// img.style.width='200px';
// img.alt="Sample Image";


// Ek div par 2 classes add karo: "card" aur "rounded". Fir "rounded" class ko remove karo.
//create 2 divs
let div1=document.createElement('div')

// append in body
body.append(div1);

// add class in dives
div1.classList.add("card");
div1.classList.add("rounded");
// remove rounded class
div1.classList.remove("rounded");


// Ek button par data-action="delete" attribute add karo. Click hone par console me “Delete clicked!” print karo.
    const deleteBtn = document.createElement('button');
    deleteBtn.textContent = 'Delete';
    deleteBtn.setAttribute('data-action', 'delete');
    deleteBtn.style.cssText = 'padding:8px 12px; margin:8px; cursor:pointer;';

    body.append(deleteBtn);

    deleteBtn.addEventListener('click', () => {
      console.log('Delete clicked!');
    });
// Ek list me 5 items ho. 3rd li ko find karke uska background lightpink karo.

// const list = document.getElementById('five-list'); // no '#'
// if (list && list.children[1]) {
//   list.children[1].style.background = 'lightpink';
// }

const third = document.querySelector('#five-list li:nth-child(3)');
if (third) third.style.background = 'lightpink';



// Kisi container div ke firstChild aur lastChild ko console me log karo.

const container = document.querySelector('#buttons-bank');
if (container) {
  console.log('firstChild:', container.firstElementChild);
  console.log('lastChild:', container.lastElementChild);
}



// Ek nested structure (div>ul>li*3) banao aur parentElement / nextElementSibling ka use karke second li se third li tak navigate karke uska text bold karo.
// Create container div and its nested list
// Create container div and its nested list
document.addEventListener('DOMContentLoaded', () => {
  // 1) Create container and list
  const creDiv = document.createElement('div');
  creDiv.id = 'newList';
  creDiv.innerHTML = `
    <ul style="padding:8px; border:1px solid #ddd; list-style:disc; margin-left:20px;">
      <li>harsh</li>
      <li>kushwaha</li>
      <li>amerandra</li>
      <li>bahubali</li>
    </ul>
  `;

  // 2) Mount safely (use #traversal if present, else body)
  const mount = document.getElementById('traversal') || document.body;
  mount.append(creDiv);

  // 3) Select second li and make third bold
  const secLi = document.querySelector('#newList ul li:nth-child(2)');
  if (secLi?.nextElementSibling) {
    secLi.nextElementSibling.style.fontWeight = 'bold';
  }

  // Optional: visual cue for parentElement
  if (secLi) {
    secLi.parentElement.style.border = '1px dashed #ccc';
  }
});


// Create/Remove/Replace

// Ek paragraph banao aur 2s baad usse remove() kar do.

// Ek existing h2 ko nayi h2 se replace karo jiska text “Replaced Heading” ho.

// Ek div ke andar pehle prepend() se “Start” wala p aur end me append() se “End” wala p add karo.

// Forms & Validation

// Ek simple login form (username, password, submit button) JS se banao. Submit par:

// Agar fields empty ho to form submit na ho aur red error message show ho.

// Sahi hone par “Logged in!” green message show ho.

// Password input par input event par live character count dikhayo (e.g., “Chars: 5”).

// Checkbox “I agree” ke bina submit button disabled rakho; tick karte hi enable ho jaye




