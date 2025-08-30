/*// Guessing Game creating
//User enters a max nuber & then tries to guess a random generated number between 1 to max.
let max=prompt("Enter the Maximum number:");
let random=Math.floor(Math.random()*max+1);
let guess=prompt("guess the number:")
count=0;
while(true){
    count++;
    if(guess=="exit"){
        console.log("exit the game thanks for playing!!!");
        break;
    }
    if(guess==random){
        console.log(`congrats,guess the number succefully atempts  #${count} generated number is(${random}) thanku for playing game!!!`)
        break;
    }
    else{
        if(guess>random){
           guess= prompt("your guess is grater then generated number,please try again")
        }else{
            guess=prompt("your guess is less then, generated number,please try again ")
        }
    }
}*/

// practice questions
//1. Create a program that generates a random number representing a dice roll. [the number should be between 1 and 6.]

let dice=Math.floor(Math.random()*6+1);
console.log(dice);

//2. Create an object representing a car that stores the following properties for the car: name model,color.print the car's name.
const car={
    name:"Audi",
    model:"a17",
    color:"black"
}
console.log(car.name);

// 3. Create an object Person with their name, age and city. Edit their city's original value to change it to "New York". Add a new property country and set it to the United States.
const Person={
    name:"harsh",
    age:20,
    city:"bhabua"
};
Person.city="New York";
Person.country="United States";

