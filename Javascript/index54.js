function displayFactorial(num) {
    let fact = 1;

    for (let i = 1; i <= num; i++) {
        fact = fact * i;
        console.log(fact);
    }
}


function displayFabbio(num) {

    let a = 0;
    let b = 1;
    let temp = 0;

    for (let i = 0; i <= num; i++) {
        console.log(a);
        temp = a + b;
        a = b;
        b = temp;
    }
}


function displayPrime(num) {

    let flag = true;

    for (let i = 0; i < (num / 2); i++) {
        if (num / i == 0) {
            flag = false;
            break;
        }
    }

    if (flag == true) {
        console.log('This is a prime number');
    }

    else {
        console.log('This is not a prime number');
    }
}

function main() {

    let value = 5;

    displayFactorial(value);
    displayFabbio(value);
    displayPrime(value);

}

main();