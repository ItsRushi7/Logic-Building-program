function displaySwap(num1,num2)
{

    let temp = 0;

    temp = num1;
    num1 = num2;
    num2 = temp;

    console.log(num1,num2);
}

function main() {
    let value1 = 4;
    let value2 = 8;

    displaySwap(value1, value2);
}
main();