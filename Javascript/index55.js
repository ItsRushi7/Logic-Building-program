function square(num) {
    let ans = 0;

    ans = num * num;

    return ans;
}

function cube(num) {

    let ans = 0;

    ans = num * num * num;

    return ans;
}

function main() {

    let value = 2;
    let ans = 0;

    ans = square(value);
    console.log(`square of ${ans}`);

    ans = cube(value);
    console.log(`cube of ${ans}`);

}

main();