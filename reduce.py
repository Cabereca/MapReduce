def reduce_function(key, value):
    contagem_final = open('contagem_final', 'a')
    contagem_final.write(f"{key} {sum(value)}\n")
    contagem_final.close()
