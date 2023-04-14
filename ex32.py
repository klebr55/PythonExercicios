from datetime import datetime

datatual = 0
ano = int(input("Que ano quer analisar? [Digite 0 para o ano atual]: "))
if ano != 0:
    if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
        print(f"O ano {ano} é bissexto")
    else:
        print(f"O ano {ano} não é bissexto")
elif ano == 0:
    datatual = datetime.now().year
    if datatual % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
        print(f"O ano de {datatual} é bissexto.")
    else:
        print(f"O ano de {datatual} não é bissexto.")