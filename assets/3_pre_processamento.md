Após a coleta dos dados e sua disponibilização na camada raw do nosso [datalake](../datalake/) é hora de fazermos o pré-processamento desses dados e disponibilizarmos na camada bronze.  
Para isso iremos utilizar a linguagem de programação Python, usando majoritariamente a biblioteca Pandas, para manipulação e transformação dos dados. 

Os scripts do pré-processamento de dados podem ser encontrados no diretório [data_pipeline/preprocessing](../data_pipeline/preprocessing/) deste projeto.

Os dados tratados e transformados podem ser encontrados no diretório [datalake/bronze](../datalake/bronze/) deste projeto.

Abaixo temos a lista dos tratamentos feitos em cada base de dados do projeto:

- **athlete_bios** - dados biográficos dos atletas
    - Retirada de caracteres especiais da coluna Used name com replace;
    - Divisão da coluna Measurements em altura (cm) e peso (kg);
    - Extração da data e local de nascimento e falecimento dos campos Born e Died, respectivamente;
    - Renomeação das colunas;
    - Ajuste dos nomes das colunas para snake case;
    - Filtro das colunas relevantes para o projeto.
- **athlete_results** - resultados dos atletas nos jogos olímpicos
    - Retirada de caracteres especiais e transformação em numérico da coluna Pos (colocação, posição, do atleta);
    - Extração do ano e temporada dos jogos no campo Games;
    - Criação de booleano, extraído do campo Games, indicando se o jogo foi na modalidade juvenil;
    - Renomeação das colunas;
    - Ajuste dos nomes das colunas para snake case;
    - Filtro das colunas relevantes para o projeto.
- **editions** - edições dos jogos olímpicos
    - Retirada de edições não relevantes para o projeto;
    - Separação dos dados de início e fim da competição da coluna Competition;
    - Formatação das colunas de data para tipagem date;
    - Criação de booleano indicando se a edição não aconteceu devido à ter ocorrido durante uma Guerra Mundial;
    - Renomeação das colunas;
    - Ajuste dos nomes das colunas para snake case;
    - Filtro das colunas relevantes para o projeto.
- **sports** - lista dos esportes olímpicos
    - Ajuste dos nomes das colunas para snake case;
    - Filtro das colunas relevantes para o projeto.
- **events** - lista dos eventos olímpicos, sendo este uma subcategoria dos esportes
    - Criação de booleano, extraído da coluna Event, indicando se o evento foi descontinuado;
    - Criação de booleano, extraído da coluna Discipline, indicando se o evento é sem medalha;
    - Ajuste dos nomes das colunas para snake case.
- **noc_regions** - de/para da sigla NOC com o nome do país
    - Ajuste dos nomes das colunas para snake case.
