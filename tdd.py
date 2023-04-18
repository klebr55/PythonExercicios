import unittest  # Importa o módulo unittest, que permite escrever testes automatizados em Python.

class TestPar(unittest.TestCase):  # Cria uma classe que herda da classe TestCase do módulo unittest.
    def test_par(self):  # Define um método de teste, que verifica se a função eh_par retorna o resultado correto.
        self.assertTrue(eh_par(2))  # Verifica se a função retorna True para o número 2 (que é par).
        self.assertFalse(eh_par(3))  # Verifica se a função retorna False para o número 3 (que é ímpar).

def eh_par(num):  # Define a função eh_par, que recebe um número como parâmetro e verifica se ele é par.
    return num % 2 == 0  # Retorna True se o número for par e False se for ímpar.

if __name__ == '__main__':  # Verifica se o arquivo está sendo executado diretamente (e não importado como um módulo).
    unittest.main()  # Roda os testes automatizados definidos na classe TestPar.