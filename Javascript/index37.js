function checkArmstrong(num) {
    if (num <= 0) {
        console.log("please enter the positive number");
    }

    let digit = 0,
        sum = 0;

    const TEMP = num;

    while (num != 0) 
        {
        digit = num % 10;
        console.log(digit);
        sum = sum + digit * digit * digit;
        num = parseInt(num / 10);
    }

    console.log(sum)
    if (TEMP == sum) {
        return true;
    }
    else {
        return false;
    }
}

function main() {
    let value = 153;
    let ans = false;

    ans = checkArmstrong(value);

    if (ans == true) {
        console.log("this is a armstrong number");

    }
    else {
        console.log("this is a not armstrong number");
    }
}

main();