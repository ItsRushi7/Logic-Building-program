function checkPallendrome(num) {
    if (num < 0) {
        console.log("please enter the positive number");
        exit();
    }

    let digit = 0;
    let temp = num;
    let sum = "";

    while (num != 0) {

        digit = num % 10;
        sum = sum + digit;
        num = parseInt(num / 10);

    }

    console.log(sum);
    return (sum == temp) ? true : false;

}

function main() {
    let value = 12344321;
    let ans = false;

    ans = checkPallendrome(value);

    if (ans == true) {
        console.log("the number is pallendrome");
    }

    else {
        console.log("the number is not pallendrome");
    }
}
main();