function strUpperCase(str) {
    str = str + '\0';
    let i = 0;
    let newString = '';

    while (str[i] != '\0') {

        let ASCII = str[i].codePointAt() - 32;
        newString = newString + String.fromCodePoint(ASCII);
        i++;
    }

    return newString;
}
function main() {
    let string = 'arraypointer';
    let ans = '';

    ans = strUpperCase(string);

    console.log(`After string in uppercasee ${ans}`);
}

main();