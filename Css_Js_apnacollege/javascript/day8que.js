// q1. Square and sum the array elements using the arrow function and the find the average of the array.
let list=[1,2,3,4,5];
let squArr=list.map((el)=>{
    return el**2;
});
squArr.forEach((el)=>{
    console.log(el);
});
let sumArr=squArr.reduce((sqr,el)=>(sqr+el));
console.log("sum of array:",sumArr);

let avg=sumArr/list.length;
console.log("average of array:",avg);

//q 2. create a new array using the map function whose each element is equal the original element plus 5.
let list2=[1,2,3,4,5];
let newList=list2.map((ele)=>(ele+5));

newList.forEach((ele)=>{
    console.log(ele);
});

// q 3.Create a new aray whose elements are in uppercase of words present in the original array.
let str=["apple", "banana", "cherry"];
let newStr=str.map((ele)=>{
    return ele.toUpperCase();
});
for(let i=0;i<newStr.length;i++){
    console.log(newStr[i]);
}

// 4. Write a function called doubleAndArgs which accepts an array and a varialbe number of arguments. The function should return a new array with the original array values and all of the additional arguments doubled.

const doubleAndReturnArgs=(arr,...args)=>[
    ...arr,
    ...args.map((v)=>v*2),
];
doubleAndReturnArgs([1,2,3],4,5,6);
doubleAndReturnArgs([2],10,5);

// 5. Write a function called mergeObjects that accepts two objects and returns a new object which contains all the keys and values of the first object and second object.

const mergeObjects=(obj1,obj2)=>({...obj1,...obj2});
mergeObjects({a:1,b:2},{c:3,d:4});
console.log(mergeObjects({ a: 1, b: 2 }, { c: 3, d: 4 }));