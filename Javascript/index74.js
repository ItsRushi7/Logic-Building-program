function strcom(str1, str2) {
    str1 = str1 + '\0';
    str2 = str2 + '\0';

    let i = 0;
    let flag = true;

    while ((str1[i],str2[i] != '\0')) {

        if (str1[i] != str2[i]) {
            flag = false;
            break;
        }
        i++;
    }

    return flag;
}
function main() {

    let string1 = 'Abcd';
    let string2 = 'Abed';

    let ans = false;

    ans = strcom(string1, string2);

    if (ans === true) {
        console.log('Both string are equal');
    }
    else {
        console.log('Both string are not equal');
    }

}
main();