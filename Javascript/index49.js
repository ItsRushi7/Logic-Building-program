
//codePointAt to convert string into ASCII value
// String.fromCodePoint() this is coverted ASCII into string char

let displayletter = (char) => {

    for (let count = 65; count <= char; count++) {
        console.log(String.fromCodePoint(count));
    }
}

function main() {
    let char = 'E';
    let UTF = 0; 

    UTF = char.codePointAt(char);

    displayletter(UTF);

}
main();