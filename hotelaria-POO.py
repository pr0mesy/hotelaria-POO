class Fatura:
    def __init__(self, preco_diaria, quantidade_dias):
        self.preco_diaria = preco_diaria
        self.quantidade_dias = quantidade_dias
        self.valor_total = quantidade_dias * preco_diaria

    def gerar_fatura(self):
        valor_total = self.preco_diaria * self.quantidade_dias
        print(f"O total da fatura é R$ {valor_total:.2f}")

class Hotel:
    def __init__(self):
        print("Bem-vindo ao Hotel Infinity! ")
        self.quartos_disponiveis = {
        'A1': 'vago',
        'A2': 'vago',
        'A3': 'vago',
        'B1': 'vago',
        'B2': 'vago',
        'B3': 'vago',
    }
        self.preco_diaria = 90
        self.quantidade_dias = 0
    
    def listar(self):
        print("Quartos:")
        for key, status in self.quartos_disponiveis.items():
            print(f"{key} ({status})", end="  ")
        print()

    def reservar(self):
        Hotel.listar(self)
        while True:
            opcao = input("Digite o quarto para fazer a reserva: ")

            if opcao not in self.quartos_disponiveis:
                print("Digite uma opção válida: ")
            elif self.quartos_disponiveis[opcao] == 'reservado':
                print("Esse quarto já está reservado. ")
            else:
                self.quartos_disponiveis[opcao] = "reservado"
                print(f"Quarto reservado com sucesso! ")
                break

        self.quantidade_dias = int(input("Digite a quantidade de dias a se hospedar: "))

def menu():
    hot = Hotel()
    while True:
        opcao = input('''
        (1) - Reservar quarto
        (2) - Listar quartos
        (3) - Gerar fatura
        (4) - Sair

        ''')
         
        match opcao:
            case '1':
                hot.reservar()
            case '2':
                hot.listar()
            case '3':
                fatura1 = Fatura(hot.preco_diaria, hot.quantidade_dias)
                fatura1.gerar_fatura()
            case '4':
                print("Saindo...")
                break
            case _:
                print("Digite uma opção válida")

menu()