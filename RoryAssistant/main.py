import webbrowser
from core.assistant import RoryAssistant

# Registrar navegadores comunes (rutas en español)
webbrowser.register('chrome', None, webbrowser.BackgroundBrowser("C:\\Archivos de programa\\Google\\Chrome\\Application\\chrome.exe"))
webbrowser.register('brave', None, webbrowser.BackgroundBrowser("C:\\Archivos de programa\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"))
webbrowser.register('firefox', None, webbrowser.BackgroundBrowser("C:\\Archivos de programa\\Mozilla Firefox\\firefox.exe"))
# Añade más si usas otros navegadores (Edge, etc.)

def run():
    rory = RoryAssistant()
    rory.start()

if __name__ == "__main__":
    run()