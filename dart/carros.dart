main() {
  //instancias
  Carro car1 = Carro();
  car1.modelo = "Corolla";
  car1.veloAtual = 0;
  car1.veloMax = 200;
  
  Carro car2 = Carro();
  car2.modelo = "Fusquinha";
  car2.veloAtual = 0;
  car2.veloMax = 140;
  
  // TESTES
  // testando o corolla
  car1.imprimirInfos();
  //condiçao ? oq acontece se verdadeiro : oq acontece se falso
  print(car1.acelerar(50) ? "Acelerando..." : "Não é possível acelerar mais... Vai estourar o motor :p");
  print(car1.atingiuVeloMax() ? "Voce atingiu a velocidade maxima!" : "Voce ainda não atingiu a velocidade máxima!");
  print(car1.frear(5) ? "Freando..." : "Nao é possivel frear; o carro já está parado!");
  car1.imprimirInfos();
  
  // testando o fusquinha
  print("------------"); //separador xd
  car2.imprimirInfos();
  print(car2.acelerar(50) ? "Acelerando..." : "Não é possível acelerar mais... Vai estourar o motor :p");
  print(car2.acelerar(90) ? "Acelerando..." : "Não é possível acelerar mais... Vai estourar o motor :p");
  print(car2.atingiuVeloMax() ? "Voce atingiu a velocidade maxima!" : "Voce ainda não atingiu a velocidade máxima!");
  print(car2.frear(90) ? "Freando..." : "Nao é possivel frear; voce já está parado!");
  print(car2.frear(60) ? "Freando..." : "Nao é possivel frear; voce já está parado!");
  car2.imprimirInfos();
  
}

//classe carro
class Carro {
  String modelo = "";
  double veloAtual = 0;
  double veloMax = 0;
  
  //METODOS
  //metodo de acelerar
  bool acelerar(double aumento){
    if (veloAtual + aumento <= veloMax) { //verifica se a velocidade atual com a aceleraçao nao utrapassa a velocidade maxima
        veloAtual += aumento; //aumenta a velocidade
        return true; //acelerou
    }
    veloAtual = veloMax; //nao há mais o que aumentar, entao a velocidade maxima é a atual
    return false;
  }
  
  //metodo de frear
  bool frear(double reducao){
    if (veloAtual - reducao >= 0){ //verifica se é possivel subtrair sem negativar
        veloAtual -= reducao; //subtrai a reduçao da velocidade
        return true; //freou
    }
    veloAtual = 0; //o carro vai come to a complete stop (como fala isso em portugues?)
    return false; 
  }
  
  //metodo de imprimir infos
  void imprimirInfos(){
    print(" => Modelo do carro: ${modelo}");
    print("=> Velocidade atual: ${veloAtual}");
    print("=> Velocidade maxima: ${veloMax}");
  }
  
  //metodo pra ver se atingiu velocidade maxima
  bool atingiuVeloMax(){ //se atingir a velocidade maxima, o boolean vai ser verdadeiro, senao, falso
    if (veloAtual == veloMax){
      return true; //atingiu a velocidade maxima
    }
    return false; //ainda nao atingiu a velocidade maxima
  }
}