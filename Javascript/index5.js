let checkEvenOdd = (num) => (num % 2 == 0) ? true : false;

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