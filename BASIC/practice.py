
def outer():
  global glo
  glo = 20
  def inner():
    global glo
    glo = 30
    print(glo)
glo = 10
outer()
print( glo)