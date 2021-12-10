window.addEventListener("scroll", funtion(),{
    const header = document.querySelector("header");
    header.classList.toggle("sticky", window.scrollY > 0);
});