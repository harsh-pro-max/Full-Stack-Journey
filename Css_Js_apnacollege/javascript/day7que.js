// 1. write an arrow function named arrayAverage taht accepts an array of numbers and returns the average of those numbers.
const arrayAverage=(arr)=>{
    let sum=0;
    for(let i=0;i<arr.length;i++){
        sum=sum+arr[i];
    }
    let avg=sum/arr.length;
    return avg;
}
let arr=[5,2,3,5,6,4];
console.log(arrayAverage(arr));

// 2. Write an arrow function named isEven() taht takes a single number as argument and returns if it is even or not.
const isEven=(n)=>{
    if(n%2==0){
        return "even";
    }else{
        return "not a even number";
    }
}

console.log(isEven(77));

// 3. what is the output of the following code:
const object={
    message:"hello,World!",

    logMessage(){
        console.log(this.message);
    }
};
setTimeout(object.logMessage,1000);
//output is undefined
setTimeout(object.logMessage(),1000);
//print hello world

// 4. What is the output of the following code:

let length=4;
function callback(){
    console.log(this.length);
}
const object2={
    length:5,
    method(callback){
        callback();
    },
};

object2.method(callback,1,2);// extra argument error hoga 

