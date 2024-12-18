function calculateAdd(num1, num2) {
    let ans = 0;
    ans = num1 + num2;
    return ans;
}

function calculateSubstarction(num1, num2) {
    let ans = 0;
    ans = num1 - num2;
    return ans;
}

function calculateDivision(num1, num2) {
    let ans = 0;
    ans = num1 / num2;
    return ans;
}

function calculateMuiltiplication(num1, num2) {
    let ans = 0;
    ans = num1 * num2;
    return ans;
}

let addition = (num1,num2) => num1+num2;

let substraction  = (num1,num2) => num1-num2;

let  division = (num1,num2) => num1/num2;

let  muiltiplication = (num1,num2) => num1*num2;

function main() {
    let value1 = 10;
    let value2 = 20;

    let result = addition(value1,value2);
    console.log(`addition of two numbers are ${result}`)
}

main();