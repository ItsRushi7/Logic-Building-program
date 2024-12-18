function calculateAvrage(num) {
    if (num < 0) {
        console.log("please enter the positive number");
        return -1;
    }

    let digit = 0,
        count = 0,
        sum = 0;

    while (num != 0) {
        digit = num % 10;
        sum = sum + digit;
        count++;
        num = parseInt (num / 10);
    }

    let avg = 0;
    avg = sum / count;
    return avg;

}

function main() {

    let value = 1234;
    let ans = 0;

    ans = calculateAvrage(value);

    if (ans != -1) {

        console.log(`the average of digit is ${ans}`);

    }
}

main();