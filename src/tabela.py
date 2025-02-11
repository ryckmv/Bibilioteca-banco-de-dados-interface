import pymysql
class Table:
    def __init__(self) -> None:
        self.TABLE_LIVROS = "livros"
        self.TABLE_USERS = "users"
        self.TABLE_EMPRESTIMOS = "emprestimos"
        self.TABLE_LIVROS_PDF="livros_pdf"

    def connect(self):
        connection = pymysql.connect(
            host='localhost',
            user='myuser',
            password='senha',
            database='mydb',
        )
        return connection

    # Função para criar e limpar tabelas
    def setup_tables(self):
        connection = self.connect()
        with connection:
            with connection.cursor() as cursor:
                # Desativar verificações de chave estrangeira
                cursor.execute("SET FOREIGN_KEY_CHECKS = 0;")
                
                # Criação das tabelas, se não existirem
                cursor.execute(
                    f"""
                    CREATE TABLE IF NOT EXISTS {self.TABLE_LIVROS} (
                        id INT PRIMARY KEY AUTO_INCREMENT,
                        titulo VARCHAR(255),
                        autor VARCHAR(255),
                        editora VARCHAR(255),
                        publicacao INT,
                        isbn VARCHAR(20)
                    )
                    """
                    
                )
                cursor.execute(
                    f"""
                    CREATE TABLE IF NOT EXISTS {self.TABLE_LIVROS_PDF} (
                        id INT PRIMARY KEY AUTO_INCREMENT,
                        nome_arquivo VARCHAR(255),
                        arquivo_pdf LONGBLOB
                    )"""

                )
                cursor.execute(
                    f"""
                    CREATE TABLE IF NOT EXISTS {self.TABLE_USERS} (
                        id INT PRIMARY KEY AUTO_INCREMENT,
                        nome VARCHAR(255),
                        sobrenome VARCHAR(255),
                        endereco VARCHAR(255),
                        email VARCHAR(255),
                        telefone VARCHAR(20)
                    )
                    """
                )
                
                cursor.execute(
                    f"""
                    CREATE TABLE IF NOT EXISTS {self.TABLE_EMPRESTIMOS} (
                        id INT PRIMARY KEY AUTO_INCREMENT,
                        id_livro INT,
                        id_usuario INT,
                        data_emprestimo DATE,
                        data_devolucao DATE,
                        FOREIGN KEY(id_livro) REFERENCES livros(id),
                        FOREIGN KEY(id_usuario) REFERENCES users(id)
                    )
                    """
                )
                
                # Limpeza das tabelas (CUIDADO: Isso limpa as tabelas)
                cursor.execute(f"SELECT 1 FROM information_schema.tables WHERE table_name = '{self.TABLE_EMPRESTIMOS}' LIMIT 1;")
                if cursor.fetchone():
                    cursor.execute(f'TRUNCATE TABLE {self.TABLE_EMPRESTIMOS}')
                
                cursor.execute(f"SELECT 1 FROM information_schema.tables WHERE table_name = '{self.TABLE_USERS}' LIMIT 1;")
                if cursor.fetchone():
                    cursor.execute(f'TRUNCATE TABLE {self.TABLE_USERS}')
                
                cursor.execute(f"SELECT 1 FROM information_schema.tables WHERE table_name = '{self.TABLE_LIVROS}' LIMIT 1;")
                if cursor.fetchone():
                    cursor.execute(f'TRUNCATE TABLE {self.TABLE_LIVROS}')
                
                # Reativar verificações de chave estrangeira
                cursor.execute("SET FOREIGN_KEY_CHECKS = 1;")
            connection.commit()

if __name__=='__main__':
    table=Table()
    table.setup_tables()