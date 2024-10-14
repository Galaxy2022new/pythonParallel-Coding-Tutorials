def f(x):
    return x * x


from multiprocessing import Pool

p = Pool(5)

import pythonParall.func

p.map(pythonParall.func.f, [1, 2, 3])
