document.getElementById('checkTerminos').addEventListener('change', function () {
    document.getElementById('btnConfirmar')
    btnConfirmar.disabled = !this.checked;
});


document.getElementById('hidetext_btn').addEventListener('click', function () {
    var hiddenText = document.getElementById('hidetext');
    hiddenText.classList.toggle('showText');
    hiddenText.classList.toggle('hideText');
});