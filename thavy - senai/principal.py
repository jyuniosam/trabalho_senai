from podcast import EpisodioPodcast

def exibir_menu():
    print("\n--- Menu de Gerenciamento de Podcast ---")
    print("1. Cadastrar Episódio")
    print("2. Consultar Todos os Episódios")
    print("3. Consultar Episódio Individual")
    print("4. Atualizar Episódio")
    print("5. Deletar Episódio")
    print("6. Consultar Episódios por Duração")
    print("7. Calcular Receita Esperada")
    print("8. Sair")

def main():
    podcast = EpisodioPodcast()
    
    # Loop principal do programa
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")
        
        # Opção 1: Cadastrar novo episódio
        if opcao == '1':
            titulo = input("Título do episódio: ")
            apresentador = input("Nome do apresentador: ")
            
            try:
                duracao = int(input("Duração do episódio (em minutos): "))
            except ValueError:
                print("Por favor, digite uma duração válida (número inteiro)")
                continue
                
            descricao = input("Descrição do episódio: ")
            
            try:
                preco = float(input("Preço do episódio: "))
            except ValueError:
                print("Por favor, digite um preço válido (número decimal)")
                continue
            
            podcast.cadastrarEpisodio(titulo, apresentador, duracao, descricao, preco)
        
        # Opção 2: Listar todos os episódios
        elif opcao == '2':
            print(f"\n--- Lista de Episódios ---")
            podcast.consultarEpisodios()
        
        # Opção 3: Consultar episódio específico
        elif opcao == '3':
            try:
                id = int(input("Digite o ID do episódio: "))
                print(f"\n--- Informações do Episódio ---")
                podcast.consultarEpisodioIndividual(id)
            except ValueError:
                print("Por favor, digite um ID válido (número inteiro)")
                continue
        
        # Opção 4: Atualizar dados de um episódio
        elif opcao == '4':
            try:
                id = int(input("Digite o ID do episódio que deseja atualizar: "))
            except ValueError:
                print("Por favor, digite um ID válido (número inteiro)")
                continue
            
            titulo = input("Novo título (deixe em branco para não alterar): ")
            apresentador = input("Novo apresentador (deixe em branco para não alterar): ")
            duracao = input("Nova duração (deixe em branco para não alterar): ")
            descricao = input("Nova descrição (deixe em branco para não alterar): ")
            preco = input("Novo preço (deixe em branco para não alterar): ")

            if duracao:
                try:
                    duracao = int(duracao)
                except ValueError:
                    print("Por favor, digite uma duração válida (número inteiro)")
                    continue
            
            if preco:
                try:
                    preco = float(preco)
                except ValueError:
                    print("Por favor, digite um preço válido (número decimal)")
                    continue
            
            podcast.atualizarEpisodio(id, titulo, apresentador, duracao, descricao, preco)
        
        # Opção 5: Deletar um episódio
        elif opcao == '5':
            try:
                id = int(input("Digite o ID do episódio que deseja deletar: "))
                podcast.deletarEpisodio(id)
            except ValueError:
                print("Por favor, digite um ID válido (número inteiro)")
                continue
        
        # Opção 6: Consultar episódios por duração
        elif opcao == '6':
            try:
                duracao_min = int(input("Digite a duração mínima (em minutos): "))
                duracao_max = int(input("Digite a duração máxima (em minutos): "))
                podcast.consultarEpisodiosPorDuracao(duracao_min, duracao_max)
            except ValueError:
                print("Por favor, digite durações válidas (números inteiros)")
                continue
        
        # Opção 7: Calcular receita esperada
        elif opcao == '7':
            try:
                id = int(input("Digite o ID do episódio: "))
                estimativa_ouvintes = int(input("Digite a estimativa de ouvintes: "))
                podcast.calcularReceitaEsperada(id, estimativa_ouvintes)
            except ValueError:
                print("Por favor, digite valores válidos (números inteiros)")
                continue
        
        # Opção 8: Sair do programa
        elif opcao == '8':
            print("Fim do sistema")
            podcast.fechar_conexao()
            break
        
        # Opção inválida
        else:
            print("Opção inválida. Tente novamente.")

# Verifica se este arquivo está sendo executado diretamente
if __name__ == '__main__':
    main()