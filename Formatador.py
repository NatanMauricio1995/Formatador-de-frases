"""
Formatador de Frases - Projeto de Portfólio
Aplicação que demonstra conceitos de POO através de formatação e análise de texto.

Funcionalidades:
- Conversões de caso (maiúscula, minúscula, título, capitalização)
- Contagem de vogais, consoantes e letras específicas
- Busca de palavras
- Interface interativa no terminal

Autor: Natan Mauricio Santos   
Data: 01 de Agosto de 2025
Versão: 1.0
"""

# Definição da classe principal para formatação de frases
class Formatador_de_frase:
    """
    Classe responsável por todas as operações de formatação e análise de frases.
    
    Atributos:
        texto (str): A frase que será manipulada pelos métodos da classe
    """
    
    def __init__(self, texto):
        """
        Construtor da classe - inicializa o objeto com o texto fornecido.
        
        Args:
            texto (str): A frase a ser formatada e analisada
        """
        self.texto = texto
        
    def para_maiusculas(self):
        """
        Converte toda a frase para letras maiúsculas.
        
        Utiliza o método built-in upper() do Python para conversão.
        Exibe o resultado formatado na tela.
        """
        funcao = "todas as letras maiúsculas"
        titulo(funcao)  # Chama função externa para exibir título da seção
        frase_formatada = self.texto.upper()  # Conversão para maiúsculas
        print(f"A frase formatada é:")
        print(f"- {frase_formatada}")
        
    def para_minusculas(self):
        """
        Converte toda a frase para letras minúsculas.
        
        Utiliza o método built-in lower() e função auxiliar para exibição.
        """
        funcao = "todas as letras minúsculas"
        titulo(funcao)
        frase_formatada = self.texto.lower()  # Conversão para minúsculas
        exibir_frase(frase_formatada, funcao)  # Usa função externa para exibir
        
    def capitalizar(self):
        """
        Capitaliza apenas a primeira letra da frase.
        
        Utiliza o método built-in capitalize() que converte a primeira letra
        para maiúscula e o resto para minúscula.
        """
        funcao = "capitalizar a primeira letra da frase"
        titulo(funcao)
        frase_formatada = self.texto.capitalize()  # Capitaliza primeira letra
        exibir_frase(frase_formatada, funcao)
        
    def formato_titulo(self):
        """
        Converte a primeira letra de cada palavra para maiúscula.
        
        Utiliza o método built-in title() que trata cada palavra separadamente.
        """
        funcao = "formato de título"
        titulo(funcao)
        frase_formatada = self.texto.title()  # Formato de título
        exibir_frase(frase_formatada, funcao)
        
    def contar_vogais(self):
        """
        Conta o número total de vogais na frase.
        
        Inclui vogais com acentos comuns do português.
        Usa loop para percorrer cada vogal e somar suas ocorrências.
        """
        funcao = "contar vogais"
        titulo(funcao)
        
        # Lista com todas as vogais, incluindo acentuadas
        vogais = ["a", "á", "à", "ã", "â", "e", "é", "ê", "i", "í", "o", "ô", "ó", "õ", "u", "ú"]
        teste = self.texto.lower()  # Converte para minúscula para comparação
        quantidade = 0       
        
        # Loop que percorre cada vogal da lista
        for vogal in vogais:
            quantidade += teste.count(vogal)  # Soma quantas vezes cada vogal aparece
        
        # Exibe resultado com plural correto
        if(quantidade > 1):
            print(f"Há {quantidade} vogais na frase.")
        else:
            print(f"Há {quantidade} vogal na frase.")

        print("-" * 100)  # Separador visual
        
    def contar_consoantes(self):
        """
        Conta o número total de consoantes na frase.
        
        Inclui o 'ç' como consoante. Usa mesma lógica do contador de vogais.
        """
        funcao = "contar consoantes"
        titulo(funcao)
        
        # Lista com todas as consoantes do alfabeto português
        consoantes = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z", "ç"]
        teste = self.texto.lower()  # Normaliza para minúscula
        quantidade = 0       
        
        # Loop que percorre cada consoante da lista
        for consoante in consoantes:
            quantidade += teste.count(consoante)  # Soma ocorrências de cada consoante
        
        # Exibe resultado com plural correto
        if(quantidade > 1):
            print(f"Há {quantidade} consoantes na frase.")
        else:
            print(f"Há {quantidade} consoante na frase.")

        print("-" * 100)
        
    def contar_letra_a(self):
        """
        Conta especificamente quantas vezes a letra 'a' aparece na frase.
        
        Método mais simples usando count() diretamente para uma letra específica.
        """
        funcao = "contar a letra 'a' na frase"
        titulo(funcao)
        teste = self.texto.lower()  # Normaliza para minúscula
        quantidade = teste.count("a")  # Conta diretamente a letra 'a'
        
        # Exibe resultado com plural correto
        if(quantidade > 1):
            print(f"Há {quantidade} letras 'a' na frase.")
        else:
            print(f"Há {quantidade} letra 'a' na frase.")

        print("-" * 100)
        
    def procurar_palavra(self):
        """
        Permite ao usuário buscar quantas vezes uma palavra específica aparece.
        
        Solicita input do usuário e realiza busca case-insensitive.
        """
        funcao = "contar a ocorrência de uma palavra na frase"
        titulo(funcao)
        
        # Solicita palavra do usuário via input
        palavra = input("Digite a palavra a ser contada na frase: ")
        palavra_corrigida = palavra.lower()  # Normaliza entrada do usuário
        teste = self.texto.lower()  # Normaliza texto da frase
        quantidade = teste.count(palavra_corrigida)  # Conta ocorrências
        
        # Exibe resultado com plural correto
        if(quantidade > 1):
            print(f"A palavra {palavra} aparece {quantidade} vezes na frase.")
        else:
            print(f"A palavra {palavra} aparece {quantidade} vez na frase.")

        print("-" * 100)
    
    def obter_frase(self):
        """
        Exibe a frase original sem modificações.
        
        Útil para o usuário relembrar qual frase está sendo trabalhada.
        """
        funcao = "frase original"
        titulo(funcao)
        print("A frase original é:")
        print(f"- {self.texto}")


