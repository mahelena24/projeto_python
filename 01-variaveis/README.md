## 5. Exercícios de `print()`, `input()`, variáveis e estrutura de dados

Parabéns! Agora que configuramos todas as ferramentas necessárias, vamos concluir nossa aula com um simples "Hello World" em Python.

* Abra o VSCode.
* Crie um novo arquivo Python.
* Crie um repositório no Github
* Crie nosso primeiro arquivo `main.py`

### Comandos

### 1) `print()`

Para usar o comando print basta digitar `print("Alguma coisa")`

Repare que ao redor do nosso texto, coloquei `"o que eu quero escrever"`

Assim, eu consigo avisar ao Python que o que eu quero imprimir é um texto, uma `string`.

Caso eu retire o parentese, irá dar errado.

```
print("Alguma coisa)
print(Alguma coisa")
print(Alguma coisa)
```

**Como lidar com erros?**

O primeiro passo quando você tem algum erro é buscar no Google uma solução para ele

Também é possíve somar operações

```python
print(3 + 5)
```

```python
print("Olá" + " " + "Turma")
```

#### 2) `input()`

O comando input() em Python é uma função incorporada usada para capturar dados de entrada do usuário. Quando esse comando é executado, o programa pausa sua execução e espera que o usuário digite algo no console (ou terminal) e pressione Enter. Os dados inseridos pelo usuário são então retornados pela função input() como uma string (texto). Isso permite que programas interativos recebam informações do usuário para diversos fins, como parâmetros de execução, dados para processamento, escolhas em menus interativos, entre outros.

**Exemplo:**

```python
input("Digite seu nome: ")
```

**Concatenando texto**

```python
print("Olá, " + input("Digite seu nome: ") + "!")
```

**Exercício 01**

Crie programa que o usuário digita o seu nome e retorna o número de caracteres

```bash
Digite o seu nome: Luciano
7
```

**Exercício 02**

Criar um programa onde o usuário digite dois valores e apareça a soma

```python
Digite um valor: 7
Digite outro valo: 10
17
```

#### Considerações Importantes

* **Tipo de Dados**: Por padrão, tudo o que é capturado pelo `input()` é tratado como uma `string`. Se você precisar trabalhar com outro tipo de dado (como inteiros ou floats), será necessário converter a entrada do usuário para o tipo desejado usando funções como `int()` ou `float()`.
    
    ```python
    idade = int(input("Digite sua idade: "))
    ```
    
* **Segurança**: Ao usar `input()` para receber dados do usuário, é importante considerar a validação desses dados, especialmente se eles forem usados em operações críticas ou transmitidos a outras partes do sistema.
    
* **Usabilidade**: O `prompt` deve ser claro e informativo para guiar o usuário sobre o que precisa ser inserido, melhorando a usabilidade e a experiência do usuário.
    
O comando `input()` é uma ferramenta fundamental para criar scripts e programas interativos em Python, permitindo a coleta de dados de entrada de uma maneira fácil e acessível.

#### 3) Declaração e Atribuição de Variáveis

Variáveis em Python são fundamentais para o desenvolvimento de programas, pois atuam como "recipientes" para armazenar dados que podem ser modificados ao longo da execução de um script. Ao contrário de algumas outras linguagens de programação, Python é dinamicamente tipado, o que significa que você não precisa declarar explicitamente o tipo de uma variável antes de usá-la. O tipo de uma variável é determinado automaticamente pelo Python no momento da atribuição de um valor.

**Declaração e Atribuição de Variáveis**

A atribuição de um valor a uma variável em Python é feita com o operador `=`. Por exemplo:

```python
numero = 10
mensagem = "Olá, mundo!"
```

No exemplo acima, `numero` é uma variável que armazena um inteiro (`10`), e `mensagem` é uma variável que armazena uma string (`"Olá, mundo!"`).

**Tipos de Dados**

Python suporta vários tipos de dados, incluindo, mas não se limitando a:

* Inteiros (`int`)
* Números de ponto flutuante (`float`)
* Strings (`str`)
* Listas (`list`)
* Tuplas (`tuple`)
* Dicionários (`dict`)
* Booleanos (`bool`)

A linguagem determina o tipo de dados de uma variável no momento da atribuição, o que permite grande flexibilidade, mas também exige atenção para evitar erros de tipo.

**Nomes de Variáveis**

Python tem algumas regras e convenções para nomes de variáveis:

* Os nomes podem conter letras, números e sublinhados (`_`), mas não podem começar com um número.
* Os nomes de variáveis são _case-sensitive_, o que significa que `variavel`, `Variavel`, e `VARIaVEL` são consideradas três variáveis diferentes.
* Existem algumas palavras reservadas que não podem ser usadas como nomes de variáveis, como `if`, `for`, `class`, entre outras.
* É recomendado seguir a convenção _snake_case_ para nomes de variáveis que consistem em mais de uma palavra, como `nome_usuario` ou `total_pedidos`.

**Dinamismo e Reatribuição**

Uma característica importante das variáveis em Python é a possibilidade de reatribuí-las a diferentes tipos de dados:

```python
x = 100        # x é um inteiro
x = "Python"   # Agora x é uma string
```

Isso demonstra a tipagem dinâmica do Python, mas também destaca a importância de gerenciar tipos de dados com cuidado para evitar confusão ou erros em programas mais complexos.

**Escopo de Variáveis**

O escopo de uma variável determina onde ela é acessível dentro do código. Variáveis definidas em um bloco principal são globalmente acessíveis, enquanto variáveis definidas dentro de funções são locais a essas funções, a menos que sejam explicitamente declaradas como `global`.

Entender variáveis e tipos de dados é essencial para programação em Python, pois permite manipular dados de maneira eficaz e criar programas dinâmicos e flexíveis. A capacidade de Python de inferir tipos de dados torna a linguagem acessível para iniciantes, ao mesmo tempo em que oferece poderosas funcionalidades para programadores experientes.

**Exercício 03: Refatore o exercício 02 atribuindo variáveis**

```python
print(len(input("Digite o seu nome: ")))
```

```
Qual é o seu nome? Luciano
7
```

## Questão: Cálculo de Bônus com Entrada do Usuário

Escreva um programa em Python que solicita ao usuário para digitar seu nome, o valor do seu salário mensal e o valor do bônus que recebeu. O programa deve, então, imprimir uma mensagem saudando o usuário pelo nome e informando o valor do salário em comparação com o bônus recebido.

![imagem](pic.png)

#### Instruções:

1. O programa deve começar solicitando ao usuário que insira seu nome.
2. Em seguida, o programa deve pedir ao usuário para inserir o valor do seu salário. Considere que este valor pode ser um número decimal.
3. Depois, o programa deve solicitar a porcentagem do bônus recebido pelo usuário, que também pode ser um número decimal.
4. O cálculo do KPI do bônus de 2024 é de `1000 + salario * bônus`
5. Finalmente, o programa deve imprimir uma mensagem no seguinte formato: "Olá [nome], o seu valor bônus foi de 5000".