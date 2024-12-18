function display(num) {
    if (num < 0) {
        console.log("please enter the positive number");
    }

    let i = 1;

    while (i <= num) {

        console.log(i);
        i++;

    }

}
function main() {
    let value = 10;

    display(value);
}

main();