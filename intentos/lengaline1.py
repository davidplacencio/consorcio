#           n!
# nCm = --------------
#        m! (n - m)!

def custom_method(n, m):
    n_factorial = n
    m_factorial = m
    n_m_factorial = n - m

    for i in range(1, n):
        n_factorial *= i
    for i in range(1, m):
        m_factorial *= i
    for i in range(1, n - m):
        n_m_factorial *= i
    
    result = n_factorial / (m_factorial * n_m_factorial)
    mostrarformato(n, m, result)

def mostrarformato(n, m, result):
    print(f"""
                   {n}!
    {n}C{m} = -------------- = {result}
             {m}! ({n} - {m})!           
    """)
    

def main():
    n = int(input('ingrese valor de n: '))
    m = int(input('ingrese valor de m: '))

    custom_method(n,m)

if __name__ == '__main__':
    main()
