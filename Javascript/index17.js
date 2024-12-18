function countDigit(num) {
    
    if (num < 0) {
        console.log("please enter the positive number");
        return -1;
    }

    let digit = 0;
    let count = 0;

    while (num != 0) {

        digit = num % 10;
        count++;
        num = parseInt(num / 10);
    }
    
    return count;

}

function main() {
    let value = -1234;
    let ans = 0;

    ans = countDigit(value);

    console.log(`count of digit ${ans}`);
}

main();