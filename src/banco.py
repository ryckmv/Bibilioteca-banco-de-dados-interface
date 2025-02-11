import pymysql
from tabela import Table

class Biblioteca(Table):

    def __init__(self):
        super().__init__()
        


    # Função para inserir livro
    def insert_book(self, titulo, autor, editora, publicacao, isbn):
        connection = self.connect()
        try:
            with connection.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO livros (titulo, autor, editora, publicacao, isbn) VALUES (%s, %s, %s, %s, %s)",
                    (titulo, autor, editora, publicacao, isbn)
                )
            connection.commit()
            print("Livro inserido com sucesso")
        except pymysql.MySQLError as e:
            print("Erro ao inserir livro no MySQL", e)
        finally:
            connection.close()


     #inserir PDF
    def insert_pdf(self,nome,i):
        connection = self.connect()
        try:
            with connection.cursor() as cursor:
                with open(f"c:/Users/rick_/OneDrive/Desktop/pdf/{i}", "rb") as file:
                    binario = file.read()
                cursor.execute(
                    "INSERT INTO livros_pdf (nome_arquivo, arquivo_pdf) VALUES ( %s, %s)",
                    (nome, binario)
                )
            connection.commit()
            print("Livro inserido com sucesso")
        except pymysql.MySQLError as e:
            print("Erro ao inserir livro no MySQL", e)
        finally:
            connection.close()

    # Função para inserir usuário
    def insert_user(self, nome, sobrenome, endereco, email, telefone):
        connection = self.connect()
        try:
            with connection.cursor() as cursor:
                cursor.execute(
                    f"INSERT INTO {self.TABLE_USERS} (nome, sobrenome, endereco, email, telefone) VALUES (%s, %s, %s, %s, %s)",
                    (nome, sobrenome, endereco, email, telefone)
                )
            connection.commit()
            print("Usuário inserido com sucesso")
        except pymysql.MySQLError as e:
            print("Erro ao inserir usuário no MySQL", e)
        finally:
            connection.close()
    
    

    def exibir_livros(self):
        connection = self.connect()
        try:
            with connection.cursor() as cursor:
                cursor.execute(f"SELECT * FROM {self.TABLE_LIVROS}")
                self.resultado = cursor.fetchall()
                for livro in self.resultado:
                    print(f'ID: {livro[0]}')
                    print(f'Titulo: {livro[1]}')
                    print(f'Autor: {livro[2]}')
                    print(f'Editora: {livro[3]}')
                    print(f'Ano de Publicação: {livro[4]}')
                    print(f'ISBN: {livro[5]}')
                    print('\n')
        finally:
            connection.close()




    
    def insert_emprestimo(self, id_livro, id_usuario, data_emprestimo, data_devolucao):
        connection = self.connect()
        try:
            with connection.cursor() as cursor:
                cursor.execute(f'INSERT INTO {self.TABLE_EMPRESTIMOS}(id_livro, id_usuario, data_emprestimo, data_devolucao) VALUES(%s, %s, %s, %s)', (id_livro, id_usuario, data_emprestimo, data_devolucao)
                               )
            connection.commit()
            print("loan inserido com sucesso")
        except pymysql.MySQLError as e:
            print("Erro ao inserir usuário no MySQL", e)
        finally:
            connection.close()
    #exibir livros emprestados
    def get_books_on_loan(self):
        connection = self.connect()
        try:
            with connection.cursor() as cursor:
                result= f"""
                        SELECT livros.titulo, users.nome, users.sobrenome, emprestimos.data_emprestimo, emprestimos.data_devolucao
                        FROM livros
                        INNER JOIN  emprestimos ON livros.id = emprestimos.id_livro
                        INNER JOIN  users ON users.id = emprestimos.id_usuario
                        WHERE emprestimos.data_devolucao IS NULL
                        """
                cursor.execute(result)
                result = cursor.fetchall()
                connection.commit()
                for i in result:
                    print(i)
        except pymysql.MySQLError as e:
            print("Erro ao inserir usuário no MySQL", e)
        finally:
            connection.close()

        return result
    

    

if __name__=='__main__':
    # Criação da instância da classe Biblioteca
    biblioteca = Biblioteca()

    # Configuração inicial das tabelas


    # Inserir um livro
    biblioteca.insert_book('Homem Aranha', 'Joao', 'Carvalho', 1994, '12349')
    biblioteca.insert_book('Homem Aranha 2', 'Joao', 'Carvalho', 1996, '12347')


    # Inserir um usuário
   
    biblioteca.insert_emprestimo(1, 1, '2024-08-11', None)
    biblioteca.get_books_on_loan()

    # Exibir livros
    biblioteca.exibir_livros()
  
    biblioteca.insert_pdf('programação','programacao.pdf')
