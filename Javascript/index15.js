function displayDigit(num) {
    let digit = 0;

    if (num < 0) {
        console.log("please enter the positive number");
    }

    while (num > 0) {
        digit = num % 10;
        console.log(digit);
        num = parseInt(num / 10);
    }
}
function main() {
    let value = -1234;

    displayDigit(value);
}

main();