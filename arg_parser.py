import argparse

class ArgumentParser:

    def __init__(self):
        self.parser = argparse.ArgumentParser()

        # constrains
        self.parser.add_argument('-o', metavar='O', dest='obj_func', type=str,
                                 nargs=1, help='Objective function:'
                                                 '\n coefficients: "2,-1,G,10" for 2x -1y > 10')
        
        self.parser.add_argument('-c', metavar='C', dest='constraints', type=str,
                                 nargs='+', help='Give:'
                                                 '\n constraints and coefficients: "2,-1,G,10" for 2x -1y > 10')


        # parse
        self.args = self.parser.parse_args()
        
    def get_constraints(self):
        return self.args.constraints
    
    def get_obj_func(self):
        return self.args.obj_func
