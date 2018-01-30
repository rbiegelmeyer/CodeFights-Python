def digitsProduct(product):
      if product == 0:
    return 10
  if product < 10:
    return product
  
  lista = []
  i = 9
  while i > 1:
    if product%i == 0:
      product = int(product/i)
      lista.insert(0,i)
      if product < 10:
        print (product)
        lista.insert(0,product)
        return int("".join(str(x) for x in lista))
    else:
      i-=1
  if i == 1:
    return -1