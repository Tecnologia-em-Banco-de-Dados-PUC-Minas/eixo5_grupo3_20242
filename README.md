# Eixo-5
Arquitetura de Dados em Nuvem

# OLÍMPIADAS: ANÁLISE HISTÓRICA E PREVISÃO DOS PRÓXIMOS RESULTADOS
`Tecnologia em Banco de Dados - EAD`
`2024/2`

No Brasil, o esporte sempre foi muito popular e assistido por grande parte da nação. Por isso, iremos utilizar uma base de dados que contém informações detalhadas dos resultados das olimpíadas que já ocorreram, para podermos realizar previsões dos próximos resultados que ocorrerão nas próximas competições.
Para isso, utilizaremos dados da web com informações de quantidade de medalhas por tipo (ouro, prata e bronze), por país, por competição, por atleta, etc. Os dados serão coletados usando ferramentas de web scraping utilizando a linguagem Python para realizar a coletas dessas informações e iremos armazená-las na AWS, que fornece vários tipos de serviços para armazenamento de dados. Após feito a coleta dos dados, iremos utilizar técnicas de análise de dados para conseguirmos entender o comportamento dos dados históricos e, com isso, aplicar técnicas de machine learning para prevermos os próximos resultados.

## Integrantes
* Felipe Siman Nogueira
* Gabriel Alves Coelho
* Letícia Dumêt Passos
* Letícia Dumêt Passos
* Priscila Costa da Silva
* Vinícius Evangelista

## Orientador
* Cristiano Geraldo Teixeira Silva

# Documentação

| Etapa         | Atividades |
|  :----:   | ----------- |
| ETAPA 1        |[Documentação de Contexto](projeto/inicio_do_projeto.md) |

A análise de dados está presente em quase todas as áreas e nas competições esportivas está ganhando muita visibilidade, pelo volume de dados gerados e os benefícios que os mesmos podem gerar, quando analisados, para futuras competições e campeonatos. Através da coleta destes dados, é possível identificar padrões, prever resultados e otimizar a preparação dos atletas e times.
Iremos coletar dados das olimpíadas em um site e, por meio de uma técnica de web scraping, tratar e gravar esses dados em um banco de dados na nuvem utilizando os serviços da AWS. Os dados disponibilizados estão no site https://www.olympedia.org/ e a ferramenta que iremos utilizar para realizar essa coleta, tratamento e armazenamento dos dados será o Python. A base de dados escolhido possui informações de quantidade de medalhas por país, atleta e ano da competição, detalhando entre o tipo de medalha (ouro, prata e bronze).
Com o avanço da internet, cada vez mais temos dados disponíveis na web sem estrutura e, por isso, surgiu a técnica de web scraping, onde podemos extrair os dados nos sites disponíveis de forma automatizada e, assim, podemos organizar esses dados para facilitar a análise dos mesmos em outras ferramentas.
Após realizar a coleta dos dados, iremos aplicar técnicas de análise de dados para entender o comportamento das informações e, então, aplicar técnicas de machine learning para prever futuros resultados com base nos dados históricos analisados. As técnicas de machine learming estão ficando cada vez melhores graças ao avanço das IA's.
O objetivo final do trabalho será entregar um algoritmo que seja capaz de entender os dados fornecidos das olimpíadas e entregar uma probabilidade de um resultado ocorrer na próxima competição. Para isso, precisamos realizar vários treinamentos com o algoritmo de machine learning, onde o mesmo será capaz de entender os novos dados e realizar a análise da probabilidade de vitória de um país ou atleta em uma modalidade.


| ETAPA 2        |[Coleta de Dados](projeto/coleta_dados.md) |
| ETAPA 3        |[Pré-processamento](projeto/pre_processamento.md) |
| ETAPA 4        |[Aprendizagem de Máquina](projeto/aprendizado_maquina_rev.md)|
| ETAPA 5        |[Análise dos Resultados](projeto/analise_resultados.md) |
| ETAPA 6        |[Otimização](projeto/Otimizacao.md) |
