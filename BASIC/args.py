def func(name,*name1, **name2):
    print(f"Normal name: {name} \nArgs name: {name1} \nKwargs name: {name2}")
name="prince"
name1=['prince','gaur','is','doing', 'work']
name2={'Name':'Prince','sirname':'gaur','action':'work'}
func(name,*name1,**name2)
#Using *args as a function parameter enables you to pass an arbitrary number of arguments to that function.
#The arguments are then accessible as the tuple args in the body of the function.

#**kwargs (standing for keyword arguments) allows you to handle named arguments that you have not defined in advance.
#The keyword arguments return a dictionary in which the keys are the argument names, and the values are the argument values.

#Named parameters to a function can be made optional by giving them a default value.
#These must come after named parameters without a default value.

