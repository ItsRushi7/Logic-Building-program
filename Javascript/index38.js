function calculateAvrage(num1, num2, num3) {
    let ans = 0;

    let avg = 0;

    ans = num1 + num2 + num3;

    avg = (ans / 3);

    return avg;

}

function main() {
    let value1 = 1,
        value2 = 2,
        value3 = 3;

    let ans = 0;

    ans = calculateAvrage(value1, value2, value3);

    console.log(`avarage of marks ${ans}`);
}
main();