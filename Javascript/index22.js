function checkEvenDigit(num) {
    if (num < 0) {
        console.log("please enter the positive number");
        return -1;
    }

    let digit = 0;
    let count = 0;

    while (num != 0) {
        
        digit = num % 10;
        if (digit % 2 == 0){
            count++;
        }
        num = parseInt(num / 10);

    }

    return count;
}

function main() {
    let value = 123456;
    let ans = 0;

    ans = checkEvenDigit(value);

    if (ans != -1) {
        console.log(`the even number in digit are ${ans}`);
    }
}
main();