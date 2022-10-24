let msg = document.getElementById("msg")
let make_msg_none = document.getElementById("make_msg_none")

// if (make_msg_none){
    function noneFun(){
        // if(msg){
            console.log("clicked");
            msg.classList.add("d-none")
            console.log(msg);
        // }
    }
    make_msg_none.addEventListener("click", noneFun)
// }
