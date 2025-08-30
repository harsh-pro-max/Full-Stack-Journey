// 1. Write a JS program to delete all occurrences of element 'num' in a given array. 
let arr=[1,2,3,4,5,6,2,3];
// arr=[1,3,4,5,6,3];
let num=2;
for(let i=0;i<arr.length;i++){
    if(arr[i]==num){
        arr.splice(i,1);
    }
}
for(let i=0;i<arr.length;i++){
    console.log(arr[i]);
}

//2. Write a JS program to find the no of digits in a number.
// example if number = 287152,count =6;
let number=287152;
let count=0;
while(number!=0){
    count++;
    number=Math.floor(number/10);
}
console.log(count);

//3. Write a JS program to find the sum of digits in a number.
// example: if number=287152, sum=25;
let sum=0;
let copy=287152;
while(copy!=0){
    mod=copy%10;
    sum=sum+mod;
    copy=Math.floor(copy/10);
}
console.log("sum of numbers digits is:",sum);

// 4. Print the factorial of a number n.[Factorial of a number n is product of all positive integers less than or equal to a given postive integer and denoted by that integer.]
let n=7;
let fact=1;
for(let i=1;i<=n;i++){
    fact=fact*i;
}
console.log("factorial is:",fact);

// 5.Find the largest number in an array with only positive numbers.
let maxArr=[85,23,62,12,73,72,932,223,453];
let max=0;
for(let i=0;i<maxArr.length;i++){
    if(maxArr[i]>max){
        max=maxArr[i];
    }
}
console.log("in array maximum value is:",max);

