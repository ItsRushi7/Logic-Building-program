function Display(num) {
    let i = 0;

    if (num < 0) {
        console.log("please enter the positive number");
    }

    for (i = 1; i <= num; i++) {
        console.log("hello");
    }
}

function main() {
    let value = -5;

    Display(value);
}
main()