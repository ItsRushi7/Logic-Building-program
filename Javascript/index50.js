function calculateAvrage(num) {
    let avg = 0;
    let sum = 0;

    for (let i = 0 ; i <= num; i++)
    {
        sum = sum + i;
    }

    avg = sum / num;

    return avg;
}
function main() {
    let value = 10;

    let ans = 0;

    ans = calculateAvrage(value);

    console.log(`avrage of number is ${ans}`);
}
main();