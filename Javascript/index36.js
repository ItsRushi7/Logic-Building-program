function checkPosNeg(num) {

    return num < 0 ? true : false;
}

function main() {
    let value = -12;
    let ans = false;

    ans = checkPosNeg(value);

    if (ans == true) {
        console.log("this is negative number ");
    }
    else {
        console.log("this is positive number ");
    }

}

main();