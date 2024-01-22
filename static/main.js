const burger = document.querySelector(".menu-btn")
const menu = document.querySelector(".menu")
let state = false

burger.addEventListener("click", function() {

    state = !state

    if (state === true) {

        document.getElementById("nav").style.borderRadius = "0";

    } else {
        document.getElementById("nav").style.borderRadius = "25px";
    }

    this.classList.toggle("is-active")
    menu.classList.toggle("in-active")
    menu.classList.toggle("is-active")

})


menu.addEventListener("click", function() {

    state = false
    document.getElementById("nav").style.borderRadius = "25px";
    burger.classList.toggle("is-active")
    menu.classList.toggle("in-active")
    menu.classList.toggle("is-active")


})