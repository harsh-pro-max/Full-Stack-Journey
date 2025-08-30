
// use of this keyword
const student={
    name:"shradha",
    age:23,
    eng:93,
    math:95,
    phy:97,
    getAvg(){
        //my variable direclty not use like c++ so use in this keyword to use this
        // let avg=((eng+math+phy)/3);
        let avg=((this.eng+this.phy+this.math)/3);
        //console.log(avg);
        console.log(`${this.name} got avg marks =${avg}`);
    }
};

// try or catch statement

console.log("hellow harsh");
try{
    console.log(a);
}catch{
    console.log("error,a is not define!! ")
}

// arrow function
const sum =(a,b)=>{
    console.log(a+b);
}
const cube=(n)=>{
    return n**3;
}
const pow=(a,b)=>{
    return a**b;
}
// function with no argument arrow function use
const hello=()=>{
    console.log("hello harsh");
}

// implecit return in arrow funciton
const mul=(a,b)=>(
    a*b
);

//use of setTimeout function
console.log("hi there!");

// setTimeout(()=>{
//     console.log("Harsh kushwaha");
// },8000);
// console.log("Welcome to");

//setInterval method very dengrous

// let id=setInterval(()=>{
//     console.log("harsh kushwah");

// },4000);
// clearInterval(id);
// console.log(id);

// let id2=setInterval(()=>{
//     console.log("hello world");

// },4000);
// clearInterval(id2);

// console.log(id2);


// this with Arrow Function
const student2={
    name:"harsh",
    marks:80,
    prop:this,//global scope
    getName:function(){
        return this.name;
    },
    getMarks:()=>{
        console.log(this);//parent's scope
        return this.marks;
    },
    getInfo1:function(){
        setTimeout(()=>{
            console.log(this);//student
        },2000);
    },
    getInfo2:function(){
        setTimeout(function() {
            console.log(this);//window
        },2000);
    },
}

// practice question
//write an arrow function that returns the square of a number 'n'.

const sqr=(n)=>{
    return n**2;
}

// write a function that prints "hello world" 5 times at intervals of 2s each.
let id=setInterval(() => {
    console.log("Hello World");
},2000);
setTimeout(()=>{
    clearTimeout(id);
    console.log("clear interval ran")
},10000);

