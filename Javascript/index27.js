function displayMarks(marks) {

    if (marks < 0)
    {
        console.log("you are enter the incorrect marks");
        return;
        
    }

    if (marks >= 91 && marks <= 100) {
        console.log("your grade is A+");
    }

    else if (marks >= 81 && marks <= 90) {
        console.log("your grade is B+");
    }

    else if (marks >= 71 && marks <= 80) {
        console.log("your grade is C+");
    }

    else if (marks >= 61 && marks <= 70) {
        console.log("your grade is D+");
    }

    else if (marks >= 35 && marks <= 60) {
        console.log("your grade is E+");
    }

    else {
        console.log("you are fail");
    }

}
function main() {

    let value = -25;

    displayMarks(value);

}
main();