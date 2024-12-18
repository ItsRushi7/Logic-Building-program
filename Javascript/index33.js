function dispalySwap(num1, num2)
{
    let temp = 0;

    temp = num1;
    num1 = num2;
    num2 = temp;

    console.log('After swap ',num1, num2);
}

function main() {
    let value1 = 4;
    let value2 = 3;

    dispalySwap(value1,value2);
}

main();