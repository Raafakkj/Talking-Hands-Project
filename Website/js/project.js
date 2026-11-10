/**
 * Talking Hands — Script de Demonstração
 * Utiliza a Web Speech API nativa e tenta comunicação opcional com a API backend (FastAPI).
 */

document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('speak-form');
    const phraseInput = document.getElementById('phrase');
    const charCount = document.getElementById('char-count');
    const statusFeedback = document.getElementById('status-feedback');
    const clearBtn = document.getElementById('btn-clear');
    const chipButtons = document.querySelectorAll('.chip-btn');

    const API_ENDPOINT = 'http://localhost:8000/api/process';

    // Atualiza contador de caracteres
    function updateCharCount() {
        const count = phraseInput.value.length;
        charCount.textContent = `${count} ${count === 1 ? 'caractere' : 'caracteres'}`;
    }

    phraseInput.addEventListener('input', updateCharCount);

    // Botões de atalho rápido (chips)
    chipButtons.forEach((chip) => {
        chip.addEventListener('click', () => {
            const text = chip.getAttribute('data-text');
            phraseInput.value = text;
            updateCharCount();
            phraseInput.focus();
            processAndSpeak(text);
        });
    });

    // Limpar campo
    clearBtn.addEventListener('click', () => {
        phraseInput.value = '';
        updateCharCount();
        phraseInput.focus();
        statusFeedback.textContent = 'Campo limpo. Digite uma nova frase.';
    });

    // Consulta opcional ao backend para expansão / correção
    async function tryBackendCorrection(text) {
        try {
            const controller = new AbortController();
            const timeoutId = setTimeout(() => controller.abort(), 1000); // 1s de tolerância

            const response = await fetch(API_ENDPOINT, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ text }),
                signal: controller.signal,
            });

            clearTimeout(timeoutId);

            if (response.ok) {
                const data = await response.json();
                return data.corrected || text;
            }
        } catch (_) {
            // Backend offline: segue com o texto original sem travar o usuário
        }
        return text;
    }

    // Síntese de voz nativa no navegador
    function speakText(text) {
        if (!('speechSynthesis' in window)) {
            statusFeedback.textContent = 'Seu navegador não possui suporte à síntese de voz nativa.';
            return;
        }

        window.speechSynthesis.cancel();

        const utterance = new SpeechSynthesisUtterance(text);
        utterance.lang = 'pt-BR';
        utterance.rate = 0.95;

        utterance.onstart = () => {
            statusFeedback.textContent = `Reproduzindo: "${text}" 🔊`;
        };

        utterance.onend = () => {
            statusFeedback.textContent = 'Mensagem vocalizada com sucesso.';
        };

        utterance.onerror = () => {
            statusFeedback.textContent = 'Erro ao sintetizar o áudio.';
        };

        window.speechSynthesis.speak(utterance);
    }

    // Fluxo principal: processa e vocaliza
    async function processAndSpeak(text) {
        const trimmed = (text || '').trim();
        if (!trimmed) {
            statusFeedback.textContent = 'Por favor, digite ou selecione uma frase para vocalizar.';
            return;
        }

        statusFeedback.textContent = 'Processando mensagem...';
        const finalPhrase = await tryBackendCorrection(trimmed);

        // Se o backend tiver corrigido/expandido, atualiza o campo para o usuário ver
        if (finalPhrase !== trimmed) {
            phraseInput.value = finalPhrase;
            updateCharCount();
        }

        speakText(finalPhrase);
    }

    // Envio do formulário
    form.addEventListener('submit', (e) => {
        e.preventDefault();
        processAndSpeak(phraseInput.value);
    });

    // Inicializa contador
    updateCharCount();
});
