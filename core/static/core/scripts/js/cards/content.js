function moduleContent() {
    var frente = document.getElementById('front');
    var detras = document.getElementById('back');
    var button = document.getElementById('change-content-button');

    var estado = detras.style.display;

    if (estado == 'none' || !estado) {
        detras.style.display = 'block'
        button.innerHTML = 'Ver frente'
        frente.style.display = 'none'
    } else {
        detras.style.display = 'none'
        button.innerHTML = 'Ver reverso'
        frente.style.display = 'block'
    }
}