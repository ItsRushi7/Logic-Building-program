function checkPallindrome(str) {

    let len = (str.length - 1)
    let temp = '';

    for (let i = len; i >= 0; i--) {
        temp = temp + str[i];
    }

    console.log(temp);

    if (temp == str) {
        return true;
    }

    else {
        return false;
    }
}

function main() {
    let string = 'qwerttrewq';
    let ans = false;

    ans = checkPallindrome(string);

    if (ans === true) {
        console.log('this is pallendrome string ');
    }
    else {
        console.log('this is not pallendrome string ');
    }
}
main();