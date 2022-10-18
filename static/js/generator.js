let short_link = document.querySelector("#short_link")
let url = document.querySelector("#url")
let btn = document.querySelector("#btn")

let shortLink = document.querySelector("#short_link")
let edit_btn = document.getElementById("edit_btn")


let = upper = "QWERTYUIOPASDFGHJKLMNBVCXZ"
let = lower = 'qwertyuiopasdfghjklmnbvcxz'
let numbers = "1234567890"
let character = "-_"

const characters = upper + lower + numbers + character

function generateString(length) {
    let result = ' ';
    const charactersLength = characters.length;
    for ( let i = 0; i < length; i++ ) {
        result += characters.charAt(Math.floor(Math.random() * charactersLength));
    }
    return result;
}

if(edit_btn){
    edit_btn.addEventListener("click", function(){
        shortLink.type = "text"
    })
}


btn.addEventListener("click", function(){
    if (short_link.value == ""){
        if(url.value != ""){
            short_link.value = generateString(8)
        }
    }
    else{
        console.log("nimadir xato ketdi");
    }
})

