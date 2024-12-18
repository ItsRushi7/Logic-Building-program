function countfrequency(num, checkNum) {

    if (num < 0) {
        console.log("please enter the positive number");
        return -1;
    }

    let digit = 0;
    let count = 0;

    while (num != 0) {

        digit = num % 10;
        if (digit == checkNum) {
            count++;
        }
        num = parseInt(num / 10);
    }

    return count;

}

function main() {
    let value = 123848;
    let checkNum = 9;
    let ans = 0;

    ans = countfrequency(value, checkNum);

    console.log(`the freqency of digit is ${ans}`);;


}

main();