# === FUNÇÕES AUXILIARES PARA INTERFACE ===

def titulo(titulo_sessao):
    """
    Exibe um título formatado com bordas de traços.
    
    Args:
        titulo_sessao (str): O texto do título a ser exibido
        
    A função centraliza o título e o exibe em maiúsculas com bordas decorativas.
    """
    # Calcula tamanho do título para centralização
    tamanho = len(titulo_sessao)
    
    # Converte título para maiúsculas para padronização visual
    titulo_sessao = titulo_sessao.upper()
    
    # Define largura total da borda
    quantidade_tracos = 100
    
    # Calcula espaços necessários para centralizar o título
    quantidade_espacos = (quantidade_tracos - tamanho) // 2
    
    # Exibe o título formatado com bordas
    print()
    print("-" * 100)
    print(" " * quantidade_espacos, titulo_sessao)
    print("-" * 100)
    print()

def menu():
    """
    Exibe o menu principal com todas as opções disponíveis.
    
    Apresenta lista numerada de funcionalidades que o usuário pode escolher.
    """
    # Exibe título da seção
    titulo("menu")

    print("Opções:")
    print("  1  - Converter toda a frase para letras maiúsculas;")
    print("  2  - Converter toda a frase para letras minúsculas;")
    print("  3  - Capitalizar a primeira letra da frase;")
    print("  4  - Converte a primeira letra de cada palavra da frase para maiúscula;")
    print("  5  - Contar e retornar o número de vogais na frase;")
    print("  6  - Contar e retornar o número de consoantes na frase;")
    print("  7  - Contar e retornar o número de ocorrências da letra 'a' na frase;")
    print("  8  - Contar e retornar o número de ocorrências de uma palavra específica na frase;")
    print("  9  - Retornar a frase atual;")
    print("  10 - Sair")
    print()
    print("-" * 100)
    print()
    
def define_escolha():
    """
    Captura e valida a escolha do usuário do menu.
    
    Returns:
        int: Número da opção escolhida (1-10)
        
    Implementa loop de validação que só aceita números inteiros entre 1 e 10.
    Trata exceções de entrada inválida (ValueError).
    """
    # Inicializa variável com valor inválido para entrar no loop
    escolha = 0
    
    # Loop continua até entrada válida
    while ((escolha < 1) or (escolha > 10)):
        try:
            menu()  # Exibe menu a cada tentativa
            # Tenta converter entrada para inteiro
            escolha = int(input("Insira o valor numérico inteiro da opção desejada: "))
            
            # Verifica se está no range válido
            if ((escolha < 1) or (escolha > 10)):
                print("Valor numérico inválido!")
                
        except ValueError:
            # Captura erro quando entrada não é número
            print("Valor inserido não era um número inteiro!")
        
        print()
    return escolha

def exibir_frase(frase, funcao):
    """
    Padroniza a exibição de frases formatadas.
    
    Args:
        frase (str): A frase já formatada para exibir
        funcao (str): Descrição da operação realizada
        
    Mantém consistência visual na apresentação dos resultados.
    """
    print(f"A frase formatada como {funcao} é:")
    print(f"- '{frase}'")
    print("-" * 100)
    print()


# === PROGRAMA PRINCIPAL ===

def main():
    """
    Função principal que orquestra toda a execução do programa.
    
    Responsável por:
    1. Obter frase do usuário
    2. Criar instância da classe Formatador_de_frase
    3. Executar loop principal do menu
    4. Chamar métodos apropriados baseados na escolha do usuário
    """
    # Solicita frase inicial do usuário
    print()
    frase = input("Insira a frase a ser formatada: ")
    
    # Cria objeto da classe com a frase fornecida
    formatador = Formatador_de_frase(frase)
    
    # Inicializa variável de controle do loop
    escolha = 0
    
    # Loop principal do programa - continua até usuário escolher sair (10)
    while (escolha != 10):
        escolha = define_escolha()  # Obtém escolha válida do usuário
        
        # Estrutura condicional que mapeia escolhas para métodos
        if(escolha == 1):
            formatador.para_maiusculas()
        elif(escolha == 2):
            formatador.para_minusculas()
        elif(escolha == 3):
            formatador.capitalizar()
        elif(escolha == 4):
            formatador.formato_titulo()
        elif(escolha == 5):
            formatador.contar_vogais()
        elif(escolha == 6):
            formatador.contar_consoantes()
        elif(escolha == 7):
            formatador.contar_letra_a()
        elif(escolha == 8):
            formatador.procurar_palavra()
        elif(escolha == 9):
            formatador.obter_frase()
        elif(escolha == 10):
            titulo("Até mais!")  # Mensagem de despedida


# Ponto de entrada do programa - garante que main() só execute se arquivo for executado diretamente
if __name__ == "__main__":
    main()