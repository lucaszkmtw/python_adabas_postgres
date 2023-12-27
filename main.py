from models.afiliado import Afiliado

afiliado = Afiliado.get_from_adabas(20001801512)
saved = afiliado.save_to_postgres()
afiliado_from_postgres = Afiliado.get_from_postgres(20001801512)
print(afiliado_from_postgres)
