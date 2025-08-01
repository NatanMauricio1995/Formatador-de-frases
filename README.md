# Formatador de Frases

## Descrição

Aplicação Python desenvolvida para demonstrar conceitos de programação orientada a objetos através de um sistema interativo de formatação e análise de frases. O programa oferece diversas funcionalidades para manipulação de texto, incluindo conversões de caso, contagem de caracteres e busca de palavras.

## Funcionalidades

- **Conversão de Texto**:
  - Converter para maiúsculas
  - Converter para minúsculas  
  - Capitalizar primeira letra# Formatador de Frases

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat-square&logo=python)
![Status](https://img.shields.io/badge/Status-Concluído-green?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)

Sistema interativo em Python para formatação e análise completa de frases, demonstrando conceitos de Programação Orientada a Objetos e manipulação avançada de strings.

## Descrição do Projeto

Este projeto foi desenvolvido como exercício de **Programação Orientada a Objetos** e **manipulação de strings** em Python. O programa demonstra conceitos fundamentais como classes, métodos, estruturas condicionais, validação de entrada e interface de usuário interativa.

### Problema Resolvido
- **Cenário:** Necessidade de formatar e analisar textos de múltiplas formas
- **Solução:** Sistema orientado a objetos com menu interativo e 9 funcionalidades
- **Resultado:** Formatação completa e análise detalhada de qualquer frase

## Funcionalidades

### Formatação de Texto
- **Conversão para Maiúsculas:** Transforma toda a frase em letras maiúsculas
- **Conversão para Minúsculas:** Transforma toda a frase em letras minúsculas  
- **Capitalização:** Capitaliza apenas a primeira letra da frase
- **Formato Título:** Converte primeira letra de cada palavra para maiúscula

### Análise de Texto
- **Contador de Vogais:** Conta vogais incluindo acentuadas (á, é, í, ó, ú, etc.)
- **Contador de Consoantes:** Conta todas as consoantes incluindo 'ç'
- **Contador de Letra 'A':** Conta especificamente ocorrências da letra 'a'
- **Busca de Palavras:** Permite buscar quantas vezes uma palavra específica aparece
- **Exibição Original:** Mostra a frase original a qualquer momento

### Interface e Validação
- **Menu Interativo:** Interface numerada com 10 opções
- **Validação Robusta:** Aceita apenas números entre 1-10
- **Tratamento de Erros:** Captura entradas inválidas e solicita correção
- **Feedback Visual:** Títulos formatados e separadores visuais

## Tecnologias

- **Python 3.x**
- **Programação Orientada a Objetos:** Classes, métodos, encapsulamento
- **Métodos de String:** `.upper()`, `.lower()`, `.capitalize()`, `.title()`, `.count()`
- **Estruturas de Controle:** `while`, `if/elif/else`, `for`
- **Tratamento de Exceções:** `try/except ValueError`

## Como Executar

### Pré-requisitos
- Python 3.6 ou superior instalado

### Passos
1. **Clone o repositório:**
   ```bash
   git clone https://github.com/seu-usuario/formatador-frases.git
   cd formatador-frases
   ```

2. **Execute o programa:**
   ```bash
   python formatador_frases.py
   ```

3. **Interaja com o programa:**
   - Digite uma frase quando solicitado
   - Escolha uma das 10 opções do menu
   - Veja o resultado da operação
   - Continue explorando outras funcionalidades

## Preview do Sistema

```
Insira a frase a ser formatada: Olá mundo Python

────────────────────────────────────────────────────────────────────────────────────────────────────
                                                 MENU
────────────────────────────────────────────────────────────────────────────────────────────────────

Opções:
  1  - Converter toda a frase para letras maiúsculas
  2  - Converter toda a frase para letras minúsculas
  3  - Capitalizar a primeira letra da frase
  4  - Converte a primeira letra de cada palavra da frase para maiúscula
  5  - Contar e retornar o número de vogais na frase
  6  - Contar e retornar o número de consoantes na frase
  7  - Contar e retornar o número de ocorrências da letra 'a' na frase
  8  - Contar e retornar o número de ocorrências de uma palavra específica na frase
  9  - Retornar a frase atual
  10 - Sair

Insira o valor numérico inteiro da opção desejada: 1

────────────────────────────────────────────────────────────────────────────────────────────────────
                                      TODAS AS LETRAS MAIÚSCULAS
────────────────────────────────────────────────────────────────────────────────────────────────────

A frase formatada é:
- OLÁ MUNDO PYTHON
```

## Estrutura do Código

### Arquivo Principal
- **`formatador_frases.py`** - Sistema completo de formatação

### Classe Principal
```python
class Formatador_de_frase:
    def __init__(texto)           # Construtor da classe
    def para_maiusculas()         # Conversão maiúscula
    def para_minusculas()         # Conversão minúscula  
    def capitalizar()             # Capitalização
    def formato_titulo()          # Formato título
    def contar_vogais()           # Contador de vogais
    def contar_consoantes()       # Contador de consoantes
    def contar_letra_a()          # Contador letra 'a'
    def procurar_palavra()        # Busca de palavras
    def obter_frase()             # Exibe frase original
```

### Funções Auxiliares
```python
def titulo(titulo_sessao)         # Formatação visual dos títulos
def menu()                        # Interface do usuário
def define_escolha()              # Validação de entrada
def exibir_frase(frase, funcao)   # Padronização de exibição
def main()                        # Programa principal
```

## Conceitos Aplicados

### Programação Orientada a Objetos
- **Encapsulamento:** Dados e métodos organizados em classe
- **Métodos de Instância:** Operações que manipulam o texto da instância
- **Construtor:** Inicialização do objeto com texto fornecido

### Manipulação de Strings
- **Métodos Built-in:** Uso de `.upper()`, `.lower()`, `.capitalize()`, `.title()`
- **Contagem de Caracteres:** Implementação de contadores personalizados
- **Case Insensitive:** Normalização para comparações

### Validação e Interface
- **Loop de Validação:** Repetição até entrada válida
- **Tratamento de Exceções:** Captura de `ValueError` para entradas não numéricas
- **Interface Amigável:** Menu numerado e feedback visual consistente

### Boas Práticas
- **Modularização:** Separação de responsabilidades em funções
- **Comentários Descritivos:** Documentação clara do código
- **Formatação Consistente:** Padronização visual em todas as saídas

## Especificações Técnicas

- **Entrada:** Qualquer frase de texto
- **Saída:** Formatação ou análise conforme opção escolhida
- **Vogais Suportadas:** a, á, à, ã, â, e, é, ê, i, í, o, ô, ó, õ, u, ú
- **Consoantes Suportadas:** Todas incluindo 'ç'
- **Validações:** Menu aceita apenas números 1-10
- **Compatibilidade:** Multiplataforma (Windows, Linux, macOS)

## Exemplo de Uso

| Opção | Entrada | Resultado |
|-------|---------|-----------|
| 1 | "hello world" | "HELLO WORLD" |
| 2 | "PYTHON" | "python" |
| 3 | "programming" | "Programming" |
| 4 | "hello world" | "Hello World" |
| 5 | "programming" | "Há 4 vogais na frase" |
| 8 | "hello hello world" + "hello" | "A palavra hello aparece 2 vezes na frase" |

## Aprendizados

Este projeto consolidou conhecimentos em:
- **Programação Orientada a Objetos em Python**
- **Manipulação avançada de strings e métodos built-in**
- **Estruturas de controle e loops de validação**
- **Interface de usuário em terminal com menu interativo**
- **Tratamento de exceções e validação robusta**
- **Modularização e organização de código limpo**

## Melhorias Futuras

- [ ] Implementação de testes unitários automatizados
- [ ] Suporte para processamento de arquivos de texto
- [ ] Interface gráfica com Tkinter ou PyQt
- [ ] Análise estatística avançada (frequência de palavras, densidade lexical)
- [ ] Exportação de resultados para CSV/PDF
- [ ] Suporte para múltiplos idiomas e caracteres especiais
- [ ] Modo batch para processar múltiplas frases
- [ ] Integração com APIs de análise de texto

## Contribuições

Contribuições são bem-vindas! Para contribuir:

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/nova-feature`)
3. Commit suas mudanças (`git commit -m 'Adiciona nova feature'`)
4. Push para a branch (`git push origin feature/nova-feature`)
5. Abra um Pull Request

## Contato

**[Seu Nome]**
📧 Email: seu.email@exemplo.com
💼 LinkedIn: linkedin.com/in/seu-perfil
🐙 GitHub: github.com/seu-usuario

---

Se este projeto te ajudou, deixe uma estrela!

*Desenvolvido como exercício de Programação Orientada a Objetos em Python*
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
