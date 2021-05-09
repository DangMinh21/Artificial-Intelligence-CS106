from ortools.algorithms import pywrapknapsack_solver

def main():
    # Create the solver.
    solver = pywrapknapsack_solver.KnapsackSolver(
        pywrapknapsack_solver.KnapsackSolver.
        KNAPSACK_MULTIDIMENSION_BRANCH_AND_BOUND_SOLVER, 'KnapsackExample')
    # no.of test case
    n_case = 96
    # set time
    Time = 30
    with open("test_set.txt", "r") as ft:
        with open("result_ORtool.txt", "w") as fw:
            fw.write("")
        for i in range(n_case):
            read_test = ft.readline()
            print(read_test + "-----------")
            values = []
            weights = [[]]
            capacities = []
            with open(read_test[:-1], "r") as f:
                f.readline()
                n = int(f.readline())
                capacities.append(int(f.readline()))
                f.readline()
                for i in range(n):
                    line = f.readline()
                    item = list(map(int, line.split()))
                    values.append(item[0])
                    weights[0].append(item[1])

            solver.Init(values, weights, capacities)
            #set time
            solver.set_time_limit(Time)
            computed_value = solver.Solve()

            total_weight = 0
            for i in range(len(values)):
                if solver.BestSolutionContains(i):
                    total_weight += weights[0][i]
            String = str(capacities[0]) + " " + str(total_weight) + " " + str(computed_value) + "\n"
            with open("result_ORtool.txt", "a") as fw:
                fw.write(String)

if __name__ == '__main__':
    main()