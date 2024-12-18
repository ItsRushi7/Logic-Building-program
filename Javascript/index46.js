
let calculateSumofDigit = (num) => {
    let sum = 0;
    let count = 0;

    for (count = 1; count <= num; count++) {
        sum = sum + count;
    }

    return sum;

}
function main() {
    let value = 10;
    let ans = 0;

    ans = calculateSumofDigit(value);

    console.log(`sum of n number is ${ans}`);

}
main();