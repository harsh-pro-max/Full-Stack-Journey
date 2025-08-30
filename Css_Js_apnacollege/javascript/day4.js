/*
// learning for loop
console.log("1");
console.log("2");
console.log("3");
console.log("4");
console.log("5");

// for loop
for(let i=1;i<=5;i++){
    console.log(i);
}
// print all odd numbers (1 to 15).
for(let i=1;i<=15;i=i+2){
    console.log(i)
}
// to backword printing
for(let i=15;i>=1;i--){
    console.log(i);
}

// Print all even numbers (2 to 10)
for(let i=1;i<=5;i++){
    console.log(i*2)
}
// print the multiplicaiton table for 5
for (let i=1;i<=10;i++){
    console.log(i*5)

}
// printing table of any number by user input .
let num=prompt("Write a number to print table:")
num=parseInt(num)
for(let i=num;i<=num*10;i=i+num){
    console.log(i);
}
// nasted for loop
for(let i=1; i<=3;i++){
    console.log(`outer loop ${i}`);
    for(let j=1;j<=3;j++){
        console.log(j);
    }
}
*/
// while loop programs
let i=1;
while (i<=5){
    console.log(i);
    i++;
}
// favorite movie guess
let favorite="avatar";
// while((guess!=favorate)&& (guess!='quit'))
while(true){
    let guess=prompt("Input favorite movie:")
    if(favorite===guess){
        console.log("congrats movie guess succesfully");
        break;
    }
    else{
        console.log("good try but not match");
    }
}

// loops with Arrays
let fruits=['mango','apple','guava','litchi','lemon','orange'];
for(let i=0;i<fruits.length;i++){
    console.log(i,fruits[i]);
}
for(let i=fruits.length-1;i>=0;i--){
    console.log(i,fruits[i]);
}

// arrays of arrays
let heroes=[['ironman','spiderman','thor','captain'],['superman','wonder woman','flash']];
for(let i=0;i<heroes.length;i++){
    console.log(`List #${i}`);
    for(let j=0;j<heroes[i].length;j++){
        console.log(heroes[i][j]);
    }
}

// for of loop
const array = ["a", "b", "c"];

for (const element of array) {
  console.log(element);
}

// Expected output: "a"
// Expected output: "b"
// Expected output: "c"


// nested for of loop
let heroes2=[['ironman','spiderman','thor','captain'],['superman','wonder woman','flash']];

for(list of heroes2){
    for(element of list){
        console.log(element);
    }
}