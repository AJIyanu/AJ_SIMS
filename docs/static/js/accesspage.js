const switchLink = document.querySelector('.switch-link');
const formView = document.querySelectorAll('.formview');

switchLink.addEventListener("click", (event) => {
    event.preventDefault();

    console.log(switchLink.innerText);
    if (switchLink.innerText === "New Parent?") {
        formView[1].classList.add('active');
        formView[0].classList.remove('active');
        switchLink.innerText = "I am a Registered Parent"
    } else {
        formView[0].classList.add('active');
        formView[1].classList.remove('active');
        switchLink.innerText = 'New Parent?';
    }
})
