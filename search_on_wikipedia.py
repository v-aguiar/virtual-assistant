import wikipedia

def search(query):
    try:
        # Faz a busca no Wikipedia e retorna o resumo
        result = wikipedia.summary(query, sentences=1)
        return result
    except wikipedia.exceptions.DisambiguationError as e:
        return f"Encontrado mais de um resultado. Exemplos: {', '.join(e.options)}"
    except wikipedia.exceptions.HTTPTimeoutError:
        return "Houve um erro de tempo de resposta, tente novamente."
    except Exception as e:
        return str(e)