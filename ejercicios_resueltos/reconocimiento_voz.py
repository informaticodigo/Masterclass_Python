import speech_recognition as sr
import webbrowser

# Declaramos el objeto que nos permitirá reconocer el audio
r = sr.Recognizer()
# r.energy_threshold += 280

while True:
    with sr.Microphone() as source:  # Creamos un objeto que captura el audio del microfono
        audio = r.listen(source)  # Leemos el audio
        try:  # Por si no se detecta nada
            text = r.recognize_google(audio, language="es-ES")  # Reconocemos el audio
            # Comprobamos todos los comandos que podemos reconocer
            if text == "noticias":
                webbrowser.open("https://www.elmundo.es/")
            elif text == "navegador":
                webbrowser.open("https://www.google.es/")
            elif text == "canal":
                webbrowser.open("https://www.youtube.com/c/InformatiCodigo")
            elif text == "salir":
                break
        except:
            pass