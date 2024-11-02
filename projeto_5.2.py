print("Vais viajar primeiro para o Brasil e depois para a Tailândia.")

euro = float(input("Queres coverter quantos euros?"))

moed_loc = int(input("Se queres converter para Reais responde 1, se queres coverter para Baht Tailandês responde 0."))

if moed_loc == 1:
    print("Se coverteres essa quantidade de euros vais ficar com" , euro*6.36 , "Reais.")
elif moed_loc == 0:
    baht = int(euro*36.77)
    print("Se coverteres essa quantidade de euros vais ficar com" , baht , "Baht Tailandês.")