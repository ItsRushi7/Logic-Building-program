function strrev(str) {
    let len = (str.length - 1);
    let newString = '';
    let count = 0;

    for (count = 1; count <= len; count++) {
        newString = newString + str.at(-count);
    }

    return newString;
}

function main() {

    let string = 'Arraypointer';
    let ans = '';

    ans = strrev(string);

    console.log(`string aftr revers ${ans}`);
}

main();