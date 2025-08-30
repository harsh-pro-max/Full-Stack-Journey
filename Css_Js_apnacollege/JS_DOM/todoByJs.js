let btn = document.querySelector("button");
let ul = document.querySelector("ul");
let inp = document.querySelector("input");

btn.addEventListener("click", function() {

    // agar input khali hai to return karo
    if (inp.value.trim() === "") {
        alert("Please enter a task first!"); // ya koi message
        return;
    }

    // add elements in list
    let item = document.createElement("li");
    item.innerText = inp.value;


    // delete elements in a list
    let delButton = document.createElement("button");
    delButton.innerText = "Delete";
    delButton.classList.add("delete");


    item.appendChild(delButton);
    ul.appendChild(item);

    inp.value = "";

    // yaha add karna hoga event listener har naye button ke liye
    // delButton.addEventListener("click", function() {
    //     let par = this.parentElement; 
    //     console.log(par);
    //     par.remove();
    // });
});
// event Delegation 
ul.addEventListener("click",function(event){
    if(event.target.nodeName=="BUTTON"){
        let listItem=event.target.parentElement;
        listItem.remove();
        console.log("deleted");
    }
});




// ul.addEventListener("click", function(e) {
//     if (e.target.classList.contains("delete")) {
//         let par = e.target.parentElement;
//         console.log(par);
//         par.remove();
//     }
// });

