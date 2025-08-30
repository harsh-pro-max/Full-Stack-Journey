// Conditional Statments
console.log("before my if statement");
let age=23;
if(age>=18){
    console.log("you can vote");
    console.log("you can drive");
}
if(age<18){
    console.log("you cannot vote")
}

console.log("after  my if statement");

// Create a traffic light system that shows what to do based on color.
// red /yellow/ green
let color="yellow";
if(color=="red"){
    console.log("Stop!")
}
if(color=="yellow"){
    console.log("Slow Down")
}
if(color=="green"){
    console.log("Go")
}
// use of if-else statement
// write a program to check your eligible for driving licence or not
let dage=17;
if (dage>=18){
    console.log("you are elible of driving licence");
}
else{
    console.log(`you are eligible in  ${18-dage} years `)
}
// use of else if statement
// calculate grading system . marks 85 a grade,70 b grade , 60 c grade , 45 d grade .or fail.
let marks=45;
if(marks>85){
    console.log("A grade");
}
else if(marks>70){
    console.log("B grade");
}
else if(marks>60){
    console.log("C grade");
}
else if(marks>=45){
    console.log("D grade")
}
else{
    console.log("Fail!!!")
}
// question Create a system to calculate popcorn prices based on the size customer asked for:
/*  if size is XL,price is Rs.250
    if size is 'L',price is Rs.200
    if size is 'M',price is Rs.100
    if size is 'S',price is Rs.50  */

let size="XL";
if(size==="L"){
    console.log("Popcorn price is Rs.250")
}
else if(size==="L"){
    console.log("Popcorn price is Rs.200")
}
else if(size ==="M"){
    console.log("Popcorn price is Rs.100")
}
else if(size ==="S"){
    console.log("Popcorn price is Rs.50")
}
else{
    console.log("Popcorn not available.")
}
// practice qs.
// A "good string" is a string that starts with the letter 'a' & length>3.write a program to find if a string is good or not.
let str="pineapple";
let len=str.length;
if(str[0]==='a' && len>3){
    console.log("Good string");
}
else{
    console.log("not good string")
}
// use of switch statment 
// trafic light question red yellow green automate .
let bulb="red";
switch(bulb){
    case "red":
        console.log("stop!")
        break;
    case "yellow":
        console.log("slow down guies")
        break;
    case "green":
        console.log("go guies")
        break;
    default:
        console.log("Broken Light!!")
}
// use switch statement to print the day of the week using a number variable 'day' with values 1 to 7.
let day=1;
switch(day){
    case 1:
        console.log("Monday")
        break;
    case 2:
        console.log("Tuesday")
        break;
    case 3:
        console.log("Wednesday")
        break;
    case 4:
        console.log("Thursday")
        break;
    case 5:
        console.log("Friday")
        break;
    case 6:
        console.log("Satarday")
        break;
    case 7:
        console.log("Sunday")
    default:
        console.log("Wrong day")
}
