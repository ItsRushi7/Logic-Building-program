function displayGread(num) {
    if (num >= 60) {
        console.log('A+');
    }
    else if (num < 60 && num >= 50) {
        console.log('B+');
    }
    else {
        console.log('C+');
    }
}
function calculateAvrage(num1, num2, num3) {
    let add = num1 + num2 + num3;

    let ans = (add / 3);

    return ans;
}

function main() {
    let value1 = 1,
        value2 = 9,
        value3 = 87;

    let ans = 0;
    ans = calculateAvrage(value1, value2, value3);

    displayGread(ans);

}
main();