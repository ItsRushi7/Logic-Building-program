function checkMaxMin(num1, num2) {
    if (num1 > num2) {
        return true;
    }
    else {

        return false;
    }
}
function main() {
    let value1 = 11,
        value2 = 93;

    let ans = false;

    ans = checkMaxMin(value1, value2);

    if (ans == true) {
        console.log('The first number is gretar');

    }
    else {
        console.log('The second number is greater');
    }
}
main();