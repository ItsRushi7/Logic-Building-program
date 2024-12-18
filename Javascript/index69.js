function strlen(str) {

    str = str + '\0';

    console.log(str);
    let len = 0;
    let i = 0;

    while (str[i] != '\0') {
        len++;
        i++;
    }

    return len;
}
function main() {
    let string = "Arraypointer";
    let ans = 0;

    ans = strlen(string);

    console.log(`length of string is ${ans}`);

}

main();