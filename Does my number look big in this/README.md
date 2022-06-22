# Description:

A Narcissistic Number is a positive number which is the sum of its own digits, each raised to the power of the number of digits in a given base. In this Kata, we will restrict ourselves to decimal (base 10).

For example, take 153 (3 digits), which is narcisstic:

    1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153

and 1652 (4 digits), which isn't:

    1^4 + 6^4 + 5^4 + 2^4 = 1 + 1296 + 625 + 16 = 1938

## The Challenge:

Your code must return true or false (not 'true' and 'false') depending upon whether the given number is a Narcissistic number in base 10. This may be True and False in your language, e.g. PHP.

Error checking for text strings or other invalid inputs is not required, only valid positive non-zero integers will be passed into the function.

# Descrição:

Um número narcisista é um número positivo que é a soma de seus próprios dígitos, cada um elevado à potência do número de dígitos em uma determinada base. Neste Kata, vamos nos restringir ao decimal (base 10).

Por exemplo, tome 153 (3 dígitos), que é narcisista:

    1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153

e 1652 (4 dígitos), que não é:

    1^4 + 6^4 + 5^4 + 2^4 = 1 + 1296 + 625 + 16 = 1938
    
## O desafio:

Seu código deve retornar true ou false (não 'true' e 'false') dependendo se o número fornecido é um número narcisista na base 10. Isso pode ser True e False em seu idioma, por exemplo. PHP.

A verificação de erros para strings de texto ou outras entradas inválidas não é necessária, apenas inteiros positivos diferentes de zero válidos serão passados ​​para a função.