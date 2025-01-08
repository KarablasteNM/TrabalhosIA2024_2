Angelo Fernandes Oliveira - 00550162 - Turma B
Augusto Mattei Grohmann - 00550429 - Turma A
Nathan Mattes - 00342941 - Turma A

Item 2.2:
A) i)	Rodamos três vezes, na primeira o nosso agente venceu do randomplayer; 
Na segunda, tivemos um empate;
E na terceira, nosso agente venceu de novo.
Entretanto, nas duas vezes que vencemos, vencemos por erro do randomplayer, pois em ambas ainda tinha dois locais que o randomplayer poderia jogar, sendo que um nos faria empatar e outro nos faria vencer (e em ambas as situações ele inseriu no espaço que nos faria vencer).

ii) Para esse teste, também rodamos três vezes. Na primeira obtivemos empate;
Na segunda tentativa também houve empate (inclusive teve exatamente o mesmo resultado);
E na terceira também tivemos um empate com os exatos mesmos resultados.

iii) Para os testes contra os players, fizemos um pouco mais de 20 testes. Em todos que o primeiro a jogar era o minimax, obtivemos empate. Em todos que os players eram os primeiros a jogar, perdemos para o agente (isso nos preocupou um pouco a respeito do nosso raciocínio).

B)
Partidas:
Contagem de peças X Valor posicional: 18x17 (Contagem de peças)
Valor posicional X Contagem de peças: 26x38 (Contagem de peças)
Contagem de peças X Heurística customizada: 22x13 (Contagem de peças)
Heurística customizada X Contagem de peças: 13x23 (Contagem de peças)
Valor posicional X Heurística customizada: 16x7 (Valor posicional)
Heurística customizada X Valor posicional: 12x7 (Customizada)
Monte Carlo x Contagem de peças: 40 x 24 (Monte Carlo)
Monte Carlo x Valor posicional: 45 x 19 (Monte Carlo)
Monte Carlo x Heurística customizada: 37 x 27 (Monte Carlo)
Contagem de peças x Monte Carlo: 8 x 56 (Monte Carlo)
Valor posicional x Monte Carlo: 28 x 36 (Monte Carlo)
Heurística customizada x Monte Carlo: 21 x 43 (Monte Carlo)

A melhor implementação, com exceção do extra (MCTS) foi de longe a de contagem de peças, que venceu 4 dos 6 jogos, sendo a grande maioria de “lavada”, apenas chegou perto de perder em uma das partidas contra o valor posicional.
A Monte Carlo por sua vez venceu todas as outras quando adicionada ao torneio.
Apenas para fazer um teste extra, colocamos cada heurística contra si mesma, esses foram os resultados:

Contagem X Contagem: 59 X 5
Valor X Valor: 12 X 7
Custom X Custom: 13 X 14
MCTS x MCTS: 46 x 18


Demais considerações:
A implementação customizada foi elaborada a partir de sujestões fornecidas pelo ChatGPT e melhorias propostas pelos membros da equipe.
A implementação escolida para o torneio foi a Monte Carlo, visto que é a mais avançada detre as heurísticas estudadas em aula.

Extras:
Foi implementado o MCTS com o auxílio do ChatGPT para se obter uma base para o código, que foi retrabalhado até chegar no estado que foi entregue.

