# Representando cada cartão/paciente da lista
class Nodo:
    def __init__(self, numero, cor):
        self.numero = numero
        self.cor = cor
        self.proximo = None


# Classe que controla a lista
class ListaEspera:
    def __init__(self):
        self.head = None  # Primeiro paciente da fila
        # Numeros iniciais dos cartões
        self.proximoVerde = 1
        self.proximoAmarelo = 201

    # Coloca um paciente verde no final da lista
    def inserirSemPrioridade(self, nodo):
        atual = self.head
        # Percorre a lista até encontrar o último paciente
        while atual.proximo is not None:
            atual = atual.proximo
        # O último passa a apontar para o novo paciente
        atual.proximo = nodo

    # Coloca um paciente amarelo depois de todos os amarelos, mas antes de todos os verdes
    def inserirComPrioridade(self, nodo):
        atual = self.head
        anterior = None
        # Percorre somente os pacientes amarelos
        while atual is not None and atual.cor == "A":
            anterior = atual
            atual = atual.proximo
        # Se não tem amarelo, o novo vira o primeiro
        if anterior is None:
            nodo.proximo = self.head
            self.head = nodo
        # Se tem amarelos, coloca depois do ultimo amarelo
        else:
            nodo.proximo = atual
            anterior.proximo = nodo

    # Pede a cor, gera o número e adiciona o paciente
    def inserir(self):
        cor = input("Informe a cor do cartão (A ou V): ").upper()
        # Continua perguntando enquanto a cor for inválida
        while cor != "A" and cor != "V":
            print("Cor inválida. Digite apenas A ou V.")
            cor = input("Informe a cor do cartão (A ou V): ").upper()
        # Gera automaticamente o número do cartão
        if cor == "V":
            numero = self.proximoVerde
            self.proximoVerde += 1
        else:
            numero = self.proximoAmarelo
            self.proximoAmarelo += 1
        # Cria novo paciente
        novoNodo = Nodo(numero, cor)
        # Se a lista estiver vazia, ele vira o primeiro paciente
        if self.head is None:
            self.head = novoNodo
        # Pacientes verdes vão para o final
        elif cor == "V":
            self.inserirSemPrioridade(novoNodo)
        # Pacientes amarelos recebem prioridade
        else:
            self.inserirComPrioridade(novoNodo)

        print(f"Paciente com cartão {cor}{numero} adicionado à fila.")

    # Mostra todos os pacientes na ordem de atendimento
    def imprimirListaEspera(self):
        if self.head is None:
            print("A fila está vazia.")
            return
        atual = self.head

        print("\n--- Pacientes na fila ---")
        # Percorre a lista do primeiro até o último paciente
        while atual is not None:
            print(f"Cartão: {atual.cor}{atual.numero}")
            atual = atual.proximo

    # Remove e chama o primeiro paciente da fila
    def atenderPaciente(self):
        if self.head is None:
            print("Não há pacientes na fila.")
            return
        # Guarda o primeiro paciente
        paciente = self.head
        # O próximo paciente passa a ser o primeiro da fila
        self.head = self.head.proximo
        # Desliga o paciente removido da lista
        paciente.proximo = None

        print(
            f"Paciente com cartão {paciente.cor}{paciente.numero}, "
            "dirija-se para o atendimento."
        )


# Criando a fila
fila = ListaEspera()
# Mantém o menu funcionando até o usuário escolher sair
while True:
    print("\n--- SISTEMA DE TRIAGEM ---")
    print("1 - Adicionar paciente à fila")
    print("2 - Mostrar pacientes na fila")
    print("3 - Chamar paciente")
    print("4 - Sair")
    opcao = input("Escolha uma opção: ")
    if opcao == "1":
        fila.inserir()
    elif opcao == "2":
        fila.imprimirListaEspera()
    elif opcao == "3":
        fila.atenderPaciente()
    elif opcao == "4":
        print("Programa encerrado.")
        break
    else:
        print("Opção inválida. Escolha uma opção de 1 a 4.")
