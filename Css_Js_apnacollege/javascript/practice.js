// 1. Create a number variable num with some value.Now,print "good" if the number is divisible by 10 and print "bad" if it is not.
let number=79;
if (number%10==0){
    console.log("good");
}
else{
    console.log("bad");
}

//2. Take the user's name & age as input using prompts.then return back the following statment to the user as an alert (by substituting their name & age);
// name is age year old.
let fullName=prompt("enter your name:");
let age=prompt("enter your age:");
let msg=`${fullName} is ${age} year old`;
alert(msg)

// 3. Write a switch statement to print the months in a quarter. 
// Months in Quarter 1: January, February, March
// Months in Quarter 2: April,May,June
// Months in Quarter 3. July,August,September
// Months in Quarter 4. October, November, December
let quarter=4;
switch(quarter){
    case 1:
        console.log("January, February, March")
        break;
    case 2:
        console.log("April,May,June")
        break;
    case 3:
        console.log("July,August,September")
        break;
    case 4:
        console.log("October, November, December")
        break;
    default:
        console.log("not quarter availabe")
}

// 4. A string is a golden string if it starts with the character 'A' or 'a' and has a total length greater than 5.For a given string print if it is golden or not.
let word="Apple";
if((word[0]=='a'|| word[0]=='A') && word.length){
    console.log("Golden word");
}
else{
    console.log("Not Golden word!!!")
}

// 5. Write a program to find the largest of 3 numbers
let a=757
let b=23
let c=2343
if(a>b && a>c){
    console.log("a is grater");
}
else if(b>a && b>c){
    console.log("b is grater")
}
else{
    console.log("c is grater")
}
// 6. Write a program to check if 2 numbers have the same last diit.Eg. 32 and 47852 have the same last digit 
let num1=43234;
let num2=3342;
if (num1%10===num2%10){
    if(num1%100===num2%100){
        console.log("same digits");
    }
    else{
        console.log("first digit are same")
    }
}else{
    console.log("not same first digit")
}