1) MNIST é o mais fácil de todos, pois as imagens são simples, sem muita variação entre a mesma classe, em tons de cinza e tamanho não muito grande, e com fundo uniforme.
MNIST FASHION é mais difícil que MNIST, pois as imagens são mais complexas, possuíndo mais variação dentro de classes.
CIFAR-10 é mais difícil que MNIST FASHION, pois as imagens são maiores e tem cor e existem menos imagens no todo, além de que as classes possuem ainda mais variação com fundos diferentes e objetos com mais diferenças por classe.
CIFAR-100 é mais difícil que CIFAR-10, sendo assim o mais difícil de todos, por possuir 10x mais classes com o mesmo número total de imagens, tornando mais difícil que o modelo acerte a classe com a mesma frequência, já que cada uma tem 10x menos imagens para serem usadas no treinamento.

2) Características obsevadas nos testes com variações dos hiperparâmetros e configuração da estrutura da rede:
Extras adicionados: Variação da taxa de aprendizado em 2 deles, uso de dropout e normalização.

MNIST: Consiste em 70000 imagens 28x28 em tons de cinza com 10 classes ao todo. 60000 imagens são de treinamento e 10000 de teste.
Utilizar kernels de tamanhos diferenciados permitiu a detecção de uma range maior de padrões, aumentando a acurácia.
Aumentar ou diminuir o número de neurônios diminuiu a acurácia.
A utilização de dropout antes da última cada com valor de 0,5 ajuda a controlar o overfitting.
A lerning rate em 0.0001 melhorou a acurácia comparado com valores maiores e menores.
A normalização constante dos dados aumentou a acurácia.

FASHION MNIST: Consiste em 7000 imagens 28x28 em tons de cinza com 10 classes ao todo. 60000 imagens são de treinamento e 10000 de teste. 
Todos os comportamentos de MNIST se reptem aqui, porém os valores dos filtros e de neurônios foram escalados para lidar com a maior variedade por classe.
Duas camadas de convolução com kernels 5x5 e 3x3 se mostraram melhores para aumento da acurácia.

CIFAR-10: Consiste em 60000 imagens 32x32 coloridas em 10 classes, cada uma com 6000 imagens. 50000 são de treinamento e 10000 de teste.
Todas tentativas de mudança do tamanho do kernel de convolução diminuiram a acurácia 
O número de filtros encontrado e o número de neurônios foram o sweet spot encontrado entre overfitting e underfitting, com testes com valores maiores e menores gerando resultados piores.
A ordem do número de filtros gera melhor acurácia quando é crescente.
A normalização aumentou a acurácia.


CIFAR-100: Consiste em 60000 imagens 32x32 coloridas em 10 classes, cada uma com 600 imagens. 50000 são de treinamento e 10000 de teste.
As características observadas no CIFAR-10 se mantém, com comportamentos semelhantes mas hiperparametros escalados para lidar com o maior tamanho do problema, mas com algumas outras diferenças:
A utilização de dropout antes da última cada com valor de 0,5 ajuda a controlar o overfitting.
O número de filtros teve que ser duplicado pois não era o suficiente com os valores do CIFAR-10.



Fontes:
https://www.baeldung.com/cs/batch-normalization-cnn
https://www.cs.toronto.edu/~kriz/cifar.html
https://www.kdnuggets.com/2019/12/5-techniques-prevent-overfitting-neural-networks.html

