function calculateSquare(area) {
    let square = 0;

    square = area * area;

    return square;
}

function calculateCube(area)
{

    let cube = 0;

    cube = area ** area;

    return cube;
}

function main() {
    let value = 3;

    let ans = 0;

    ans = calculateSquare(value);
    console.log(`area of square is ${ans}`);

    ans = calculateCube(value);
    console.log(`cube of square is ${ans}`);
}

main();