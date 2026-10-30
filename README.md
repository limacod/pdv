# PONTO DE VENDA (PDV)
O objetivo desse algoritmo consiste no desenvolvimento de um sistema de ponto de venda (PDV), na linguagem PYTHON.
O sistema funciona com duas regras de descontos, no qual aplica um desconto no valor da compra do cliente com base na sua idade e valor da compra, além disso o principal objetivo é registrar as comprar e apresentar os resultados ao fim do dia.

FUNCIONAMENTO: 

A logica usada no código funciona com um loop "while" que recebe o primeiro "input" que solicita o valor da compra do cliente, após isso o algoritmo faz o primeiro teste, se o valor informado for igual a "0" o sistema aciona o "break" e encerra o loop, finalizando o algoritmo e apresentando os resultados dia, total de compras, total bruto, valores dos descontos aplicado e o valor final.
Dando sequência no código, se o valor da compra ele for superior a 0 o algoritmo dará sequencia e a segunda entrada de dados vai solicitar a idade do cliente, se a idade do cliente for maior ou igual a 65 o valor da compra recebera um desconto de 20%, ou seja, o valor da compra * 0,8. Após o primeiro desconto ser aplicado, o próximo "IF" vai verificar se o valor continua maior que R$ 100, se a condição for verdadeira será aplicado um desconto de 10%, ou seja, valor da compra * 0.90. Se a idade do cliente for inferior a 65 o algoritmo verificará se o valor atende a condição do desconto de 10%.
Para finalizar o algoritmo print o valor da compra, total de descontos e o valor final da compra, após isso o sistema adiciona o valor da compra, desconto e o valor final em uma lista com a finalidade de ver quantas compras foram realizadas no fim do dia.
O sistema atende seu objetivo principal ao final do código mostrando a quantidade de compras realizadas no dia, o total bruto, o total de descontos e o total final.

para rodar usa-se o comando "python .\pdv.py" no terminal.

tabela de exemplos:

Caso	Valor (R$)	Idade    	Desconto Idade	  Desconto Valor	  Valor Final Esperado
  1	     50.00    	30	        0%	              0%	                  R$ 50.00
  2	    100.00	    30        	0%	              0%	                  R$ 100.00
  3	    80.00	      65	        20%	              0%                  	R$ 64.00
  4	    100.00	    70	        20%              	0%	                  R$ 80.00
  5	    125.00	    70	        20%	              0%	                  R$ 100.00
  6    	200.00	    30	        0%	              10%	                  R$ 180.00
  7    	100.00	    30	        0%	              10%	                  R$ 90.00
  8	    200.00	    65	        20%              	10%	                  R$ 144.00
  9	    1000.00	    80	        20%	              10%	                  R$ 720.00
  10	  200.00	    64	        0%	              10%	                  R$ 180.00
