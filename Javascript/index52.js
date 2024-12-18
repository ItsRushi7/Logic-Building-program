function display(num) {

    let rev = 0;
    while (num != 0) {

        rev = num % 10;
        switch (rev) {
            case 1:
                console.log('one');
                break;

            case 2:
                console.log('two');
                break;

            case 3:
                console.log('three');
                break;

            case 4:
                console.log('four');
                break;

            case 5:
                console.log('five');
                break;

        }
        num = parseInt(num / 10);
    }
}

function main() {
    let value = 1234;

    display(value);

}
main();