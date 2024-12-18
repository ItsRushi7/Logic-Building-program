function countDigAlphSym(str) {

    str = str + '\0';

    let Digit = 0,
        alphabet = 0,
        Symbol = 0;
    i = 0;

    while (str[i] != '\0') {

        if (str[i] >= 'a' && str[i] <= 'z') {
            alphabet++;
        }

        else if (str[i] >= 'A' && str[i] <= 'Z') {
            alphabet++;
        }

        else if (str[i] >= '0' && str[i] <= '9') {
            Digit++;
        }
        else {
            Symbol++;
        }

        i++;

    }

    console.log(`Alphabet in string ${alphabet}`);
    console.log(`Digit in string ${Digit}`);
    console.log(`Symbol in string ${Symbol}`);

}

function main() {
    let string = 'qwer3467ik*%$#@';

    countDigAlphSym(string);

}
main();