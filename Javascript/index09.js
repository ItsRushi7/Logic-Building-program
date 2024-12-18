function calucateFactors(num) {

    if (num < 0) {
        console.log("please enter the positive number");
    }

    let i = 0;
    let sum = 0;

    for (i = 1; i <= (num / 2); i++) {

        if (num % i == 0) {

            sum = sum * i;
        }
    }

    return sum;
}
function main() {
    let value = 8;
    let ans = 0;

    ans = calucateFactors(value);

    console.log(`Muiltiplication of factors is ${ans}`);
}

main();