/**
 * Talking Hands — Dark Mode Toggle
 * Salva a preferência do usuário em localStorage.
 * Se não houver preferência, segue o sistema (prefers-color-scheme).
 */
(function () {
    const STORAGE_KEY = 'th-theme';

    function getPreferred() {
        const stored = localStorage.getItem(STORAGE_KEY);
        if (stored === 'dark' || stored === 'light') return stored;
        return null; // deixa o CSS usar prefers-color-scheme
    }

    function apply(theme) {
        if (theme) {
            document.documentElement.setAttribute('data-theme', theme);
        } else {
            document.documentElement.removeAttribute('data-theme');
        }

        // Atualiza a barra de navegação do navegador móvel
        const metaThemeColor = document.querySelector('meta[name="theme-color"]');
        if (metaThemeColor) {
            const isDark = theme === 'dark' || (!theme && window.matchMedia('(prefers-color-scheme: dark)').matches);
            metaThemeColor.setAttribute('content', isDark ? '#000000' : '#f7f8f5');
        }
    }

    // Aplica imediatamente (antes do DOM carregar) para evitar flash
    apply(getPreferred());

    document.addEventListener('DOMContentLoaded', function () {
        var btn = document.getElementById('theme-toggle');
        if (!btn) return;

        btn.addEventListener('click', function () {
            // Determina o tema ATUAL visível
            var current = document.documentElement.getAttribute('data-theme');
            if (!current) {
                // Sem atributo => detecta do sistema
                current = window.matchMedia('(prefers-color-scheme: dark)').matches
                    ? 'dark'
                    : 'light';
            }

            var next = current === 'dark' ? 'light' : 'dark';
            localStorage.setItem(STORAGE_KEY, next);
            apply(next);
        });
    });
})();
