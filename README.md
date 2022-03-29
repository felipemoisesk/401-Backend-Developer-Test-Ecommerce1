<h1 align="center">
     <a> 101-Backend-Developer-Test-MercadoLivre </a>
</h1>

<h4 align="center">
	🚧 MAR/22 🚀 🚧
</h4>

## 💻 About the test

Test accomplished in MAR/2022 for the role of Backend Developer Junior, ML.

        Complete the following function so that it returns all possible 4-digit numbers, 
        where each is less than or equal to <maxDigit>, and the sum of the digits of each generated number is 21
        Exemple maxDigit=6: 3666, 4566...

---

## ⚙️ Solution development

- [x] **Explaining main.py**:

  - [x] Creating an input variable to type a number from 1 to 9, 'maxDigit';
  - [x] The number entered is assigned to four variables that correspond to the position of each digit of this 4-digit number:
    - d1: position 1 (thousand);
    - d2: position 2 (hundred);
    - d3: position 3 (ten);
    - d4: position 4 (unit);
  - [x] These variables are assigned to a <numax> object that corresponds to the 4-digit number;
  - [x] A list called <numbers> is created so that the for loop assigns to it all numbers that:
    - Are greater than 1000, which in turn is the smallest 4-digit number available;
    - Are smaller than the largest possible 4-digit number from the number initially entered, 'maxDigit';
    - Sum of the four digits that make up the 4-digit number is equal to 21;
  - [x] At the end of the script execution, it will be in this <listanumers> that will have the list of 4-digit numbers answering the challenge question.

---

## 🛠 Technologies

The tools were used in building the project:

#### **Language chosen** ([Python](https://www.python.org/))

#### **Utilities**

- Editor: **[PyCharm](https://www.jetbrains.com/pt-br/pycharm/download/#section=linux)**

---

## 📝 License

This project is licensed under [MIT](./LICENSE).

Made with ❤️ by Felipe Möises 👋🏽 [Get in touch!](https://www.linkedin.com/in/felipemoises/)

---

## README version

[Francês 🇫🇷](./README-FR.md)  |  [Portuguese 🇧🇷](./README-PT.md)
