void main() {
  double n1 = 9.56;

  //   double m1 = 1;
  //   double m50 = 0.50;
  //   double m25 = 0.25;
  //   double m10 = 0.10;
  //   double m05 = 0.05;
  //   double m01 = 0.01;

  //1 UM 1
  // qtidade de moedas de 1
  int valor1 = n1 ~/ 1; //9

  // resto
  double resto1 = n1 - (valor1 * 1); //9.56 - 9

  
  //50 CINQUENTA 50
  // qtidade de moedas de 50, mas usando do que sobrou sem as moedas de 1
  int valor50 = resto1 ~/ 0.5; //1

  //resto
  double resto50 = resto1 - (valor50 * 0.50); //0.56 - 0.50

  
  //25 VINTE E CINCO 25
  // qtidade de moedas de 25, mas usando do que sobrou sem as moedas de 50
  int valor25 = resto50 ~/ 0.25;  //0

  //resto
  double resto25 = resto50 - (valor25 * 0.25); //0.06 - 0

  
  //10 DEZ 10
  // qtidade de moedas de 10, mas usando do que sobrou sem as moedas de 25
  int valor10 = resto25 ~/ 0.10; //0

  //resto
  double resto10 = resto25 - (valor10 * 0.10); //0.06 - 0

  
  //0.10 ZERO PONTO DEZ 0.10
  // qtidade de moedas de 05, mas usando do que sobrou sem as moedas de 10
  int valor05 = resto10 ~/ 0.05; //1

  //resto
  double resto05 = resto10 - (valor05 * 0.05);//0.06 - 0.05

  //0.01 ZERO PONTO ZERO UM 0.01
  // qtidade de moedas de 01, mas usando do que sobrou sem as moedas de 05
  int valor01 = resto05 ~/ 0.01; //1

  print("Valor: $n1");

  print("Moedas de 1 real: ${valor1}");
  print("Moedas de 50 centavos: ${valor50}");
  print("Moedas de 25 centavos: ${valor25}");
  print("Moedas de 10 centavos: ${valor10}");
  print("Moedas de 05 centavos: ${valor05}");
  print("Moedas de 01 centavos: ${valor01}");
}
