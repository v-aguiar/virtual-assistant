import speech_recognition as sr

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Aguardando comando...")
        audio = recognizer.listen(source)
    try:
        command = recognizer.recognize_google(audio, language='pt-BR')
        print(f"Você disse: {command}")
        return command.lower()
    except sr.UnknownValueError:
        print("Não entendi o que você disse.")
        return None
    except sr.RequestError:
        print("Erro de conexão com o serviço de reconhecimento de fala.")
        return None
