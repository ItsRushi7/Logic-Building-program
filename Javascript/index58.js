function addEmenetArray(Arr, size) {
    
    for (let index = 0; index < size; index++) {
        Arr[index] = index + 1;

    }
    return Arr;
}
function main() {

    let size = 5;
    let Arr = [];
    let ans = 0;

    ans = addEmenetArray(Arr, size);

    for (let index = 0; index < ans.length; index++) {

        console.log(ans[index]);

    }
}
main();