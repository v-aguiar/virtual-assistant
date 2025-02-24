from speech_to_text import listen
from text_to_speech import speak

def main():
    while True:
        command = listen()
        if command:
            if 'pesquisar no Wikipedia' in command:
                speak("Abrindo o Wikipedia.")
                # Adicione o código para abrir o Wikipedia
            elif 'abrir o YouTube' in command:
                speak("Abrindo o YouTube.")
                # Adicione o código para abrir o YouTube
            elif 'localização da farmácia mais próxima' in command:
                speak("Mostrando a localização da farmácia mais próxima.")
                # Adicione o código para mostrar a localização
            elif 'sair' in command:
                speak("Saindo.")
                break
            else:
                speak("Comando não reconhecido.")
if __name__ == "__main__":
    main()
