function chengeObj(obj)
{
    obj.name = 'Vishu';
    obj.age = 30;
    obj.isAdmin = true;

}

function main() {
    let obj = {
        name: '',
        age: 0,
        isAdmin: false,
    };

    chengeObj(obj);

    console.log(obj);
}

main();