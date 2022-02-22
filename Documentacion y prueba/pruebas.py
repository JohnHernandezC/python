def compruebaMail (mailUsuario):
    """
    la funcion compruebaMail comprueba si un correo es correcto o si no
    si tiene mas de una @ o si la @ esta al final o al inicio es incoorercto
    >>> compruebaMail('john@cursos.es')
    True
    >>> compruebaMail('johncursos.es@')
    False
    >>> compruebaMail('johncursos.es')
    False
    """
    arroba=mailUsuario.count('@')
    if (arroba!=1 or mailUsuario.rfind('@')==(len(mailUsuario)-1) or mailUsuario.find('@')==0):
        return False
    else:
        return True



import doctest
doctest.testmod()
help(compruebaMail)