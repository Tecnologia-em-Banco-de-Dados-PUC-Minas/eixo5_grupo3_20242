Para a coleta de dados iremos utilizar a técnica de web scraping, onde coletamos dados de um serviço web e disponibilizamos em outra ponta.   
O serviço web que iremos pegar os dados para o projeto é o site https://www.olympedia.org/, após coleta dos dados os mesmos serão salvos no formato csv dentro da camada raw do nosso datalake, que aqui está sendo representado pelo diretório [datalake](../datalake) na raiz do projeto.   
O scraping e a escrita dos dados serão feitos através da linguagem de programação Python.   

Os scripts de scrape podem ser encontrados no diretório [data_pipeline/extraction](../data_pipeline/extraction/) deste projeto.

Os dados coletados através do scrape podem ser encontrados no diretório [datalake/raw](../datalake/raw) deste projeto.

Abaixo temos a lista dos urls bases que foram utilizados no scrape e seus respectivos dados de retorno no datalake:

- https://www.olympedia.org/athletes
  - athlete_bios - dados biográficos dos atletas
  - athlete_results - resultados dos atletas nos jogos olímpicos
- https://www.olympedia.org/editions
  - editions - edições dos jogos olímpicos
- https://www.olympedia.org/sports
  - sports - lista dos esportes olímpicos
- https://www.olympedia.org/event_names
  - events - lista dos eventos olímpicos, sendo este uma subcategoria dos esportes
