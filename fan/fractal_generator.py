"""
This console program can generate Serpinskiy triangle
How to use:
1. Set minimal fonts size in your console and run this file
2. if you don't see triangle make size smaller
3. Wait a minute and enjoy))

P. S.
Tested only on linux console
"""

import random
import os

size = 100   # set smaller number there if you dont see triangle

place = [['  ' for i in range(size*3)] for y in range(size)]

dags_coords = [[random.randint(1, size), random.randint(1, size*2)],
    [random.randint(1, size), random.randint(1, size*2)],
    [random.randint(1, size), random.randint(1, size*2)]
]

"""
uncomment this part of code to get max size triangle

dags_coords = [[1, 1],
    [1, size*3],
    [size, round(size*3/2)]
]
"""


for i in dags_coords:
    place[i[0]-1][(i[1]-1)] = ' ◆'

dag_pozition = [random.randint(1, size), random.randint(1, size)]
place[dag_pozition[0]-1][(dag_pozition[1]-1)] = ' ◆'

os.system('clear')
for a in place:
    print(''.join(a))

dag_pozition = [random.randint(1, size), random.randint(1, size)]

while 1:
    direction = random.randint(0, 2)

    dag_coord = [int(((dags_coords[direction][0] + dag_pozition[0]) / 2)),
        int((dags_coords[direction][1] + dag_pozition[1]) / 2)]

    place[dag_coord[0]-1][dag_coord[1]-1] = ' ◆'

    os.system('clear')
    for a in place:
        print(''.join(a))
    dag_pozition = dag_coord
    print(direction)
