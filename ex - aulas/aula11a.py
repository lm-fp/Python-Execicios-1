# ansi - escape sequence

#  \033 [style text back m
#  \033 [0;33;44m

# 0 sem estilo 1 neguito  4 sublinhado 7 converter (fundo e letra)
# 30-> branco 31-> vermelho 32-> verde 33-> amarelo 34-> azul  35->rosa 36-> ciano 37-> cinza

# exmplos
# \033[0;30;41m
# \033[4;33;44m
# \033[0 ;35;43m
# \033[30;42m
# \033[m
# \033[7;30m

print('\033[7;33;46mOla mundo\033[m')
nome = 'lets'
print('Ola, prazer em te conhecer, {}{}{}'.format('\033[35m', nome, '\033[m'))
cores = {'limpa' : '\033[m',
        'azul' : '\033[34m',
        'amarelo' : '\033[33m'}
print('Ola, prazer em te conhecer, {}{}{}'.format(cores['amarelo'], nome, cores['limpa']))

