function checkPosNeg(num) {
    if (num < 0) {
        return true;
    }
    else {

        return false;
    }
}
function main() {
    let value = -1;
    let ans = false;

    ans = checkPosNeg(value);

    if (ans == true) {
        console.log('This is negative number');

    }
    else {
        console.log('This is positive number');
    }
}
main();