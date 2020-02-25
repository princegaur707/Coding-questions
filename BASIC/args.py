def func(name,*name1, **name2):
    print(f"Normal name: {name} \nArgs name: {name1} \nKwargs name: {name2}")
name="prince"
name1=['prince','gaur','is','doing', 'work']
name2={'Name':'Prince','sirname':'gaur','action':'work'}
func(name,*name1,**name2)