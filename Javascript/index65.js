function additionArrayMatrix(arr) {

    let sum = 0;

    for (let i = 0; i < 2; i++) {
        for (let j = 0; j < 3; j++) {
            sum = sum + arr[i][j];
        }
    }

    return sum;

}

function main() {
    let arr = [[2, 3, 4], [2, 0, -1]];
    let ans = 0;

    ans = additionArrayMatrix(arr);

    console.log(`addition of matrix is ${ans}`);
}
main();