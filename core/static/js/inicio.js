// Obtener la ventana emergente y el enlace de cierre
var modal = document.getElementById("loginModal");
var closeBtn = document.getElementsByClassName("close")[0];

// Mostrar la ventana emergente al hacer clic en el enlace de inicio de sesión
document.getElementById("loginLink").onclick = function() {
  modal.style.display = "block";
};

// Ocultar la ventana emergente al hacer clic en el botón de cierre
closeBtn.onclick = function() {
  modal.style.display = "none";
};

// Ocultar la ventana emergente al hacer clic fuera del contenido de la ventana emergente
window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
};