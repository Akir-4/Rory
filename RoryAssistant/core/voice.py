import speech_recognition as sr

class VoiceHandler:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()

    def listen(self, trigger_word="rory"):
        with self.microphone as source:
            print("Escuchando... (di 'Rory' para activarme)")
            self.recognizer.adjust_for_ambient_noise(source, duration=1)  # Ajusta al ruido ambiental
            audio = self.recognizer.listen(source)

        try:
            command = self.recognizer.recognize_google(audio, language="es-ES").lower()
            print(f"Escuché: {command}")
            if trigger_word in command:
                return command
            else:
                return None
        except sr.UnknownValueError:
            print("No entendí lo que dijiste.")
            return None
        except sr.RequestError:
            print("Error al conectar con el servicio de reconocimiento.")
            return None