#printing args and kwargs separately
def args_kwargs(*args,**kwargs):
    print("Positional Arguments(args):",args)
    print("Keyword Arguments(kwargs):",kwargs)
args_kwargs(1,2,3,name="Akhila",age=21)