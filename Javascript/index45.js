function displayOdd(num) {
    for (let i = 1; i <= num; i++) {
        if (i % 2 == 0) continue;

        else {
            console.log(i);
        }

    }
}
function main() {
    let value = 10;

    displayOdd(value);
}
main();