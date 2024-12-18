function insertAtPos(arr, atPos, value) {

    let len = arr.length;
    let brr = [];

    if (atPos < 0 || atPos > len) {
        console.log('Position invalid.....');
    }

    if (atPos == 0) {
        arr.unshift(value);
    }

    else if (atPos == len) {
        arr.push(value)
    }

    else {
        for (let i = 0; i < atPos; i++) {

            if (i == atPos - 1) {
                arr.splice(i, 0, value);           
            }
        }
    }

    return arr;
}
function main() {

    let arr = [10, 20, 30, 40, 50, 60],
        pos = 5,
        value = 100,
        ans = [];

    ans = insertAtPos(arr, pos, value);

    console.log(`After insert element into array \n${ans}`);

}
main();
