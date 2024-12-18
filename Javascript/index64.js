function arrayAscending(arr) {

    arr.sort((a, b) => a - b);

    return arr;
}

function arraydecending(arr) {

    arr.reverse();

    return arr;
}
function main() {

    let arr = [78, 23, 96, 54, 48, 3];
    let ascending = [];
    let decending = [];

    ascending = arrayAscending(arr);
    console.log(`Array in ascending order ${ascending}`);


    decending = arraydecending(ascending);
    console.log(`Array in decending order ${decending}`);
}

main();