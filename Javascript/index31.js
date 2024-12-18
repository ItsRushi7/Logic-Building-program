function calculateSimpleIntrest(P, R, N) {
    
    let simpleIntrest = (P * R * N) / 100;

    return simpleIntrest;
}

function main() {
    let Principle_Amount = 2000,
        Rate_of_intarest = 3.5,
        Number_of_year = 2;

    let ans = 0;

    ans = calculateSimpleIntrest( Principle_Amount, Rate_of_intarest, Number_of_year);

    console.log(`Simple intrest is ${ans}`);
}

main();