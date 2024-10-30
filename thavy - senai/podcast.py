import sqlite3

class EpisodioPodcast:
    def __init__(self):
        self.conexao = self.criar_conexao()

    def criar_conexao(self):
        # Estabelecendo conexão e criando tabela
        conexao = sqlite3.connect("estudioPodcast.db")
        consulta = conexao.cursor()
        episodios = """
        CREATE TABLE IF NOT EXISTS episodios(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titulo VARCHAR(200),
        apresentador VARCHAR(100),
        duracao INTEGER,
        descricao VARCHAR(200),
        preco FLOAT
        );
        """
        consulta.execute(episodios)
        return conexao
    
    def cadastrarEpisodio(self, titulo, apresentador, duracao, descricao, preco):
        sql = "INSERT INTO episodios (titulo, apresentador, duracao, descricao, preco) VALUES (?, ?, ?, ?, ?)"
        campos = (titulo, apresentador, duracao, descricao, preco)
        consulta = self.conexao.cursor()
        consulta.execute(sql, campos)
        self.conexao.commit()
        print(consulta.rowcount, "Linha(s) inserida(s) com sucesso.")

    def consultarEpisodios(self):
        sql = "SELECT * FROM episodios"
        consulta = self.conexao.cursor()
        consulta.execute(sql)
        resultado = consulta.fetchall()
        if resultado:
            for episodio in resultado:
                print(f"Título: {episodio[1]}")
                print(f"Apresentador: {episodio[2]}")
                print(f"Duração: {episodio[3]}")
                print(f"Descrição: {episodio[4]}\n")
                print(f"Preço: {episodio[5]}\n")
        else:
            print("Nenhum espisódio cadastrado.")

    def deletarEpisodio(self, id):
        sql = "DELETE FROM episodios WHERE id = ?"
        consulta = self.conexao.cursor()
        consulta.execute(sql, (id,))
        self.conexao.commit()
        if consulta.rowcount > 0:
            print(f"Episódio com ID {id} excluído com sucesso.")
        else:
            print(f"Episódio não encontrado.")

    def atualizarEpisodio(self, id, titulo, apresentador, duracao, descricao, preco):
        consulta = self.conexao.cursor()
        consulta.execute("SELECT * FROM episodios WHERE id = ?", (id,))
        episodio = consulta.fetchone()
        
        if not episodio:
            print(f"Episódio com ID {id} não encontrado.")
            return
        
        novo_titulo = titulo if titulo.strip() else episodio[1]
        novo_apresentador = apresentador if apresentador.strip() else episodio[2]
        nova_duracao = duracao if duracao else episodio[3]
        nova_descricao = descricao if descricao.strip() else episodio[4]
        novo_preco = preco if preco else episodio[5]
        
        sql = "UPDATE episodios SET titulo = ?, apresentador = ?, duracao = ?, descricao = ?, preco = ? WHERE id = ?"
        campos = (novo_titulo, novo_apresentador, nova_duracao, nova_descricao, novo_preco, id)
        consulta.execute(sql, campos)
        self.conexao.commit()
        print(f"Episódio com ID {id} atualizado com sucesso.")

    def consultarEpisodioIndividual(self, id):
        sql = "SELECT * FROM episodios WHERE id = ?"
        consulta = self.conexao.cursor()
        consulta.execute(sql, (id,))
        resultado = consulta.fetchone()
        if resultado:
            print(f"Título: {resultado[1]}")
            print(f"Apresentador: {resultado[2]}")
            print(f"Duração: {resultado[3]}")
            print(f"Descrição: {resultado[4]}\n")
            print(f"Preço: {resultado[5]}\n")
        else:
            print("Episódio não encontrado.")

    def consultarEpisodiosPorDuracao(self, duracao_min, duracao_max):
        sql = "SELECT * FROM episodios WHERE duracao BETWEEN ? AND ?"
        consulta = self.conexao.cursor()
        consulta.execute(sql, (duracao_min, duracao_max))
        resultados = consulta.fetchall()
        
        if resultados:
            print(f"\nEpisódios com duração entre {duracao_min} e {duracao_max} minutos:")
            for episodio in resultados:
                print(f"ID: {episodio[0]}")
                print(f"Título: {episodio[1]}")
                print(f"Apresentador: {episodio[2]}")
                print(f"Duração: {episodio[3]} minutos")
                print(f"Descrição: {episodio[4]}")
                print(f"Preço: R$ {episodio[5]:.2f}")
        else:
            print(f"\nNenhum episódio encontrado com duração entre {duracao_min} e {duracao_max} minutos.")

    def calcularReceitaEsperada(self, id, estimativa_ouvintes):
        sql = "SELECT preco FROM episodios WHERE id = ?"
        consulta = self.conexao.cursor()
        consulta.execute(sql, (id,))
        resultado = consulta.fetchone()
        
        if resultado:
            preco = resultado[0]
            receita = preco * estimativa_ouvintes
            print(f"Receita esperada para o episódio: R$ {receita:.2f}")
        else:
            print("Episódio não encontrado.")

    def fechar_conexao(self):
        # Fechando a conexão ao final
        if self.conexao:
            self.conexao.close()