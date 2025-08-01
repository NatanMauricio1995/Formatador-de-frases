# Formatador de Frases

## Descrição

Aplicação Python desenvolvida para demonstrar conceitos de programação orientada a objetos através de um sistema interativo de formatação e análise de frases. O programa oferece diversas funcionalidades para manipulação de texto, incluindo conversões de caso, contagem de caracteres e busca de palavras.

## Funcionalidades

- **Conversão de Texto**:
  - Converter para maiúsculas
  - Converter para minúsculas  
  - Capitalizar primeira letra
  - Formato de título (primeira letra de cada palavra)

- **Análise de Texto**:
  - Contar vogais na frase
  - Contar consoantes na frase
  - Contar ocorrências da letra 'a'
  - Buscar palavra específica
  - Exibir frase original

## Estrutura do Projeto

```
formatador_frases.py    # Arquivo principal com toda a implementação
README.md              # Documentação do projeto
```

## Como Executar

### Pré-requisitos
- Python 3.6 ou superior

### Execução
1. Clone ou baixe o arquivo `formatador_frases.py`
2. Execute no terminal:
```bash
python formatador_frases.py
```

## Como Usar

1. **Inserir Frase**: Ao iniciar, digite a frase que deseja formatar
2. **Escolher Opção**: Selecione uma das 10 opções disponíveis no menu
3. **Ver Resultado**: O programa exibirá o resultado da operação escolhida
4. **Continuar ou Sair**: Escolha nova operação ou digite 10 para sair

### Exemplo de Uso
```
Insira a frase a ser formatada: Olá mundo Python

MENU
Opções:
  1  - Converter toda a frase para letras maiúsculas
  2  - Converter toda a frase para letras minúsculas
  ...
  10 - Sair

Insira o valor numérico inteiro da opção desejada: 1

TODAS AS LETRAS MAIÚSCULAS
A frase formatada é:
- OLÁ MUNDO PYTHON
```

## Estrutura Técnica

### Classes
- **Formatador_de_frase**: Classe principal que encapsula todas as operações de formatação e análise de texto

### Métodos Principais
- `para_maiusculas()`: Conversão para maiúsculas
- `para_minusculas()`: Conversão para minúsculas
- `capitalizar()`: Capitalização da primeira letra
- `formato_titulo()`: Formato de título
- `contar_vogais()`: Contagem de vogais (incluindo acentuadas)
- `contar_consoantes()`: Contagem de consoantes
- `contar_letra_a()`: Contagem específica da letra 'a'
- `procurar_palavra()`: Busca de palavra específica
- `obter_frase()`: Retorna frase original

### Funções Auxiliares
- `menu()`: Interface do usuário
- `define_escolha()`: Validação de entrada do usuário
- `titulo()`: Formatação visual dos títulos
- `exibir_frase()`: Padronização da exibição de resultados

## Características Técnicas

- **Linguagem**: Python 3
- **Paradigma**: Programação Orientada a Objetos
- **Interface**: Terminal/Console
- **Tratamento de Erros**: Validação de entrada do usuário
- **Encoding**: Suporte a caracteres acentuados

## Conceitos Demonstrados

- Programação Orientada a Objetos (classes, métodos, encapsulamento)
- Manipulação de strings
- Estruturas de controle (loops, condicionais)
- Tratamento de exceções
- Interface de usuário em terminal
- Validação de entrada
- Modularização de código

## Melhorias Futuras

- Implementação de testes unitários
- Suporte a arquivos de texto
- Interface gráfica
- Análise mais avançada de texto (frequência de palavras, etc.)
- Exportação de resultados

## Autor

Desenvolvido como projeto de estudos em Python, demonstrando conceitos fundamentais de programação.
