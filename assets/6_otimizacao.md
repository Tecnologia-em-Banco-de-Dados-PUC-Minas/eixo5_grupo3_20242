Com uma vasta quantidade de dados sobre Olimpíadas - atletas, resultados, esportes, NOC - seria de grande valia a criação de um Data Viz, afim de visualizarmos de forma gráfica e intuitiva a grandeza que esses dados nos tem para oferecer.  
Adotando a estratégia de um Datalake medalhão, teriamos como ponto de partida a camada bronze - pré-processamento dos dados - onde iriamos fazer tratamentos e manipulações de dados via SQL para popularmos assim as camadas silver e gold.  
Introduzindo softwares de governança de dados, como OpenMetadata ou Astera, teríamos uma forte documentação e controle dos dados trabalhados e introduzidos no projeto.

Alguns pontos de otimizações para com a aprendizagem de máquina está em expandi-la para as outras categorias de jogos olímpicos - esportes e eventos - dada a boa acurácia que tivemos utilizando a categoria de Tênis Individual Masculino.  
Outro ponto de melhoria também seria a melhor normalização dos dados e uso de outros dados relevantes aos atletas e resultados para com o aprendizado via Naive Bayes, melhorando o 1º quadrante (verdadeiro positivo) da matriz de confusão, onde há a assertividade da previsão do real atleta campeão medalhista, isto é, a previsão dizer que o atleta será campeão medalhista e ele realmente for.

Assim, otimizando a aprendizagem de máquina, teremos um ótimo algoritmo de previsão de medalhistas olímpicos para os próximos jogos.
