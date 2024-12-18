function displayFactorial(num) {
    if (num < 0) {
        console.log("please enter the positive number");
    }

    let i = 1;
    let fact = 1;

    while (i <= num) {

        fact = fact * i;

        i++;

    }
    return fact;

}
function main() {
    let value = 5;
    let ans = 0;

    ans = displayFactorial(value);

    console.log("factorial of ", ans);
}

main();