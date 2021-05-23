from arg_parser import *
from simplex import *

args = ArgumentParser()
constrain_args = args.get_constraints()
obj_func = args.get_obj_func()

def calculate_min():
    var_number = int(input("Podaj ilość zmiennych w funkcji celu: "))
    constrains_number = int(input("Podaj ilość ograniczeń: "))
    real_constrains_number = constrains_number

    objective_fun = []
    for i in range(var_number):
        objective_coef = float(input(f"Podaj współczynnik przy zmiennej x{i+1}: "))
        objective_fun.append(float(objective_coef))
    objective_fun.append(0)
    constrains_list = []
    for i in range(constrains_number):
        print("Teraz podaj ograniczenia:")
        constrain_arr = []
        for i in range(var_number):
            constrain_coef = float(input(f"Podaj współczynnik przy zmiennej x{i+1}: "))
            constrain_arr.append(constrain_coef)
        operator = input("Podaj operator (G-większe bądź równe, L-mniejsze bądź równe, E-równe): ")
        constrain_arr.append(operator)
        result = float(input("Podaj wynik ograniczenia: "))
        constrain_arr.append(result)
        if operator == 'E':
            second_constrain_arr = []
            real_constrains_number += 1
            constrain_arr[constrain_arr.index('E')] = 'G'
            second_constrain_arr = constrain_arr.copy()
            second_constrain_arr[second_constrain_arr.index('G')] = 'L'
            constrains_list.append(constrain_arr)
            constrains_list.append(second_constrain_arr)
        else:
            constrains_list.append(constrain_arr)

    print(constrains_list)
    m = gen_matrix(var_number, real_constrains_number)
    for c in constrains_list:
        constrain(m, c)

    obj(m, objective_fun)
    #print(constrain_args, obj_func)

    return minz(m)


if __name__ == "__main__":
    print(calculate_min())
