let file = require('fs');

function createFile(filename) {

    let data = "File is created sucssefully";

    file.access(filename, (err) => {
        if (err) {

            file.writeFile(filename, data, (err) => { 

                if (err) {
                    console.log(err);
                }

                else{
                    console.log('file is created sussefully');
                }
            });
        }
        else {
            console.log('file is exits');
        }

    });
}

function main() {
    let filename = 'Demo.txt';

    let ans = false;

    ans = createFile(filename);

}

main();