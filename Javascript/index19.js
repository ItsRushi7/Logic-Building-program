function checkDigit(num, checkNum) {

    if (num < 0) {
        console.log("please enter the positive number");
        return -1;
    }

    let digit = 0;

    while (num != 0) {

        digit = num % 10;
        if (digit == checkNum) {
            break;
        }
        num = parseInt(num / 10);
    }

    if (digit == checkNum) {
        return true;
    }

    return false;

}

function main() {
    let value = 1234;
    let checkNum = 8;
    let ans = false;

    ans = checkDigit(value, checkNum);


    if (ans == true) {

        console.log(`the number is present in digit`);
    }
    else {
        console.log(`the number is not present in digit`);
    }
}

main();