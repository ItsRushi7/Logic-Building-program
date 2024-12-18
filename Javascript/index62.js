function dislapyMaxMin(arr) {

    let len = (arr.length - 1);
    let max = arr[0];
    let min = arr[0];

    for (let count = 0; count <= len; count++) {
        if (max < arr[count]) {
            max = arr[count];
        }
        if (min > arr[count]) {
            min = arr[count];
        }

    }

    return [max, min];
}

function main() {

    let arr = [10, 35, 85, 65, 93, 34];
    let ans = 0;

    ans = dislapyMaxMin(arr);

    console.log(`maxmimum number of array is ${ans[0]}`);
    console.log(`minimum number of array is ${ans[1]}`);
}
main();