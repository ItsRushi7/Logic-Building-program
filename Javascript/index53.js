function calculator(num1, num2, operator) {

    let ans = 0;

    switch (operator) {
        case '+':
            ans = num1 + num2;
            break;
        case '-':
            ans = num1 - num2;
            break;
        case '*':
            ans = num1 * num2;
            break;
        case '/':
            ans = num1 / num2;
            break;
        default:
            console.log('plasae enter the correct operstor');

    }
    return ans;
}
function main() {

    let value1 = 10;
    let value2 = 10;

    let operator = '*';
    let ans = 0;

    ans = calculator(value1, value2, operator);

    console.log(`Answere of the calulation ${ans}`);

}

main();