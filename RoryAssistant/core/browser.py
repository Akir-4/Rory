import webbrowser
from utils.helpers import get_open_browsers

class BrowserHandler:
    def search_youtube(self, query, browser=None):
        url = f"https://www.youtube.com/results?search_query={query}"
        open_browsers = get_open_browsers()

        if browser:  # Si especificaste un navegador
            if browser in open_browsers:
                print(f"¡Listo! Abriendo una pestaña nueva en {browser}.")
                webbrowser.get(browser).open_new_tab(url)
            else:
                print(f"{browser} no está abierto, lo abriré para ti.")
                try:
                    webbrowser.get(browser).open(url)  # Abre el navegador especificado
                except webbrowser.Error:
                    print(f"No pude abrir {browser}, usando el predeterminado.")
                    webbrowser.open(url)
        else:  # Si no especificaste
            if len(open_browsers) == 0:
                print("¡Listo! Abriendo el navegador y buscando en YouTube.")
                webbrowser.open(url)
            elif len(open_browsers) == 1:
                print("¡Listo! Abriendo una pestaña nueva y buscando en YouTube.")
                webbrowser.open_new_tab(url)
            else:
                print(f"Tengo varios navegadores abiertos: {open_browsers}")
                choice = input("¿En cuál quieres buscar? (escribe el nombre o deja en blanco para usar el primero): ").lower()
                if choice in open_browsers:
                    print(f"¡Listo! Abriendo una pestaña en {choice}.")
                    webbrowser.get(choice).open_new_tab(url)
                else:
                    print("No entendí, usaré el primero que encontré.")
                    webbrowser.open_new_tab(url)