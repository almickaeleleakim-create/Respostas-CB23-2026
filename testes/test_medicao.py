"""Seus testes do Marco 2 (veja a seção 5 do ENUNCIADO_MARCO2.md).

Regras: pelo menos 4 testes seus (o exemplo abaixo não conta), uma docstring em cada teste
dizendo qual caso ele cobre, e floats comparados com assertAlmostEqual, math.isclose ou
np.allclose, a não ser que a igualdade exata seja justamente o que você quer testar.
"""
import unittest

from elevatoria.acumuladores import AcumuladorIngenuo,AcumuladorKahan


class TestAcumuladorIngenuoExemplo(unittest.TestCase):
    """Exemplo do formato. `AcumuladorIngenuo` é código existente da base."""

    def test_sem_parcelas(self):
        """Sem nenhuma parcela, o total é zero."""
        self.assertEqual(AcumuladorIngenuo().total, 0.0)


# Acrescente abaixo as suas classes de teste, começando pelos testes de regressão da
# issue #7 (escreva-os ANTES de corrigir o defeito e confirme que falham).
class TestAcumuladorKahan(unittest.TestCase):
    """Regressão da issue #7: o AcumuladorKahan não compensava o arredondamento."""
 
    def test_um_milhao_de_pulsos(self):
        """1 000 000 de parcelas de 0,1 L devem somar exatamente 100000.0, e não 100000.00000133288"""
        acumulador = AcumuladorKahan()
        acumulador.adicionar_todos([0.1] * 1_000_000)
        self.assertEqual(acumulador.total, 100000.0)
 
    def test_erro_do_kahan_e_bem_menor_que_o_do_ingenuo(self):
        """Com 100_000 parcelas de 0,1 L, o erro do Kahan é no mínimo 1000 vezes menor."""
        ingenuo, kahan = AcumuladorIngenuo(), AcumuladorKahan()
        for acumulador in (ingenuo, kahan):
            acumulador.adicionar_todos([0.1] * 100_000)
        erro_ingenuo = abs(ingenuo.total - 10_000.0)
        erro_kahan = abs(kahan.total - 10_000.0)
        self.assertGreater(erro_ingenuo, 0.0)
        self.assertLessEqual(erro_kahan, erro_ingenuo / 1000)

if __name__ == "__main__":
    unittest.main()
