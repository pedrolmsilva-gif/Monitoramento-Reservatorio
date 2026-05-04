from colorama import Fore, Style, init

# Inicializa o colorama. 


# Lista de níveis (estruturada para fácil manutenção)
reservatorio_niveis = [
    {"nivel": 1, "situacao": "Muito baixo (crítico)", "cor": Fore.RED},
    {"nivel": 2, "situacao": "Baixo", "cor": Fore.YELLOW},
    {"nivel": 3, "situacao": "Médio", "cor": Fore.GREEN},
    {"nivel": 4, "situacao": "Alto", "cor": Fore.CYAN},
    {"nivel": 5, "situacao": "Muito alto (alerta)", "cor": Fore.BLUE}
]

def exibir_mensagem(nivel_informado):
    """
    Função que busca o nível na lista e imprime a mensagem com a cor definida.
    """
    # Procura o nível na nossa lista
    for item in reservatorio_niveis:
        if item["nivel"] == nivel_informado:
            print(f"{item['cor']}[Nível {item['nivel']}] - Situação: {item['situacao']}")
            return

    # Caso o nível informado não exista
    print(f"{Fore.WHITE}Nível {nivel_informado} inválido.")

def simular_sistema():
    """
    Simula o monitoramento passando por todos os níveis do reservatório.
    """
    print(f"{Style.BRIGHT}--- Sistema de Monitoramento de Água (ETEC) ---\n")
    
    # Percorre a lista e exibe cada status
    for i in range(1, 6):
        exibir_mensagem(i)
        
    print(f"\n{Style.BRIGHT}--- Monitoramento finalizado ---")

# Executa a simulação
if __name__ == "__main__":
    simular_sistema()