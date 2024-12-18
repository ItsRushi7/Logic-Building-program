function calculateArea(num) {
    const PI = 3.14;
    let redius = num;
    let area = 0.0;

    area = PI * redius * redius;

    return area;
}

function main() {
    let value = 4;
    let ans = 0;

    ans = calculateArea(value);

    console.log(` area of circle is ${ans}`);
}

main();