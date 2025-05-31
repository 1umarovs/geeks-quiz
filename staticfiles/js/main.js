let btn = document.querySelector(".btn");
let modal = document.querySelector(".modal-block");
let closeBtn = document.querySelector(".close-btn");
let main = document.querySelector(".main");
let body = document.body;

if (btn && modal && closeBtn && main) {
    btn.addEventListener("click", () => {
        modal.classList.add("active-modal");
        body.classList.add("no-scroll");
        main.classList.add("opacity");
    });

    closeBtn.addEventListener("click", () => {
        modal.classList.remove("active-modal");
        body.classList.remove("no-scroll");
        main.classList.remove("opacity");
    });
}
