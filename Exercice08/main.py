def log_decorator(func):
    def wrapper():
        print("Avant l'exécution de la fonction.")
        func()
        print("Après l'exécution de la fonction.")
    
    return wrapper

@log_decorator
def function_test():
    print("Cette fonction ne prend pas d'arguments.")

function_test()
