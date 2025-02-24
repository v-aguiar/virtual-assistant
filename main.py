from speech_to_text import listen
from text_to_speech import speak
from search_on_wikipedia import search_wikipedia

def main():
    while True:
        command = listen()
        if command:
            if 'pesquisar' in command:
                speak("Sobre o que você gostaria de pesquisar no Wikipedia?")
                search_query = listen()  # Espera o usuário fornecer a pesquisa
                result = search_wikipedia(search_query)
                speak(result)
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
