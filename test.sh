clear

echo "************ Executando testes unitários ************"
python3 -m unittest -v tests/unit/calculadora_imposto_test.py
python3 -m unittest -v tests/unit/transacoes_test.py
python3 -m unittest -v tests/unit/valor_monetario_test.py

echo "************ Executando testes de integração ************"
python3 -m unittest -v tests/integration/test_cli.py

