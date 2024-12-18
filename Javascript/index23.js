function checkEvenDigit(num) {
    if (num < 0) {
        console.log("please enter the positive number");
        return -1;
    }

    let digit = 0;

    while (num != 0) {

        digit = num % 10;
        if (digit % 2 == 0) {
            console.log(digit);
        }
        num = parseInt(num / 10);

    }

}

function main() {
    let value = 123456;

    checkEvenDigit(value);

}
main();