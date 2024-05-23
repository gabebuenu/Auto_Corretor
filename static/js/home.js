document.getElementById('btnPagina2').addEventListener('click', function() {
    document.getElementById('pagina1').style.display = 'none';
    document.getElementById('pagina2').style.display = 'block';
    document.getElementById('botao_avaliar').disabled=true;
});

document.getElementById('btnPagina1').addEventListener('click', function() {
    document.getElementById('pagina2').style.display = 'none';
    document.getElementById('pagina1').style.display = 'block';
    document.getElementById('botao_avaliar').disabled=false;
});