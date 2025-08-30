// function definition
function hello(){
    console.log("hello harsh");
}
hello();
function printName(){
    console.log("Harsh Kushwaha")
}
function print1to5(){
    for(let i=1;i<=5;i++){
        console.log(i);
    }
}

function isAdult(){
    let age=18;
    if(age>=18){
        console.log("adult")
    }else{
        console.log("not adult")
    }
}
isAdult();
// 1.create a function that prints a poem.
function printPoem(){
    console.log("twincle twincle little start\n How I wonder what you are");
}
printPoem();

// 2. Create a funtion to roll a dice & always display the value of the dice(1 to 6).
function dice(){
    rand=Math.floor(Math.random()*6+1);
    console.log(rand);
}
dice();

// 3. Create a function to diside the toss result.
function Toss(){
    toss=Math.floor(Math.random()*2+1);
    if(toss==1){
        console.log("head");
    }
    else{
        console.log("tell");
    }
}
Toss();

//function with argument
function printInfo(name,age){
    console.log(`${name} age is ${age}`);
}

printInfo("harsh kushwaha",20);

function sum(a,b){
    console.log(a+b);
}
sum(45,25);

// create a function that gives us the average of 3 numbers.
function calAvg(a,b,c){
    console.log((a+b+c)/3);
}
calAvg(5,2,5);

// create a function that prints the mulitplication table of a number.
function printTable(num){
    for(let i=num;i<=10*num;i=i+num){
        console.log(i);
    }
}
printTable(5);

// create a function that returns the sum of numbers from 1 to n.
function sumOf1toN(N){
    sum=0;
    for(let i=1;i<=N;i++){
        sum=sum+i;
    }
    return sum;
}
console.log(sumOf1toN(10));

//create a function that returns the concatenation of all strings in an array.
function concatArray(arr){
    let newStr=[];
    for(let i=0;i<arr.length;i++){
        newStr+=arr[i];
    }
    return newStr;
}
let str=["harsh","prince","Kumar"];
console.log(concatArray(str));


// lexcul scope
function outerFunc(){
    let x=5;
    let y=6;
    function innerFunc(){
        console.log(x);
    }
    innerFunc();
}
// what will be the output?
let greet="hello";

function changeGreet(){
    let greet="namaste";
    console.log(greet);
    function innerGreen(){
        console.log(greet);
    }
}
console.log(greet);
changeGreet();

//function expression
let name="shradha";

//just like shradha store a function in a variable.
// nameless function

let sum2=function(a,b){
    return a+b;
}
sum2(5,2);

// Higher order function
//takes one or multiple functions as argumetns
function multipleGreet(func,n){
    for(let i=1; i<=n;i++){
        func();
    }
}
let greet2=function(){
    console.log("hello");
}
multipleGreet(greet2,2);

//higher order function return a function

function oddEvenTest(request){
    if(request=='odd'){
        return function(n){
            console.log(!(n%2==0))
        }
    }else if(request=='even'){
        return function(n){
            console.log(n%2==0)
        }
    }else{
        console.log("wong request");
    }
}

let even=oddEvenTest("even");
even(54);

// instance object method method defining in object
const calculator={
    num:55,
    add: function(a,b){
        return a+b;
    },
    sub: function(a,b){
        return a-b;
    },
    mul: function(a,b){
        return a*b;
    }
};
// use of add method
console.log(calculator.add(5,6));
//use of sub method
console.log(calculator.sub(56,2));
// use of instance member 
console.log(calculator.num);


// methods shorthand
const calculator2={
    add(a,b){
        return a+b;
    },
    sub(a,b){
        return a-b;
    }
};
