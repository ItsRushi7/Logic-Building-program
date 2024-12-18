function sumofDigit(num) {

    if (num < 0) {
        console.log("please enter the positive number");
        return -1;
    }

    let digit = 0;
    let sum = 0;

    while (num != 0) {

        digit = num % 10;
        sum = sum + digit;
        num = parseInt(num / 10);
    }

    return sum;

}

function main() {
    let value = -1234;
    let ans = 0;

    ans = sumofDigit(value);

    if (ans != -1) {

        console.log(`sum of digit ${ans}`);
    }
}

main();