def func(name,*name1, **name2):
    print(f"Normal name: {name} \nArgs name: {name1} \nKwargs name: {name2}")
nme="prince"
nme1=['prince','gaur','is','doing', 'work']
nme2={'Name':'Prince','sirname':'gaur','action':'work'}
func(nme,*nme1,**nme2)