let todo = [];

while (true) {
    let req = prompt("Please enter your request (add, list, delete, quit):");

    if (req === "quit") {
        console.log("Quitting app successfully");
        break;
    }

    if(req==="list"){
    console.log("----------------");
    for(let i = 0; i < todo.length; i++){
        console.log(`${i}: ${todo[i]}`);
    }
    console.log("----------------");
    } else if (req === "add") {
        let task = prompt("Please enter the task you want to add:");
        todo.push(task);
        console.log("Task added");
    } else if (req === "delete") {
        let index = parseInt(prompt("Enter the index of the task to delete:"));
        if (!isNaN(index) && index >= 0 && index < todo.length) {
            todo.splice(index, 1);
            console.log("Task deleted");
        } else {
            console.log("Invalid index");
        }
    } else {
        console.log("Unknown command. Please try again.");
    }
}

