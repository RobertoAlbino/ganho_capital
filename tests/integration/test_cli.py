import os
import subprocess
import unittest


class TestCli(unittest.TestCase):
    def carregar_script(self):
        return os.path.abspath("ganho_capital/ganho_capital.py")

    def carregar_cenario(self, cenario):
        cenario = os.path.join(os.path.dirname(__file__), f"data/{cenario}.txt")
        with open(cenario, "r") as f:
            return f.read()

    def executar_script(self, cenario):
        return subprocess.run(
            ["python3", self.carregar_script()],
            input=self.carregar_cenario(cenario),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )

    def test_cenario_1(self):
        resultado = self.executar_script("cenario_1")
        esperado = (
            "[{'tax': '0.00'}, {'tax': '10000.00'}]\n"
            "[{'tax': '0.00'}, {'tax': '0.00'}]"
        )
        self.assertEqual(resultado.returncode, 0)
        self.assertEqual(resultado.stdout.strip(), esperado)

    def test_cenario_2(self):
        resultado = self.executar_script("cenario_2")
        esperado = "[{'tax': '0.00'}, {'tax': '0.00'}, {'tax': '0.00'}]"
        self.assertEqual(resultado.returncode, 0)
        self.assertEqual(resultado.stdout.strip(), esperado)

    def test_cenario_3(self):
        resultado = self.executar_script("cenario_3")
        esperado = "[{'tax': '0.00'}, {'tax': '10000.00'}, {'tax': '0.00'}]"
        self.assertEqual(resultado.returncode, 0)
        self.assertEqual(resultado.stdout.strip(), esperado)

    def test_cenario_4(self):
        resultado = self.executar_script("cenario_4")
        esperado = (
            "[{'tax': '0.00'}, {'tax': '0.00'}, {'tax': '0.00'}]\n"
            "[{'tax': '0.00'}, {'tax': '10000.00'}, {'tax': '0.00'}]"
        )
        self.assertEqual(resultado.returncode, 0)
        self.assertEqual(resultado.stdout.strip(), esperado)

    def test_cenario_5(self):
        resultado = self.executar_script("cenario_5")
        esperado = "[{'tax': '0.00'}, {'tax': '0.00'}, {'tax': '1000.00'}]"
        self.assertEqual(resultado.returncode, 0)
        self.assertEqual(resultado.stdout.strip(), esperado)

    def test_cenario_6(self):
        resultado = self.executar_script("cenario_6")
        esperado = "[{'tax': '0.00'}, {'tax': '0.00'}, {'tax': '0.00'}]"
        self.assertEqual(resultado.returncode, 0)
        self.assertEqual(resultado.stdout.strip(), esperado)

    def test_cenario_7(self):
        resultado = self.executar_script("cenario_7")
        esperado = (
            "[{'tax': '0.00'}, {'tax': '0.00'}, {'tax': '0.00'}, "
            "{'tax': '10000.00'}]"
        )
        self.assertEqual(resultado.returncode, 0)
        self.assertEqual(resultado.stdout.strip(), esperado)

    def test_cenario_8(self):
        resultado = self.executar_script("cenario_8")
        esperado = (
            "[{'tax': '0.00'}, {'tax': '0.00'}, {'tax': '0.00'}, "
            "{'tax': '0.00'}, {'tax': '3000.00'}]"
        )
        self.assertEqual(resultado.returncode, 0)
        self.assertEqual(resultado.stdout.strip(), esperado)

    def test_cenario_9(self):
        resultado = self.executar_script("cenario_9")
        esperado = (
            "[{'tax': '0.00'}, {'tax': '0.00'}, {'tax': '0.00'}, "
            "{'tax': '0.00'}, {'tax': '3000.00'}, {'tax': '0.00'}, "
            "{'tax': '0.00'}, {'tax': '3700.00'}, {'tax': '0.00'}]"
        )
        self.assertEqual(resultado.returncode, 0)
        self.assertEqual(resultado.stdout.strip(), esperado)

    def test_cenario_10(self):
        resultado = self.executar_script("cenario_10")
        esperado = (
            "[{'tax': '0.00'}, {'tax': '80000.00'}, {'tax': '0.00'}, "
            "{'tax': '60000.00'}]"
        )
        self.assertEqual(resultado.returncode, 0)
        self.assertEqual(resultado.stdout.strip(), esperado)

    def test_cenario_11(self):
        resultado = self.executar_script("cenario_11")
        esperado = "[{'tax': '0.00'}, {'tax': '0.00'}]"
        self.assertEqual(resultado.returncode, 0)
        self.assertEqual(resultado.stdout.strip(), esperado)
