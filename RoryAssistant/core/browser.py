import webbrowser
from utils.helpers import get_open_browsers
from core.voice import VoiceHandler

class BrowserHandler:
    def __init__(self):
        self.voice = VoiceHandler()

    def search_youtube(self, query, browser=None):
        url = f"https://www.youtube.com/results?search_query={query}"
        open_browsers = get_open_browsers()

        if browser:  # Si especificaste un navegador
            if browser in open_browsers:
                self.voice.speak(f"¡Listo! Abriendo una pestaña nueva en {browser}.")
                webbrowser.get(browser).open_new_tab(url)
            else:
                self.voice.speak(f"{browser} no está abierto, lo abriré para ti.")
                try:
                    webbrowser.get(browser).open(url)
                except webbrowser.Error:
                    self.voice.speak(f"No pude abrir {browser}. Usando el predeterminado.")
                    webbrowser.open(url)
        else:  # Si no especificaste
            if len(open_browsers) == 0:
                self.voice.speak("¡Listo! Abriendo el navegador y buscando en YouTube.")
                webbrowser.open(url)
            elif len(open_browsers) == 1:
                self.voice.speak("¡Listo! Abriendo una pestaña nueva y buscando en YouTube.")
                webbrowser.open_new_tab(url)
            else:
                self.voice.speak(f"Tengo varios navegadores abiertos: {', '.join(open_browsers)}.")
                choice = input("¿En cuál quieres buscar? (escribe el nombre o deja en blanco para usar el primero): ").lower()
                if choice in open_browsers:
                    self.voice.speak(f"¡Listo! Abriendo una pestaña en {choice}.")
                    webbrowser.get(choice).open_new_tab(url)
                else:
                    self.voice.speak("No entendí. Usaré el primero que encontré.")
                    webbrowser.open_new_tab(url)