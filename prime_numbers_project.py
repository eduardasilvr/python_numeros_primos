def is_prime(num):
    """Função para verificar se um número é primo."""
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def generate_prime_numbers(start, end):
    """Função para gerar uma lista de números primos em um intervalo."""
    primes = []
    for num in range(start, end + 1):
        if is_prime(num):
            primes.append(num)
    return primes

def main():
    # Solicita ao usuário para definir o intervalo
    start = int(input("Digite o valor inicial do intervalo: "))
    end = int(input("Digite o valor final do intervalo: "))

    # Gera e exibe a lista de números primos
    prime_numbers = generate_prime_numbers(start, end)
    print(f"Números primos no intervalo de {start} a {end}: {prime_numbers}")

if __name__ == "__main__":
    main()
