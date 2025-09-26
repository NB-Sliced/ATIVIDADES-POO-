import random
import time

print("aminadabe entrou em sua casa , escolha um lugar para se esconder")
print()

esconderijo = ["no banheiro", "em baixo do sofá", "em baixo da cama", "na cozinha", "no quintal",
               "dentro do guarda roupa", "atrás da cortina da sala"]

print("onde deseja se esconder ?")
print()
print("a - no banheiro")
print("b - em baixo do sofá")
print("c - em baixo da cama")
print("d - na cozinha ")
print("e - no quintal")
print("f - dentro do guarda roupa")
print("g - atrás da cortina da sala")

mapa = {
    "a": "no banheiro",
    "b": "em baixo do sofá",
    "c": "em baixo da cama",
    "d": "na cozinha",
    "e": "no quintal",
    "f": "dentro do guarda roupa",
    "g": "atrás da cortina da sala"
}

# parte do caba se esconder
while True:
    aluno = input("\ndigite uma letra que corresponde ao seu esconderijo:\n").lower()
    if aluno not in mapa:
        print("código inválido, digite uma letra ")
        continue

    escolha = mapa[aluno]
    procura = random.choice(esconderijo)

    print()
    print("××× aminadabe olhou", procura, "×××")
    print()

    if escolha == procura:
        print("""AMINADABE ACHOU VOCÊ


  ⠛⠛⣿⣿⣿⣿⣿⡷⢶⣦⣶⣶⣤⣤⣤⣀   
   ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀ 
   ⠉⠉⠉⠙⠻⣿⣿⠿⠿⠛⠛⠛⠻⣿⣿⣇ 
  ⢤⣀⣀⣀  ⢸⣷⡄ ⣁⣀⣤⣴⣿⣿⣿⣆
    ⠹⠏   ⣿⣧ ⠹⣿⣿⣿⣿⣿⡿⣿
         ⠛⠿⠇⢀⣼⣿⣿⠛⢯⡿⡟
          ⠦⠴⢿⢿⣿⡿⠷ ⣿ 
       ⠙⣷⣶⣶⣤⣤⣤⣤⣤⣶⣦⠃ 
       ⢐⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿  
       ⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇  
         ⠙⠻⢿⣿⣿⣿⣿⠟
""")
        break
    else:
        print("--aminadabe não lhe achou! Escolha outro esconderijo rápido, pois ele está ficando com raiva...")
        print()
        print("     |  (o)   (o)  |   suspiro")
        print()
        mapa.pop(aluno)
        print(mapa)

        if not mapa:
            print("""aminadabe não te achou e você conseguiu fugir , ele começou a gargalhar loucamente enquanto observava você se afastar da residência em que ele estava

⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠛⠛⠉⠉⠁      ⠈⠉⠉⠛⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⠁ ⢀⣀      ⡀   ⣿⣿⣿⣆⡀ ⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠉⠠⢒⣴⣿⣿⣿⣿⣦ ⠐⢢⡢⠉⠑⢦⡈⠻⠿⣿⣿⣿⠒ ⡘⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃  ⢀⣿⣿⣿⣿⣿⣿⡿⠃ ⡀⠁   ⢳⣤⠤⣐⡒⠂ ⠠⢡⠈⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡗ ⢀⣀⠾⠿⣿⣿⣿⠿⢋⠤⡖⠋  ⣀⣀  ⠉⠙⡆⠙ ⣀⢠⢳⡆⠄⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟ ⡀ ⠃ ⠐⠈⠁ ⡴⠃ ⣧ ⢰⠟⠋⢉⣠⣤⣶⡖⣷⠐⢠⡇⡞⣿⣿ ⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿ ⢣⢘⢄⡀ ⣀⣠⡄   ⢈⢀⢰ ⠠⠾⡛⡈⠱⡱⢲⢏⡟⣸⣾⣿⣿ ⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿ ⠈⠺⣼⣿⣡⣧⡧⢟⡷⠗⢧⠻⡀⢰⢆⣷⢫⣷⢹⡆⣇⣏⣿⢳⣷⣿⣿⣿ ⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇  ⣿⣿⣿⣿⣷⣾⣸⣾⠾⡇⢏⣎⡿⣹⡿⣎⡏⣿⣾⣿⣿⣿⣿⣿⣿⡏ ⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿   ⠈⢿⣿⣿⣿⣧⣯⣧⣿⢿⢺⡾⣿⣷⣿⣻⣽⣿⣿⣿⣿⣿⣿⣿⣿⣫⡄⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇   ⠈⠾⣿⣿⣿⣿⣾⣾⣾⣿⣿⣻⣿⣿⣿⣷⣿⣿⣿⣿⣿⣿⣿⣿⣯⡀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆  ⠱⠈⢟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡷⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆  ⠡ ⡩⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢟⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆   ⠈⠢⡙⢽⢿⣿⣿⣿⣿⣿⣿⣟⣿⣿⣿⣿⣿⣿⣿⡿⣿⡟⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⡀  ⠈⠐⢌⡃⢸⢹⣿⣿⠛⣟⣟⣟⣿⣽⣹⠙⣟⠷⠉⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣀   ⠉⠆⠉⠿⡎⡇⡏⢀⢹⣀⢇⠁⠉⠉ ⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣄⣀   ⠈⠈⠈⠁⠈⢀⢀⣠⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿          

""")
            break