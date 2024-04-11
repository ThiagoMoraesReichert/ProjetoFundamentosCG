# -=-=-=-=-=-=-=-
def musicaElefantes(n):
    for i in range(1,n):
        print(i, " Elefante(s) incomoda(m) muito a gente,")
        print(i+1, 'elefante(s)', end='')
        for j in range(0, i+1):
            print('Incomodam, ', end='')
        print(' muito mais!')
# -=-=-=-=-=-=-=-

musicaElefantes(3)