function calculatePosNegArray(arr) {

    let len = arr.length - 1;
    let positve = [];
    let negetive = [];

    for (let i = 0; i <= len; i++) {
        if (arr[i] < 0) {
            negetive.push(arr[i]);
        }

        if (arr[i] >= 0) {
            positve.push(arr[i]);
        }
    }

    console.log(`pasitive numberin array is ${positve}`);
    console.log(`pasitive numberin array is ${negetive}`);

}

function main() {

    let arr = [-1, -2, 0, 3, 5, 6, -20]

    calculatePosNegArray(arr);
}

main();