function checkEligibility(married, gender, age) {

    if (married == true) {
        console.log('you are already married');
    }

    else {

        if (gender == 'm') {
            if (age >= 21) {
                console.log('you can married');
            }
            else {
                console.log('you can not married');
            }
        }

        if (gender == 'f') {

            if (age >= 18) {
                console.log('you can married');
            }
            else {
                console.log('you can not married');
            }
        }

    }
}

function main() {
    let married = false,
        gender = 'm',
        age = 2;

    checkEligibility(married, gender, age);
}
main();