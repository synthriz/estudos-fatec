void main(){
  //instancia de pessoa 1
  Pessoa p1 = Pessoa();
  p1.nome = "Molinari";
  p1.altura = 1.75;
  p1.peso = 70.0;
  
  //testando os metodos
  p1.imprimirInfos();
  print("=> IMC: ${p1.calcularImc().toStringAsFixed(0)}"); //imc formatado
  print("=> Sua classificaçao do IMC é: ${p1.classificarImc()}");
  
  print("------------"); //separador xd
  print(p1.engordar(5) ? "Voce engordou!" : "Valor invalido!");
  print(p1.emagrecer(2) ? "Voce emagreceu!" : "Valor invalido!");
  print(p1.crescer(0.05) ? "Voce esticou!" : "Valor invalido!");
  p1.imprimirInfos();
  
  //testes invalidos
  print(p1.engordar(-1) ? "Voce engordou!" : "Valor invalido!");
  print(p1.emagrecer(90) ? "Voce emagreceu!" : "Valor invalido!");
  print(p1.crescer(-5) ? "Voce esticou!" : "Valor invalido!");
  p1.imprimirInfos();
}

//classe pessoa
class Pessoa{
  //ATRIBUTOS
  String nome = "";
  double peso = 0;
  double altura = 0;
  
  //METODOS
  //metodo engordar
  bool engordar(double pesoGanho){
    if(pesoGanho < 0) return false; //pesoGanho nao pode ser negativo
    peso += pesoGanho; //calculo do novo peso
    return true;
  }
  
  //metodo emagrecer
  bool emagrecer(double pesoPerdido){
    if(pesoPerdido < 0 || peso - pesoPerdido < 0) return false; //pesoPerdido nao pode ser negativo, nem o novo valor de peso
    peso -= pesoPerdido; //calculo do novo peso
    return true;
  }
  
  //metodo crescer
  bool crescer(double alturaGanha){
    if(alturaGanha < 0) return false; //alturaGanha nao pode ser negativa
    altura += alturaGanha; //calculo da nova altura
    return true;
  }
  
  //metodo calcular imc
  double calcularImc(){
    return peso / (altura * altura); //calculo imc
  }
  
  //metodo pra classificar o imc
  String classificarImc(){
    double imc = calcularImc();
    if (imc < 19) return "Abaixo do peso"; //se imc < 19, abaixo do peso
    if (imc > 26) return "Acima do peso"; //se imc < 26, acima do peso
    return "Peso ideal"; //senao, esta no peso ideal
  }
  
  //metodo de imprimir infos
  void imprimirInfos(){
    print("=> Nome: ${nome}");
    print("=> Peso: ${peso}");
    print("=> Altura: ${altura}");
  }
}