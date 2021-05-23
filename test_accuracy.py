from simplex import *
from main import calculate_min


correct_answers = {'task1': {'x1': 0, 'min': 3.0, 'x2': 3.0},
                   'task2': {'x1': 20.0, 'min': 142.0, 'x2': 6.0},
                   'task3': {'x1': 3.0, 'min': 800.0, 'x2': 2.0}}


parameters = {'task1': {'cons': ['1,1,G,3', '1,2,G,4'], 'obj': ['2,1,0']},
              'task2': {'cons': ['5,1,G,3', '1,2,G,4'], 'obj': ['2,1,0']}}


def test_simplex():
    for i, p in enumerate(parameters.items()):
        task = f'task{i+1}'
        result = calculate_min(p[1]['cons'], p[1]['obj'])
        compared = correct_answers[task]

        assert result == compared