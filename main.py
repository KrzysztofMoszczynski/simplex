from arg_parser import *
from simplex import *

args = ArgumentParser()
constrain_args = args.get_constraints()
obj_func = args.get_obj_func()


def calculate_min(constrain_args, obj_func):
    m = gen_matrix(2, len(constrain_args))

    for c in constrain_args:
        constrain(m, c)

    obj(m, obj_func[0])
    print(constrain_args, obj_func)

    return minz(m)


if __name__ == "__main__":
    print(calculate_min(constrain_args, obj_func))
