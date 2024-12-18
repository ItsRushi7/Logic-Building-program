function checkPrime(num) {
    if (num < 0) {
        console.log("please enter the positive number");
    }

    let flag = true;

    for (let i = 2; i <= (num / 2); i++) {

        if (num % 2 == 0) {
            flag = false;
            break;
        }
    }

    return (flag == true) ? true : false;

}


function main() {

    let value = 10;
    let ans = false;

    ans = checkPrime(value);

    if (ans == true) {

        console.log("It is a prime number ");
    }

    else {
        console.log("It is not a prime number ");
    }
}
main();