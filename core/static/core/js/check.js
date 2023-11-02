document.getElementById('checkTerminos').addEventListener('change', function () {
    document.getElementById('btnConfirmar')
    btnConfirmar.disabled = !this.checked;
});
