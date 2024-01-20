document.addEventListener('DOMContentLoaded', function () {
    
    const themeToggle = document.getElementById('theme-toggle');
    const toggleIcon = document.getElementById('toggle-icon');
    if(localStorage.getItem('mode')){
        const mode = localStorage.getItem('mode');
        if(mode == "dark"){
            document.body.classList.toggle('dark-theme');
            toggleIcon.classList.toggle('dark-mode');
            toggleIcon.classList.toggle('light-mode');
            themeToggle.click()
        }
    }

    themeToggle.addEventListener('change', function () {
        document.body.classList.toggle('dark-theme');
        toggleIcon.classList.toggle('dark-mode');
        toggleIcon.classList.toggle('light-mode');
        let mode = "light"
        if(document.getElementsByClassName('dark-theme')[0]){
            mode = "dark"
        }
        localStorage.setItem('mode', mode)
    });
});
