void main() {
  void fibonacci(int n) {
  int a = 0, b = 1, temp;
  int count = 0;

  while (count < n) { //valida a quantidade de termos
    print(a);
    temp = a + b; //soma do termo anterior (temp = 1+1 = 2)
    a = b; // atualiza "a" para o valor de "b" (o próximo número anterior) (a=1)
    b = temp; // atualiza "b" p novo valor de fibonacci (temp) (b=2)
    count++;
  }
}

  int n = 15; // quantos termos a sequencia vai ter
  print("sequencia ate $n:");
  fibonacci(n);
}
