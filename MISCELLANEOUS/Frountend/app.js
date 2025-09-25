// let arr = [1,2,3];
// arr.sayHello = ()=>{
//     console.log("hello!, i am arr");
// };

// factory function 
// function PersonMaker(name,age){
//     const person={
//         name:name,
//         age:age,
//         talk(){
//             console.log(`hi, my name is ${this.name}`);
//         }
//     }
//     return person;
// }

// Constructors
// function Persion(name,age){
//     this.name = name;
//     this.age=age;
// }

// Persion.prototype.talk=function(){
//     console.log(`Hi,my name is ${this.name}`);
// }

// let p1 = PersonMaker("ADAM",25);
// let p2 = PersonMaker("eve", 25);
// // parameters constructor use 
// let p3= new Persion("adam",24);
// let p4= new Persion("eve",42);

// classess : classess are a template for creating objects
class Person {
    constructor(name,age){
        this.name = name;
        this.age = age;
    }
    talk (){
        console.log(`Hi, my name is ${this.name}`);
    }
}
let p5=new Person("adam",40);
let p6= new Person("harsh",20);

class person{
    constructor(name,age){
        console.log("person class constructor")
        this.name=name;
        this.age=age;
    }
    talk(){
        console.log(`HI, I am ${this.name}`);
    }
}
class student extends person{
    constructor(name,age,marks){
        console.log("student class constructor");
        super(name,age);// parent class constructor is being called
        this.marks=marks;
    }
}
class teacher extends person {
    constructor(name,age,subject){
        console.log("teacher class constructor");
        super(name,age);//parent class constructor is being called 
        this.subject = subject;
    }
}

// inheritance 
class Student {
    constructor(name,age,marks){
        this.name=name;
        this.age=age;
        this.marks=marks;
    }
    talk(){
        console.log(`Hi, I am ${this.name}`);
    }
}

let stu1 = new Student("harsh",25,94);

class Teacher {
    constructor(name,age,subject){
        this.name = name;
        this.age=age;
        this.subject=subject;
    }
    talk(){
        console.log(`Hi, I am ${this.name}`);
    }
}