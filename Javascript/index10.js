function checkPerfect(num) {
    if (num < 0) {
        console.log("please enter the positive number");
    }

    let i = 0;
    let check = 0;

    for (i = 1; i <= (num / 2); i++) {

        if (num % i == 0) {

            check = check + i;
        }

        if (check > num) {
            break;  
        }
    }

    return (check == num) ? true : false;

}

function main() {
    let value = 7;
    let result = false;

    result = checkPerfect(value);

    if (result == true) {

        console.log(`${value} is the perfect number`);
    }

    else {
        console.log(`${value} is not perfect number`);
    }

}

main();