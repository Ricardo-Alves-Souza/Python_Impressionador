palavra_usuario = str(input('Digite uma palavra: '))

def analisar_texto(texto):
    """
    analisa o texto fornecido e calcula a contagem de palavras, a frequência de palavras
    e a frequencia de letras.

    Parameters
    ----------
    texto : str 

    Return
    ------
    tuple
        contagem de palavras, frequência de palavras, frequência de letras
    """

    from string import punctuation
    from collections import Counter

    tratamento = str.maketrans('', '', punctuation)
    texto_tratado = texto.translate(tratamento).casefold()
    texto_split = texto_tratado.split()

    print(f'Total de palavras {len(texto_split)}')
    print(Counter(texto_split))
    print(Counter(texto_tratado))
       
analisar_texto(palavra_usuario)