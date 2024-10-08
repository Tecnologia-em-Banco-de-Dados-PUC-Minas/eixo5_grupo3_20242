import sys
import os
import logging

from dotenv import load_dotenv
import pandas as pd
from sqlalchemy import create_engine


log_format = '%(asctime)s - %(levelname)s - %(message)s'
logging.basicConfig(level=logging.INFO, format=log_format)
log = logging.getLogger(__name__)

load_dotenv()


def read_parquets(path: str) -> tuple[pd.DataFrame, str]:
    '''
    Função para ler arquivos parquets e retornar um único dataframe e seu respectivo nome,
    é esperado que os parquets tenham a mesma estrutura

    args:
        - path: caminho de diretório onde os parquets estão
    '''
    files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]

    dfs = []
    for file in files:
        tmp_df = pd.read_parquet(os.path.join(path, file))
        dfs.append(tmp_df)
    
    df = pd.concat(dfs, ignore_index=True)
    table_name = os.path.basename(os.path.normpath(path))
    
    msg = f'Tabela {table_name} criada (pandas DataFrame) com sucesso'
    log.info(msg)

    return df, table_name


class ConvertDatabase:
    def __init__(self):
        self.engine = self.create_con()


    def connection_string(self) -> str:
        '''
        Função para criar a string de conexão para o banco PostgreSQL
        baseado nos argumentos passados no arquivo .env
        '''
        host = os.getenv('DB_HOST')
        port = os.getenv('DB_PORT')
        user = os.getenv('DB_USER')
        pwd = os.getenv('DB_PWD')
        database = os.getenv('DB_DATABASE')
        return f'postgresql://{user}:{pwd}@{host}:{port}/{database}'


    def create_con(self):
        '''
        Função para criar a conexão no banco PostgreSQL usando SQLAlchemy
        '''
        try:
            engine = create_engine(self.connection_string())
            msg = 'Conectado ao banco PostgreSQL'
            log.info(msg)
            return engine
        except Exception as e:
            msg = f'Erro ao conectar ao banco - {e}'
            log.error(msg)
            sys.exit(1)


    def load_table(self, df: pd.DataFrame, table_name: str, schema_name: str) -> None:
        '''
        Função para carregar as tabelas, baseadas em pandas DataFrames,
        no banco passado pela engine, neste caso, o banco PostgreSQL

        args:
            - df: pandas DataFrame contendo os dados da tabela a ser carregada
            - table_name: nome da tabela no banco
            - schema_name: nome do esquema no banco
        '''
        try:
            with self.engine.connect() as connection:
                df.to_sql(name=table_name, schema=schema_name, con=connection, if_exists='replace', index=False)
            
            msg = f'Tabela {table_name} carregada no banco PostgreSQL com sucesso'
            log.info(msg)
        except Exception as e:
            msg = f'Erro ao carregar a tabela {table_name} no banco PostgreSQL - {e}'
            log.error(msg)


    def close_con(self) -> None:
        '''
        Função para encerrar a conexão com o banco
        '''
        self.engine.dispose()


if __name__ == '__main__':
    convert = ConvertDatabase()

    layer = 'bronze'
    base_path = f'datalake/{layer}/'
    
    for file in os.listdir(base_path):
        path = os.path.join(base_path, file)
        df, table_name = read_parquets(path)
        convert.load_table(df, table_name, layer)
    
    convert.close_con()
