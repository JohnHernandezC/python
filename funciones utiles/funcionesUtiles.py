"""def solution(inputString):
    
 return inputString == inputString[::-1]  #recorre listas en reversa

def solution(inputArray):
    mx = []
    for i in range(0,len(inputArray)-1):
      soluc =inputArray[i]*inputArray[i+1]
      mx.append(soluc)
    return max(mx) # sumarle una posicion a la lista

def solution(n):
    if n>=10**4 or n<1:
        return False

    return (n**2+(n-1)**2)#area de un poligono si cada una de sus cuadros es igual a 1

def solution(statues):


    return max(statues)-min(statues)-len(statues)+1#saber cuantso numeros faltan dentro de 1 array
    
    

def find_maximum_adjacent_product(input_list):
    
         Finds the largest product encountered:
         Example:
         find_maximum_adjacent_product([3, 6, -2, -5, 7, 3])
         >>> 21
         find_maximum_adjacent_product([3])
         >>> float('-inf')
    
    try:
     return max([element * adjacent for element, adjacent in zip(input_list[:-1], input_list[1:])])
    except ValueError:
     return float('-inf')
 
print(find_maximum_adjacent_product([]))"""



def solution(matrix):
    sum=0
    for i in range(0,len(matrix[0])):
        for x in range(0,len(matrix)):
            if matrix[x][i]==0:
              break
            else:
              sum+=matrix[x][i]
    else:
        return sum
    
#WTF COMO FUNCIONA ESTO
