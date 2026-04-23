import random

states = [(i,j) for i in range(3) for j in range(3)]
actions = ['UP','DOWN','LEFT','RIGHT']

goal = (1,1)
gamma = 0.9

def step(s,a):
    i,j = s
    if s == goal:
        return s, 0
    if a=='UP': i=max(i-1,0)
    if a=='DOWN': i=min(i+1,2)
    if a=='LEFT': j=max(j-1,0)
    if a=='RIGHT': j=min(j+1,2)
    return (i,j), -1

policy = {s:random.choice(actions) for s in states}
V = {s:0 for s in states}

for _ in range(5):
    # evaluation
    for _ in range(10):
        for s in states:
            if s==goal: continue
            ns,_ = step(s,policy[s])
            V[s] = -1 + gamma*V[ns]

    # improvement
    for s in states:
        if s==goal: continue
        policy[s] = max(actions, key=lambda a: -1 + gamma*V[step(s,a)[0]])

print("\nPolicy Iteration Results:")
for s in states:
    if s != goal:
        print(f"State: {s}, Action: {policy[s]}, Value: {round(V[s],2)}")
