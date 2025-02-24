from speech_to_text import listen
from text_to_speech import speak
from search_on_wikipedia import search
from open_youtube import open_yt

def main():
    while True:
        command = listen()
        print(f"Você disse agora: {command}")  # Adicionando o print para debug

        if command:
            command = command.strip().lower()

            print(f"Comando processado: '{command}'")

            if 'oi' in command:
                speak("Olá! Como posso ajudar?")
            elif 'pesquisar' in command:
                speak("Sobre o que você gostaria de pesquisar no Wikipedia?")
                search_query = listen()  # Espera o usuário fornecer a pesquisa
                result = search(search_query)
                speak(result)
            elif 'abrir youtube' in command:
                speak("Abrindo o YouTube.")
                result = open_yt()
                speak(result)
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
