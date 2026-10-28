"""Seus testes do Marco 3 (veja a seção 5 do ENUNCIADO_MARCO3.md).

Regras: pelo menos 4 testes seus (o exemplo abaixo não conta), uma docstring em cada teste
dizendo qual caso ele cobre, e floats comparados com assertAlmostEqual ou math.isclose, a não
ser que a igualdade exata seja justamente o que você quer testar.
"""
import unittest

from elevatoria.raizes import Bisseccao, Newton
from fornecido.hidraulica import fator_atrito_colebrook

class TestBisseccaoExemplo(unittest.TestCase):
    """Exemplo do formato. `Bisseccao` é código existente da base."""

    def test_raiz_na_ponta(self):
        """Se f(a) já é zero, a bissecção devolve a sem iterar."""
        resultado = Bisseccao().encontrar(lambda x: x - 1.0, 1.0, 3.0)
        self.assertEqual((resultado.raiz, resultado.iteracoes), (1.0, 0))


# Acrescente abaixo as suas classes de teste, começando pelos testes de regressão da
# issue #9 (escreva-os ANTES de corrigir o defeito e confirme que falham).
class TestNewton(unittest.TestCase):
    def test_newton_recalcula_derivada(self):
        """Verifica se Newton recalcula a derivada a cada iteração."""
        chamadas = []
        def derivada(x):
            chamadas.append(x)
            return 2 * x
        resultado = Newton(df=derivada).encontrar(lambda x: x**2 - 2, 0, 2)
        self.assertEqual(len(chamadas), resultado.iteracoes)

    def test_newton_converge_em_poucas_iteracoes(self):
        """Verifica se Newton resolve Colebrook em até 6 iterações."""
        resultado = fator_atrito_colebrook(1e4, 0.15e-3 / 0.20, Newton(tol=1e-12))
        self.assertTrue(resultado[1].convergiu)
        self.assertLessEqual(resultado[1].iteracoes, 6)
        
if __name__ == "__main__":
    unittest.main()
