# Cada nodo representa um estado
class Nodo:
    def __init__(self, sigla, nomeEstado):
        self.sigla = sigla
        self.nomeEstado = nomeEstado
        self.proximo = None


# Classe que controla a tabela hash
class TabelaHash:
    def __init__(self):
        # Cria 10 posições vazias
        # Cada posição será o início de uma lista
        self.tabela = [None] * 10

    # Calcula a posição do estado na tabela
    def funcaoHash(self, sigla):
        # DF sempre fica na posição 7
        if sigla == "DF":
            return 7
        # Pega o valor ASCII das duas letras
        primeiraLetra = ord(sigla[0])
        segundaLetra = ord(sigla[1])
        # Soma os valores e pega o resto da divisão por 10
        posicao = (primeiraLetra + segundaLetra) % 10
        return posicao

    # Insere o estado no início da lista
    def inserir(self, sigla, nomeEstado):
        # Descobre a posição do estado
        posicao = self.funcaoHash(sigla)
        # Cria o novo estado
        novoNodo = Nodo(sigla, nomeEstado)
        # O novo estado aponta para o antigo primeiro
        novoNodo.proximo = self.tabela[posicao]
        # O novo estado passa a ser o primeiro
        self.tabela[posicao] = novoNodo

    # Imprime as siglas separadas por posição
    def imprimirTabela(self):
        # Passa pelas 10 posições
        for posicao in range(10):
            print(f"Posição {posicao}: ", end="")
            # Pega o primeiro estado da posição
            atual = self.tabela[posicao]
            # Mostra None se a posição estiver vazia
            if atual is None:
                print("None")
            else:
                # Percorre a lista e mostra as siglas
                while atual is not None:
                    print(atual.sigla, end=" ")
                    atual = atual.proximo
                # Pula uma linha
                print()


# Cria a tabela hash
tabela = TabelaHash()
# Mostra a tabela antes de inserir qualquer informação
print("\n--- TABELA HASH VAZIA ---")
tabela.imprimirTabela()
# Insere os 26 estados e o Distrito Federal
tabela.inserir("AC", "Acre")
tabela.inserir("AL", "Alagoas")
tabela.inserir("AP", "Amapá")
tabela.inserir("AM", "Amazonas")
tabela.inserir("BA", "Bahia")
tabela.inserir("CE", "Ceará")
tabela.inserir("ES", "Espírito Santo")
tabela.inserir("GO", "Goiás")
tabela.inserir("MA", "Maranhão")
tabela.inserir("MT", "Mato Grosso")
tabela.inserir("MS", "Mato Grosso do Sul")
tabela.inserir("MG", "Minas Gerais")
tabela.inserir("PA", "Pará")
tabela.inserir("PB", "Paraíba")
tabela.inserir("PR", "Paraná")
tabela.inserir("PE", "Pernambuco")
tabela.inserir("PI", "Piauí")
tabela.inserir("RJ", "Rio de Janeiro")
tabela.inserir("RN", "Rio Grande do Norte")
tabela.inserir("RS", "Rio Grande do Sul")
tabela.inserir("RO", "Rondônia")
tabela.inserir("RR", "Roraima")
tabela.inserir("SC", "Santa Catarina")
tabela.inserir("SP", "São Paulo")
tabela.inserir("SE", "Sergipe")
tabela.inserir("TO", "Tocantins")
tabela.inserir("DF", "Distrito Federal")
# Mostra a tabela com os estados e o Distrito Federal
print("\n--- TABELA COM OS ESTADOS E O DF ---")
tabela.imprimirTabela()
# Insere o estado fictício com meu nome
tabela.inserir("JS", "Julia Souza")
# Mostra a tabela incluindo o estado fictício
print("\n--- TABELA COM O ESTADO FICTÍCIO ---")
tabela.imprimirTabela()
