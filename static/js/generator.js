let shortner = document.querySelector("#shortner")
let btn = document.querySelector("#btn")
let = upper = "QWERTYUIOPASDFGHJKLMNBVCXZ"
let = lower = 'qwertyuiopasdfghjklmnbvcxz'
let numbers = "1234567890"
let character = "-/_"
const characters = upper + lower + numbers + character

function generateString(length) {
    let result = ' ';
    const charactersLength = characters.length;
    for ( let i = 0; i < length; i++ ) {
        result += characters.charAt(Math.floor(Math.random() * charactersLength));
    }
    return result;
}
btn.addEventListener("click", function(){
    shortner.value = generateString(8)
})