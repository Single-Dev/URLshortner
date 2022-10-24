let short_link_val = document.querySelector("#short_link_copy")
let document_href = document.getElementById("document_href")
let clipboard_write = document.getElementById("clipboard_write")

if (short_link_val) {
    if (clipboard_write) {
        clipboard_write.addEventListener("click", function () {
            navigator.clipboard.writeText(`${document.location.href}${short_link_val.innerHTML}`)
            console.log(short_link_val.innerHTML)
        })
    }
    if (document_href) {
        document_href.innerHTML = document.location.href
    }
}
