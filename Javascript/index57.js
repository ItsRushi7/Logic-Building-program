let Stop = 0;

function displayFabbio(num) {

    let a = 0,
        b = 1,
        temp = 0;

    while (Stop != num) {

        console.log(a);
        temp = a + b;
        a = b;
        b = temp;
        Stop++;
        displayFabbio(num);

    }


}

console.log(Stop);

function main() {
    let value = 5;

    displayFabbio(value);

}
main();