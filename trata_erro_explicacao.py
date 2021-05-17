try:
     a =int(input('Numerador'))
     b =int(input('Denominador'))
     r = a / b

except Exception as erro:
    print(f'O Erro foi {erro.__class__}')

except (ValueError, TypeError):
    print('Tivemos um problema com o tipo de dados que você digitou.')

except ZeroDivisionError:
    print('Não é possivel dividir um numero por zero.')

except KeyboardInterrupt:
    print('O Usuário preferiu não informar os dados.')

except Exception as erro:
    print(f'O Erro encontrado foi: {erro.__cause__}')

else:
    print(f'O resulado é: {r:.1f}')
finally:
    print('Volte sempre! Muito Obrigado.')