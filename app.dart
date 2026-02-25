void main() {
  String? nombre = stdin.readLineSync();

  String? apellido = stdin.readLineSync();

  int edadMayor = int.parse(stdin.readLineSync()!);

  int edadMenor = int.parse(stdin.readLineSync()!);

  int diferencia = edadMayor - edadMenor;

  print("Nombre completo: $nombre $apellido");
  print("La diferencia de edad es: $diferencia años");
}