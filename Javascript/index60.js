function additionArrayelement(arr, size) {

    let count = 0;
    let sum = 0;

    for (count = 0; count < size; count++) {
        sum = sum + arr[count];
    }

    return sum;
}

function main() {
    let arr = [];
    let size = 10;
    let ans = 0;

    for (let count = 0; count < size; count++) {
        arr[count] = count + 1;
    }

    ans = additionArrayelement(arr, size);

    console.log(`addition of array elements ${ans}`);
}

main();