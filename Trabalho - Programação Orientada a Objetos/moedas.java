// Cofre de moedas: Real, Euro, Libra e Won

// representando qualquer moeda
public abstract class Moeda {
    protected double valor; // guarda o valor da moeda

    public Moeda(double valor) {
        this.valor = valor;
    }

    // Mostra as informações da moeda
    public abstract void info();

    // Converte o valor da moeda para Real
    public abstract double converterParaReal();

    // remover moedas
    @Override
    public boolean equals(Object obj) {
        if (this == obj) return true;
        if (obj == null) return false;
        if (this.getClass() != obj.getClass()) return false;

        Moeda outra = (Moeda) obj;
        return this.valor == outra.valor;
    }
}


// Real 
public class Real extends Moeda {

    public Real(double valor) {
        super(valor);
    }

    @Override
    public void info() {
        System.out.println("Real - R$ " + valor);
    }

    @Override
    public double converterParaReal() {
        return valor; 
    }
}


// Euro
public class Euro extends Moeda {

    public Euro(double valor) {
        super(valor);
    }

    @Override
    public void info() {
        System.out.println("Euro - € " + valor);
    }

    @Override
    public double converterParaReal() {
        return valor * 6.19; // valor aproximado para conversão
    }
}


// Libra
public class Libra extends Moeda {

    public Libra(double valor) {
        super(valor);
    }

    @Override
    public void info() {
        System.out.println("Libra - £ " + valor);
    }

    @Override
    public double converterParaReal() {
        return valor * 7.26;
    }
}


// Won
public class Won extends Moeda {

    public Won(double valor) {
        super(valor);
    }

    @Override
    public void info() {
        System.out.println("Won - ₩ " + valor);
    }

    @Override
    public double converterParaReal() {
        return valor * 0.0038;
    }
}


// Guarda todas as moedas adicionadas pelo usuário
import java.util.ArrayList;

public class Cofrinho {

    private ArrayList<Moeda> listaMoedas = new ArrayList<>(); // lista onde ficam as moedas

    // Adiciona moeda no cofrinho
    public void adicionar(Moeda m) {
        listaMoedas.add(m);
        System.out.println("Moeda adicionada!");
    }

    // Remove moeda igual da lista
    public void remover(Moeda m) {
        boolean removida = listaMoedas.remove(m);

        if (removida) {
            System.out.println("Moeda removida!");
        } else {
            System.out.println("Moeda não encontrada.");
        }
    }

    // Lista todas as moedas adicionadas
    public void listar() {
        if (listaMoedas.isEmpty()) {
            System.out.println("Nenhuma moeda no cofrinho.");
            return;
        }

        System.out.println("--- Moedas no Cofrinho ---");
        for (Moeda moeda : listaMoedas) {
            moeda.info();
        }
    }

    // Soma tudo convertido para Real
    public double totalConvertido() {
        double total = 0;

        for (Moeda moeda : listaMoedas) {
            total += moeda.converterParaReal();
        }

        return total;
    }
}


// Menu para o usuário interagir
import java.util.Scanner;

public class Principal {
    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);
        Cofrinho cofrinho = new Cofrinho();

        int opcao = -1;

        while (opcao != 0) {
            System.out.println("===== MENU DO COFRINHO =====");
            System.out.println("1 - Adicionar moeda");
            System.out.println("2 - Remover moeda");
            System.out.println("3 - Listar moedas");
            System.out.println("4 - Mostrar total convertido para Real");
            System.out.println("0 - Sair");
            System.out.print("Escolha: ");

            opcao = scanner.nextInt();

            switch (opcao) {
                case 1:
                    // Opção adicionar moedas
                    System.out.println("Escolha a moeda: 1-Real 2-Euro 3-Libra 4-Won");
                    int tipoAdd = scanner.nextInt();
                    System.out.print("Valor: ");
                    double valorAdd = scanner.nextDouble();

                    Moeda novaMoeda = null;

                    if (tipoAdd == 1) novaMoeda = new Real(valorAdd);
                    else if (tipoAdd == 2) novaMoeda = new Euro(valorAdd);
                    else if (tipoAdd == 3) novaMoeda = new Libra(valorAdd);
                    else if (tipoAdd == 4) novaMoeda = new Won(valorAdd);

                    if (novaMoeda != null) cofrinho.adicionar(novaMoeda);
                    break;

                case 2:
                    // Opção remover moedas
                    System.out.println("Escolha a moeda para remover: 1-Real 2-Euro 3-Libra 4-Won");
                    int tipoRem = scanner.nextInt();
                    System.out.print("Valor: ");
                    double valorRem = scanner.nextDouble();

                    Moeda moedaRemover = null;

                    if (tipoRem == 1) moedaRemover = new Real(valorRem);
                    else if (tipoRem == 2) moedaRemover = new Euro(valorRem);
                    else if (tipoRem == 3) moedaRemover = new Libra(valorRem);
                    else if (tipoRem == 4) moedaRemover = new Won(valorRem);

                    cofrinho.remover(moedaRemover);
                    break;

                case 3:
                    // Listar moedas
                    cofrinho.listar();
                    break;

                case 4:
                    // Mostrar total convertido
                    double total = cofrinho.totalConvertido();
                    System.out.println("Total em Real: R$ " + total);
                    break;

                case 0:
                    System.out.println("Encerrando...");
                    break;

                default:
                    System.out.println("Opção inválida.");
            }
        }

        scanner.close();
    }
}
