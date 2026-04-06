document.querySelectorAll('.opcaoQuiz').forEach(div => {
    div.addEventListener('click', () => {
        const radio = div.querySelector('input[type="radio"]');
        radio.checked = true;
        radio.dispatchEvent(new Event('change'));
    });
});