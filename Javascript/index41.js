function checkNum(num) {
    if (num > 10) {
        console.log('This is greater than 10');
    }
    else if (num < 10) {
        console.log('this is less than 10')
    }
    else {
        console.log('this is equal');
    }
}

function main() {
    let value = 10;

    checkNum(value);

}
main();