// string methord 
// tring method
const greeting = "   Hello world!   ";

console.log(greeting);
// Expected output: "   Hello world!   ";

console.log(greeting.trim());
// Expected output: "Hello world!";

const password=prompt("Enter a password");
const newPass=password.trim();
console.log(newPass);


// toUpperCase 
const sentence = "The quick brown fox jumps over the lazy dog.";

console.log(sentence.toUpperCase());
// Expected output: "THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG."

// to lowercase
const sentence1 = "The quick brown fox jumps over the lazy dog.";

console.log(sentence1.toLowerCase());
// Expected output: "the quick brown fox jumps over the lazy dog."

// method indexOf()
let msg="ILoveCoding"
console.log(msg.indexOf("Love"))

console.log(msg.indexOf("j"))

console.log(msg.indexOf("o"))

// slice method str.slice(startidx,endidx)
let msg2="ILoveCoding"
console.log(msg.slice(1,5))
// last index exclude

// replace method
let msg3="IDoCoding"
console.log(msg.replace("Do","Love"))

// repeat method
let msg4='Mango';
console.log(msg4.repeat(3))

// practice question
/* for the give string: trim it & convert it to uppercase. */
let msg5=' help!  ';
console.log(msg5.trim().toUpperCase)

/* for the string-> let name="ApnaCollege",predict the output for following: name.slice(4,9) name.indexOf("na") name.replace("Apna","Our") */
let name1="ApnaCollege";
console.log(name1.slice(4,9));
console.log(name1.indexOf("na"));
console.log(name1.replace("Apna","Our"));
//Colle
//2
//OurCollege
// Separate the "College" part in above string & replace 'I' with 't' in it.
console.log(name1.slice(4));
console.log(name1.replace('l','t'))
