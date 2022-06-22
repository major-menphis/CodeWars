def narcissistic(n):
    """Função para testar se um número inteiro é nascisista ou não

    Args:
        n (integer): insira o numero a ser testado

    Returns:
        boolean: retorna 'True' se o número inteiro n é um número narcisista
        caso contrário retorna 'False'
    """
    digits = len(str(n)) #transforma u número em string e conta seus digitos
    result = 0
    for i in str(n): # realiza o laço de repetição com o numero convertido em string
        r_potency = int(i) ** digits # realiza potenciação em cada numero separado
        result += r_potency # soma o resultado de cada repetição ao total
    if result == n: # testa se o total é igual ao numero inserido
        return True
    else:
        return False