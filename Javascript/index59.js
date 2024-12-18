function arrayRevers(size, arr) {
    let count = 0;

    for (count = 0; count < size; count++) {
        arr[count] = count + 1;
    }

    size = arr.length - 1;

    for (count = size; count >= 0; count--) {
        console.log(arr[count]);
    }
}

function main() {

    let size = 5;
    let arr = [];

    arrayRevers(size, arr);
}
main();