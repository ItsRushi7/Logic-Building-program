function displayFactors(num) {
    if (num < 0) {
        console.log("please enter the positive number");
    }

    let i = 0;

    for (i = 1; i <= (num / 2); i++) {

        if (num % i == 0) {
            console.log(i);
        }
    }

}
function main() {
    let value = 8;

    displayFactors(value);
}

main();