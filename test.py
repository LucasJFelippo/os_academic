

procs = [['a', 25, 25, 0], ['b', 10, 10, 0], ['c', 4.5, 4.5, 0], ['d', 1, 1, 0], ['e', 0.25, 0.25, 0]]


for i in range(100):
    print(procs)

    act = procs.pop(0)
    act[3] += 1
    act[2] = act[1]

    for proc in procs:
        proc[2] += 2

    c = False
    for index, proc in enumerate(procs):
        if proc[2] < act[2]:
            c = True
            procs.insert(index, act)
            break
    if not c:
        procs.append(act)

