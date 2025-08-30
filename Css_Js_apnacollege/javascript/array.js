
// Array(Data Structure)
// let student1="aman";
// let student2="shradha";
// let student3="rajat";

// use of array
let student=["aman","shradha","rajat"];
let nums=[2,4,6,8];
let info=['aman',20,80.8];
let emp=[];

//array method push:-> add the data in last 
student.push("priya");
student.push("harsh");
console.log(student)

// pop >delete from the end & return it
console.log(student.pop())
console.log(student)

// unshift->add data to start
student.unshift("money");
student.unshift("rupees");
console.log(student)

//shift-> delete data from start index
student.shift();


//q. for the given start state of an array, change it to final form using methods.
let start=['january','july','march','august'];
start.shift();
start.unshift("july");
start[1]='june';
console.log(start)

//indexOf: returns index of something
let primary=['red','yellow','blue'];
console.log(primary.indexOf('yellow'));
console.log(primary.indexOf('green'));
console.log(primary.indexOf('Yellow'));

//includes:search for a value
console.log(primary.includes("red"))
console.log(primary.includes("green"))

//concatenate array
let primary1=['red','yellow','blue'];
let secondry=['orange','green','voilet']

console.log(primary1.concat(secondry));

// reverse an array
console.log(primary1.reverse());
// slice copies a portion of an array
primary1.slice();
primary1.slice(2);
primary1.slice(2,3);

//splice(start index,deleteCount,item)
let colors=['red','yellow','blue','orange','pink','white'];
console.log(colors.splice(4));
console.log(colors.splice(0,1));
console.log(colors.splice(0,1,"black","gray"))

//sort : sort an array
let colors1=['red','yellow','blue','orange','pink','white'];
console.log(colors1.sort)

//practice question
//for the given start of an array,change it to final form using splice.
let start=['january','july','march','august'];
// console.log(start.splice(0,1,"july",'june'));
console.log(start.splice(0,2,"july","june"))
// console.log(start.shift());
console.log(start)

// Return the index of the "javascript" from the given array, if it was reversed.
let lang=['c','c++','html','javascript','python','java','c#','sql'];
console.log(lang.reverse().indexOf('javascript'));


// array reference 
let arr=['a','b'];
let arrCopy=arr;
arrCopy.push('c');
console.log(arr==arrCopy);

//constant array
const arr4=[1,2,3,4]

// create a nested array to show the following tic-tic-toe game state.
let tic=[['x',null,'o'],[null,'x','null'],['o',null,'x']];