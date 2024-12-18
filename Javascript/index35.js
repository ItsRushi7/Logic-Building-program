let checkMax = (num1, num2, num3) => {

    // if (num1 > num2) {

    //     if (num1 > num3) {
    //         return num1;
    //     }
    //     else {
    //         return num3;
    //     }

    // }

    // else {

    //     if (num2 > num3) {
    //         return num2;
    //     }
    //     else {

    //         return num3;
    //     }
    // }

    if (num1 > num2) {
        return num1;
    }
    else if (num1 > num3) {
        return num1;
    }
    else if (num2 > num3) {
        return num2;
    }
    else {
        return num3;
    }
}

function main() {
    let value1 = 6;
    let value2 = 12;
    let value3 = 88;

    let ans = checkMax(value1, value2, value3);

    console.log(`max in betwen three number : ${ans}`);
}

main();