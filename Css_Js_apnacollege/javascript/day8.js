// array method forEach
let arr=[1,2,3,4,5];
let print=function(el){
    console.log(el);
}
arr.forEach(print);

// second method is
arr.forEach(function(el){
    console.log(el);
})

// use forEach loop using forEach loop
arr.forEach((el)=>{
    console.log(el)
});

// forEach loop for object
let obj=[
    {
        name:"harsh",
        marks:80
    },
    {
        name:"prince",
        marks:90
    },
    {
        name:"aman",
        marks:95
    }
];

let gpa=obj.map((el)=>{
    return el.marks/10;
});
obj.forEach((student)=>{
    console.log(student);
});
// array map method
let num=[1,2,3,4];
let double=num.map(
    function(el){
        return el**2;
    }
);
double.forEach((el)=>{
    console.log(el);
});

// array filter method
let nums=[2,4,1,5,6,2,7,8,9];
// let even = nums.filter((num)=>(num%2==0));
let even=nums.filter((el)=>{
    return el<5;
});

// output: 2,4,6,2,8,

even.forEach((el)=>{
    console.log(el);
})

// array Every method
let every=[4,2,52,5];
let res2=every.every((el)=>{
    return el%2==0;
});

let every2=[2,4,6];
let res=every2.every((el)=>{
    return el%2==0;
});


// reduce method array
let red=[1,2,3,4,5];
let res3=red.reduce((res,el)=>(res+el));
console.log(res3);
/*
0+1=res:1
1+2=res:3
3+3=res:6
6+4=res:10
10+5;res:15
return 15

*/

// more question of array method
// finding Maximum in an array
let arrayMax=[2,3,5,2,343,22,1,2,53,355];
let result=arrayMax.reduce((max,el)=>{
    if(el>max){
        return el;
    }else{
        return max;
    }
});
console.log(result);

// Check if all numbers in our array are mulitples of 10 or not.
let arrMul=[10,200,40];
let check=arrMul.every((el)=>(el%10==0));
console.log(check);

// Create a function to find the min number in an array.
let minArr=[4,-2,1,52,423,12,21];
let min=minArr.reduce((min , el)=>{
    if(el<min){
        return el;
    }
    else{
        return min;
    }
});

console.log(min);

// default parameter
function sum(a,b=3){
    return a+b;
}
console.log(sum(a));
//output:5
//if not assign default parameter b so mendatary to pass 2 value .

// spread method
// console.log(..."harshkushwaha");

let spreadMin=[43,1,2,42,3,4,32,1,3];
console.log(Math.min(...spreadMin));

let odd=[1,3,5,7];
let even2=[2,4,6,8];

let num3=[...odd,...even];
for(let i=0;i<num3.length;i++){
    console.log(num3[i]);
}

// array spread() method with object literals.

// const data={
//     email:"ironman@gmail.com",
//     password:"abcd"
// };

// let dataCopy={...data};

//array rest function

function sum3(...args){
    for(let i=0;i<args.length;i++){
        console.log("you gave us:",args[i]);
    }
}

function min5(a,b,c,d){
    console.log(arguments);
}

// destructuring
// let names=["tony","bruce","steve","peter"];
// let [winner,runnerup,...others]=names;
// console.log(winner,runnerup);

// destructuring in object 
const student3={
    name:"karan",
    age:20,
    class:9,
    subjects:["hindi","english","math","science"],
    username:"karana@123",
    password:"abcd",
};
let {username,password}=student3;