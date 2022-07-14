from itertools import count
import generator.query as query
# import generator.query as query
import generator.toCSV as toCSV
import generator.dtr as dtr
import os
import sys

blue = query.db_query()


def st(input):
    dtr.init_rooms()
    bluePrint = input
    counter = 0
    max = 0
    z = 1000
    failure = False
    j = 0
    for b in bluePrint:
        count = 0
        for i in range(j + 1, len(bluePrint)):
            mod = bluePrint[i]
            if mod["major"] == b["major"] and mod["level"] == b["level"]:
                count += 1

        while True:
            b["days"] = dtr.get_days()
            b["timeslots"] = dtr.get_timeslots()
            b["room"] = dtr.get_room(b, b["days"], b["timeslots"], count)
            if b["room"] != None:
                # print("scheduled " + b["module"] + " to room " + b["room"])
                # print("counter: " + str(counter))
                max = counter
                z = counter + 9000
                # dtr.print_rooms()
                break
            counter += 1
            if counter > z:
                print("failed to schedule")
                # print("restarting")
                # print(max)
                failure = True
                sys.stdout.flush()
                # os.execv(sys.argv[0], sys.argv)
                os.execv(sys.executable, [sys.executable, __file__] + sys.argv)

                # st()
                # return null
        j += 1
    return bluePrint, failure


def st_experimental():
    bluePrint = blue
    failures = []
    dtr.init_rooms()
    j = 0
    for b in bluePrint:
        count = 0
        for i in range(j + 1, len(bluePrint)):
            mod = bluePrint[i]
            if mod["major"] == b["major"] and mod["level"] == b["level"]:
                count += 1

        room, day, time = dtr.backtrack(b, count)
        if j == 93:
            j = 93
        if room == None or day == None or time == None:
            failures.append(b)
            bluePrint.remove(b)
            #print("Deleted", j)
            # print(len(failures))
            # print(len(bluePrint))
        else:
            b["days"] = day
            b["timeslots"] = time
            b["room"] = room
        j += 1
    for b in bluePrint:
        if not ('days' in b):
            failures.append(b)
            bluePrint.remove(b)
    # dtr.print_rooms()
    # print("Initial Failures: ", len(failures))
    s, f = st(failures)

    for b in s:
        # print("here")
        # print(b["days"])
        bluePrint.append(b)
        # print(len(bluePrint))
        #print('days' in b)
        # print(b)

    # for t in bluePrint:
    #    if not('days' in t):
    # print("missing")
    #        bluePrint.remove(t)
    # print("\n")
    # for t in bluePrint:
    # if not('days' in t):
    # print("missing")
    # print(len(bluePrint))
    #i = 0
    # for t in bluePrint:
    # if not('days' in t):
    # print("missing")
    # print(i)
    #i += 1
    return bluePrint


def recursive_backtracking_search():
    dtr.init_rooms()

    result = dtr.backtrack_helper(blue, 0)
    print(result)

    return result


def format_guest_list():
    pass


if format_guest_list():
    pass

# when we reach this point we have a list of modules with timeslots and rooms
# that have no lecturer or room conflicts with the other modules
# we need to check the student conflicts
# then we need to check the quality of the solution
# and improvise if needed
# toCSV.createCSV(st())

print("\n")

# print("done")


# Backtracking result
def start_BFSRB(filename):
    print("reached BFSRB")
    st_result = st_experimental()
    problems = []
    for t in st_result:
        if not ('days' in t):
            problems.append(t)
    st(problems)
    print("done")
    # return st_result
    # fit = fitness.calculate_fitness(st_result)
    toCSV.createCSV(st_result, filename)


#print("Secondary Failures: ", len(problems))
# print("\n")
#i = 0
# for t in st:
#    print(i)
#    print(t)
#    print(t['days'])
#    i += 1

# print(index)
#blue.sort(key=lambda x: x['students'])
# print(len(blue))
# blue.reverse()
# print(blue)
#bool_result = recursive_backtracking_search()
# print(blue)


# ## Uncomment for MCTS
# def start_MCTS():
#     tree = MCTS.MCTSAgent(blue)
#     tree.train(100000000)
#     result = tree.get_best_path()
#     fit = fitness.calculate_fitness(result)
#     toCSV.createCSV(result, fit)


# #print(path)
# #print(internal_reward)
# #def run_ga():


# ## Uncomment for genetic algorithm
# def start_geneticAlgorithm():
#     s = time.time()

#     elite_ga = genetic_algorithm.Elitist_GA(10, blue, 0.4, 0.05, 100, 8)
#     elite_ga.run_generations()
#     result = elite_ga.get_best()
#     print(result.get_path())
#     print(result.get_score())
#     et = time.time()
#     elapsed_time = et - s
#     print('Execution time:', elapsed_time, 'seconds')

#     # fit = fitness.calculate_fitness(result)
#     # toCSV.createCSV(result, 0)


# # neat_ga.run(15)
# # result = neat_ga.results()

# mods = st_result
# fit = fitness.calculate_fitness(mods)
# toCSV.createCSV(mods, fit)
