function checkEvenOdd(num) {

    return (num % 2 == 0) ? true : false;
}

function main() {
    let value = 12;
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