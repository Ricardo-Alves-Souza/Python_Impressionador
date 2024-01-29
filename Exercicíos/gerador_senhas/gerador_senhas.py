import string
from random import choice
from random import choices
from random import shuffle

def gerar_senha(tamanho):
    if tamanho < 4:
        print('O tamanho da senha não pode ser menor do que 4 caracteres, digite outro tamanho!')
    else:
        letra, numero, caracter_especial = string.ascii_letters, string.digits, string.punctuation
        senha = [choice(letra), choice(numero), choice(caracter_especial)]

        posibilidades = "".join([letra, numero, caracter_especial])

        senha.extend(choices(posibilidades, k= tamanho - 3))

        shuffle(senha)
        
        return "".join(senha)

#tamanho = int(input('Digite o comprimento da senha: '))
tamanho = 10
print(gerar_senha(tamanho))