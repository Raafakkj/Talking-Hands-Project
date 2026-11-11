document.addEventListener("DOMContentLoaded", () => {
    // Seleciona todas as seções dentro do <main>
    const secoes = document.querySelectorAll("main > section");

    // Se o navegador não suportar IntersectionObserver, mostra tudo direto
    if (!("IntersectionObserver" in window)) {
        secoes.forEach((secao) => secao.classList.add("visivel"));
        return;
    }

    const observador = new IntersectionObserver((entradas, obs) => {
        entradas.forEach((entrada) => {
            if (entrada.isIntersecting) {
                entrada.target.classList.add("visivel");
                obs.unobserve(entrada.target); // Anima apenas uma vez
            }
        });
    }, {
        threshold: 0.24 // Dispara quando 12% da seção entrar na tela
    });

    secoes.forEach((secao) => {
        secao.classList.add("reveal");
        observador.observe(secao);
    });
});