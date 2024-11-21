void main() {
  //instancia
  ContaCorrente cc1 = ContaCorrente();
  cc1.nomeTitular = "João";
  cc1.nConta = 1234;
  cc1.saldo = 1000.50;
  cc1.premio = true;

  //infos
  cc1.imprimirInfos();

  // calculo emprestimo
  double valorEmprestimo = cc1.calculaEmprestimo();
  print("Voce tem ${valorEmprestimo} reais disponíveis para emprestimo! :D");

  // teste deposito
  bool depositoSucesso = cc1.depositar(500);
  print(depositoSucesso
    ? "=> DEPOSITO REALIZADO! Novo Saldo: ${cc1.saldo}"
    : "ERRO =( Valor invalido");

  // teste saque
  bool saqueSucesso = cc1.sacar(500);
  print(saqueSucesso
    ? "=> SAQUE REALIZADO! Novo Saldo: ${cc1.saldo}"
    : "ERRO =( Saldo insuficiente ou valor invalido.");

  // testes saques invalidos
  print(cc1.sacar(4000) ? "=> SAQUE REALIZADO!" : "ERRO =( Saldo insuficiente");
  print(cc1.sacar(-90) ? "=> SAQUE REALIZADO!" : "ERRO =( Valor invalido");
}

class ContaCorrente {
  // atributos
  String nomeTitular = "";
  int nConta = 0;
  double saldo = 0.0;
  bool premio = false;

  // METODOS
  //metodo pra depositar dinheiro
  bool depositar(double valor) {
    if (valor <= 0) return false; // vivendo e aprendendo
    saldo += valor;
    return true;
  }

  // metodo pra sacar dinheiro
  bool sacar(double valor) {
    if (valor <= 0 || valor > saldo) return false;
    saldo -= valor;
    return true;
  }

  // metodo pra imprimir infos
  void imprimirInfos(){
    print("Titular: ${nomeTitular}, Saldo: ${saldo} reais");
  }

  // metodo pra calcular emprestimo com base se o cliente é premium
  double calculaEmprestimo() => premio ? saldo * 0.3 : saldo * 0.15;
}