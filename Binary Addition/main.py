def add_binary(a, b):
    soma = a + b
    binary = bin(soma)
    return f"{binary.replace('0b', '')}"