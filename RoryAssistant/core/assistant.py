from core.voice import VoiceHandler
from core.browser import BrowserHandler

class RoryAssistant:
    def __init__(self):
        self.voice = VoiceHandler()
        self.browser = BrowserHandler()
        self.name = "Rory"

    def start(self):
        self.voice.speak(f"¡Hola! Soy {self.name}. Estoy listo para escucharte.")
        while True:
            comando = self.voice.listen()
            if comando:
                self.process_command(comando)

    def process_command(self, comando):
        comando = comando.lower()
        if self.name.lower() in comando:
            if "busca" in comando and "youtube" in comando:
                browsers = ["chrome", "firefox", "edge", "safari", "brave"]
                specified_browser = None
                for browser in browsers:
                    if f"en {browser}" in comando:
                        specified_browser = browser
                        query = comando.split("busca")[1].replace(f"en youtube en {browser}", "").replace("en youtube", "").strip()
                        break
                if specified_browser:
                    self.browser.search_youtube(query, specified_browser)
                else:
                    query = comando.split("busca")[1].replace("en youtube", "").strip()
                    self.browser.search_youtube(query)
            else:
                self.voice.speak("No entendí. ¿Qué quieres que haga?")