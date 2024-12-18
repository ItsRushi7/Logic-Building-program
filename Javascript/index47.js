let calculateFactorial = (num) => {

    let fact = 1,
        count = 0;

    for (count = 1; count <= num; count++) {
        fact = fact * count;
    }

    return fact;
}
function main() {
    let value = 5;

    let ans = 0;

    ans = calculateFactorial(value);

    console.log(`factorial is ${ans}`);
}
main();