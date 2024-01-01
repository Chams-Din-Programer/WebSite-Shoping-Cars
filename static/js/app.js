
function showpw(){
    const input = document.getElementById("Comfirm-Password");
    const hide1 = document.getElementById("hide1");
    const hide2 = document.getElementById("hide2");

    if(input.type === "password"){
        input.type = "text";
        hide2.style.display = "block";
        hide1.style.display = "none";
    }
    else{
        input.type = "password";
        hide2.style.display = "none";
        hide1.style.display = "block";
    }
}


const inputs = document.querySelectorAll(".contact-input");
const toggleBtn = document.querySelector(".theme-toggle");
const allElements = document.querySelectorAll("*");

toggleBtn.addEventListener("click", () => {
    document.body.classList.toggle("dark");

    allElements.forEach(el => {
        el.classList.add("transition");
        setTimeout(() => {
            Element.classList.remove("transition");
        }, 1000);
    });
});

inputs.forEach((ipt) => {
    ipt.addEventListener("focus", () => {
        ipt.parentNode.classList.add("focus");
        ipt.parentNode.classList.add("not-empty");
    });
    ipt.addEventListener("blur", () => {
        if (ipt.value == "") {
            ipt.parentNode.classList.remove("not-empty");
        }
        ipt.parentNode.classList.remove("focus");
    });
});