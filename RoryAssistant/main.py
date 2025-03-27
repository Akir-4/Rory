import webbrowser
from core.assistant import RoryAssistant

# Registrar navegadores comunes (rutas en español)
webbrowser.register('chrome', None, webbrowser.BackgroundBrowser("C:\\Archivos de programa\\Google\\Chrome\\Application\\chrome.exe"))
webbrowser.register('brave', None, webbrowser.BackgroundBrowser("C:\\Archivos de programa\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"))
webbrowser.register('firefox', None, webbrowser.BackgroundBrowser("C:\\Archivos de programa\\Mozilla Firefox\\firefox.exe"))
webbrowser.register('edge', None, webbrowser.BackgroundBrowser("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"))
# Añade más si usas otros navegadores

def run():
    rory = RoryAssistant()
    rory.start()

if __name__ == "__main__":
    run()