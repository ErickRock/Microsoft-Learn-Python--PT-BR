
valor = input('Você gostaria de continuar? Sim[S] ou Não[N]: ')

if valor =='sim' or valor == 's' or valor == 'S':
  print('Continuando...')
  print('Completo!')
elif valor == 'nao' or valor == 'n' or valor == 'N':
  print('Saindo...')
else:
  print('Responda com sim[S] ou nao[N]: ')
