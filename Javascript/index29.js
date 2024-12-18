function displayMarks(marks) {

    if (marks < 0) {
        console.log("you are enter the incorrect marks");
        return;

    }

    switch (true) 
    {
        case marks >= 91 && marks <= 100:
            console.log("your grade is A+");
            break;

        case (marks >= 81 && marks <= 90):
            console.log("your grade is B+");
            break;

        case (marks >= 71 && marks <= 80):
            console.log("your grade is C+");
            break;

        case (marks >= 61 && marks <= 70):
            console.log("your grade is D+");
            break;

        case (marks >= 35 && marks <= 60):
            console.log("your grade is E+");
            break;

        // default:
        //     console.log("you are fail");
    }

}


function main() {

    let value = 95;

    displayMarks(value);

}

main();