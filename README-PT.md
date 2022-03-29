<h1 align="center">
     <a> 101-Backend-Developer-Test-MercadoLivre </a>
</h1>

<h4 align="center">
	🚧 MAR/22 🚀 🚧
</h4>

## 💻 Sobre o teste

Teste realizado em MAR/2022 para posição de Backend Developer Junior, ML.

        Complete a seguinte função para que a mesma devolva todos os possíveis números de 4 dígitos, 
        onde cada um seja menor ou igual a <maxDigit>, e a soma dos dígitos de cada número gerado seja 21
        Exemplo maxDigit=6: 3666, 4566...

---

## ⚙️ Desenvolvimento da solução

- [x] **Explicando o main.py**:

  - [x] Criando uma variável input para que seja digitado um número de 1 a 9, 'maxDigit';
  - [x] O número digitado é atribuído para quatro variáveis que corresponde a posição de cada um dos algarismos deste número de 4 dígitos:
    - d1: posição 1 (milhar);
    - d2: posição 2 (centena);
    - d3: posição 3 (dezena);
    - d4: posição 4 (unidade);
  - [x] Estas variáveis são atribuídas a um objeto <numax> que correponde ao número de 4 dígitos;
  - [x] É criada uma lista chamada <numeros> para que o loop for atribua a ela todos os números que:
    - Forem maiores que 1000, que por sua vez é o menor número de 4 digitos existente;
    - Forem menores que o maior número de 4 dígitos possível a partir do número inicialmente digitado, 'maxDigit';
    - Soma dos quatro algarismos que compõe o número de 4 dígito for igual a 21;
  - [x] Ao final da execução do script, será nesta <listanumeros> que terá a relação de números de 4 digitos respondendo pergunta do desafio.

---

## 🛠 Tecnologias

As seguintes ferramentas foram usadas na construção do projeto:

#### **Linguagem escolhida**  ([Python](https://www.python.org/))

#### **Utilitários**

-   Editor:  **[PyCharm](https://www.jetbrains.com/pt-br/pycharm/download/#section=linux)**

---

## 📝 Licença

Este projeto esta sobe a licença [MIT](./LICENSE).

Feito com ❤️ por Felipe Möises 👋🏽 [Entre em contato!](https://www.linkedin.com/in/felipemoises/)

---

##  Versões do README

[Francês 🇫🇷](./README-FR.md)  |  [Inglês 🇺🇸](./README.md)
