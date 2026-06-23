tasks = ["T1", "T2", "T3"]
resources = [1, 2]

allocation = {}

def allocate(task_index):
    if task_index == len(tasks):
        return True

    task = tasks[task_index]

    for resource in resources:

        count = list(allocation.values()).count(resource)

        if count < 2:      # Fairness constraint

            allocation[task] = resource

            if allocate(task_index + 1):
                return True

            del allocation[task]

    return False

if allocate(0):
    print("Resource Allocation:")
    for t, r in allocation.items():
        print(t, "-> Resource", r)
else:
    print("No feasible allocation found")
