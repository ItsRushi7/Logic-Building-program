function checkEvenOdd(num) {
    if (num % 2 == 0) {

        return true;
    }

    return false;
}

function main() {
    let value = 13;
    let ans = false;

    ans = checkEvenOdd(value);

    if (ans == true) {
        console.log("this is even number ");
    }
    else {
        console.log("this is odd number ");
    }

}

main();