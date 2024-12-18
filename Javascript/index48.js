function displayfibonacci(num) {
    let a = 0,
        b = 1,
        c = 0;

    for (let i = 0; i <= num; i++) {
        console.log(a);
        c = a + b;
        a = b;
        b = c;
    }

}

function main() {
    let value = 10;

    displayfibonacci(value);
}
main();



