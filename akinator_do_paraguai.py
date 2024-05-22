#feito por : david
p1 = input('pense em um pais. ele é da europa?(s/n)')
if p1=='n':
    print('pais nao cadastrado')
if p1 == 's':
    p2 = input('o pais fala frances?(s/n)')
    if p2 == 's':
        p3 = input('é o principal pais?(s/n)')
        if p3 == 's':
            print('frança')
        else:
            print('luxemburgo')
    if p2 == 'n':
        p3 = input('o pais fala alemao?(s/n)')
        if p3 == 's':
            p4 = input('é o pais principal?(s/n)')
            if p4 == 's':
                print('alemanha')
            else:
                print('suiça')
        if p3=='n':
            print('pais nao cadastrado')

