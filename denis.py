def l():
    print('=-'*15)
l()
print('6 é burro?')
l()

print("algoritmo idade")
ano_nascimento = int(input("Digite sua data de nascimento: "))
data_atual = int(input("Digite o ano atual: "))

idade = data_atual - ano_nascimento
t = 2030 - ano_nascimento

print(f"sua idade em 2030 vai ser: {t}")
print(f"sua idade atual é: {idade}")