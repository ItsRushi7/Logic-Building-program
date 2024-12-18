function display(string1) {
    if (string1 == 'ECMAScript' || string1 == 'ecmascript') {
        console.log('right!');
    }

    else {
        console.log("you dont no ECMAScript");
    }
}

function main() {
    let str1 = null;
    str1 = prompt('what is the official name of java script ', '');

    display(str1);

}

main();