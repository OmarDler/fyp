from audioop import cross
import fitness
import numpy as np
import dtr
import random


class Path:

    def __init__(self, path, score):
        self.path = path
        self.score = score

    def get_score(self):
        return self.score

    def get_path(self):
        return self.path


class Elitist_GA:

    def __init__(self, generations, env, crossover, mutation, pop_size,
                 t_size):
        dtr.init_rooms()
        self.options = []
        for i in range(10):
            for j in range(16):
                for k in range(16):
                    self.options.append({
                        "days":
                        dtr.get_days_internal(i),
                        "timeslots":
                        dtr.get_timeslots_internal(j),
                        "room":
                        dtr.get_room_internal(k)
                    })

        self.generations = generations
        self.modules = env
        self.cross = crossover
        self.mutation = mutation
        self.population = self.generate_new_population(pop_size)
        self.tournament_size = t_size

    def run_tournament_old(self, paths):
        winners = []
        size = len(paths)
        if size == 2:
            return paths
        group_a = paths[0:int(size / 2)]
        group_b = paths[int(size / 2):size]

        i = 0

        while i < int(size / 2):
            if group_a[i].score > group_a[i + 1].score:
                winners.append(group_a[i])
            else:
                winners.append(group_a[i + 1])
            if group_b[i].score > group_b[i + 1].score:
                winners.append(group_b[i])
            else:
                winners.append(group_b[i + 1])
            i += 2
        return self.run_tournament(winners)

    def run_tournament(self, paths):
        max_a = 0
        max_b = 0
        winners = []
        for k in range(len(paths)):
            if paths[k].score > paths[max_a].score:
                max_a = k
        winners.append(paths[max_a])
        for k in range(len(paths)):
            if (paths[k].score > paths[max_b].score) and (k != max_a):
                max_b = k
        winners.append(paths[max_b])
        return winners

    def crossover(self, parents):
        parent_a = parents[0]
        parent_b = parents[1]
        children = []
        new_child = []
        new_child_b = []

        cross_length = int(self.cross * len(parent_a.get_path()))

        for option in parent_a.get_path()[:cross_length]:
            new_child.append(option)
        for option in parent_b.get_path()[cross_length:]:
            new_child.append(option)

        i = 0
        for element in new_child:
            if new_child.count(element) > 1:
                ## Duplicates exist

                new_val = random.randint(0, 2559)

                while new_val in new_child:
                    new_val = random.randint(0, 2559)

                new_child[i] = new_val
            i += 1

        for option in parent_b.get_path()[:cross_length]:
            new_child_b.append(option)
        for option in parent_a.get_path()[cross_length:]:
            new_child_b.append(option)

        i = 0
        for element in new_child_b:
            if new_child_b.count(element) > 1:
                ## Duplicates exist

                new_val = random.randint(0, 2559)

                while new_val in new_child_b:
                    new_val = random.randint(0, 2559)

                new_child_b[i] = new_val
            i += 1
        dtr.MCTS_reset()
        mods = self.modules.copy()
        for i in range(len(new_child)):
            module = mods[i]
            option = self.options[new_child[i]]

            module["days"] = option["days"]
            module["timeslots"] = option["timeslots"]
            module["room"] = option["room"]

            counter = 0
            while not (dtr.is_valid(mods, i, None)) and counter < 10000:

                new_val = random.randint(0, 2559)
                while new_val in new_child:
                    new_val = random.randint(0, 2559)
                option = self.options[new_val]

                module["days"] = option["days"]
                module["timeslots"] = option["timeslots"]
                module["room"] = option["room"]
                counter += 1

            if counter != 0:
                new_child[i] = new_val

            dtr.mcts_schedule(module)

        reward = self.get_score(mods)

        to_append = Path(new_child, reward)
        self.mutate(to_append)
        children.append(to_append)

        dtr.MCTS_reset()
        mods = self.modules.copy()
        for i in range(len(new_child_b)):
            module = mods[i]
            option = self.options[new_child_b[i]]

            module["days"] = option["days"]
            module["timeslots"] = option["timeslots"]
            module["room"] = option["room"]
            counter = 0
            while not (dtr.is_valid(mods, i, None)) and counter < 10000:
                if counter == 9999:
                    print("limit reached")

                new_val = random.randint(0, 2559)
                while new_val in new_child_b:
                    new_val = random.randint(0, 2559)
                option = self.options[new_val]

                module["days"] = option["days"]
                module["timeslots"] = option["timeslots"]
                module["room"] = option["room"]
                counter += 1

            if counter != 0:
                new_child_b[i] = new_val
            dtr.mcts_schedule(module)

        reward = self.get_score(mods)
        to_append = Path(new_child_b, reward)
        self.mutate(to_append)
        children.append(to_append)

        return children

    def mutate(self, child):
        for i in range(len(child.get_path())):
            random_int = random.randint(0, 1000)
            if random_int <= self.mutation * 1000:
                new_val = random.randint(0, 2559)
                while new_val in child.get_path():
                    new_val = random.randint(0, 2559)
                child.get_path()[i] == new_val

    def run_generation(self, num):
        for i in range(num):
            print("Running generation", i)
            new_pop = []
            max_a = 0
            max_b = 0

            for k in range(len(self.population)):
                if self.population[k].score > self.population[max_a].score:
                    max_a = k
            for k in range(len(self.population)):
                if (self.population[k].score >
                        self.population[max_b].score) and (k != max_a):
                    max_b = k
            best_pop_parents = []
            best_pop_parents.append(self.population[max_a])
            best_pop_parents.append(self.population[max_b])
            new_best_children = self.crossover(best_pop_parents)
            for child in new_best_children:
                new_pop.append(child)
            for parent in best_pop_parents:
                new_pop.append(parent)
            while not (len(new_pop) == len(self.population)):
                tournament_paths = []
                for j in range(self.tournament_size):
                    index = np.random.randint(len(self.population))
                    tournament_paths.append(self.population[index])
                best_parents = self.run_tournament(tournament_paths)
                new_children = self.crossover(best_parents)
                for child in new_children:
                    new_pop.append(child)
            self.population = new_pop

            print("Mean Score:", self.get_pop_score())

    def run_generations(self):
        self.run_generation(self.generations)

    def generate_new_population(self, size):
        pop = []
        for i in range(size):

            print("generated", i, "members")
            dtr.MCTS_reset()
            path = []
            mods = self.modules.copy()
            for j in range(len(mods)):
                new_val = random.randint(0, 2559)
                while new_val in path:
                    new_val = random.randint(0, 2559)
                path.append(new_val)

            for j in range(len(path)):

                module = mods[j]
                option = self.options[path[j]]

                module["days"] = option["days"]
                module["timeslots"] = option["timeslots"]
                module["room"] = option["room"]

                counter = 0
                while not (dtr.is_valid(mods, j, None)) and counter < 10000:
                    if counter == 9999:
                        print("limit exhausted after", j, "modules")

                    new_val += 1
                    new_val = new_val % 2559
                    while new_val in path:
                        new_val += 1
                        new_val = new_val % 2559
                    option = self.options[new_val]

                    module["days"] = option["days"]
                    module["timeslots"] = option["timeslots"]
                    module["room"] = option["room"]
                    counter += 1

                dtr.mcts_schedule(module)

            reward = self.get_score(mods)

            ret = Path(path, reward)
            pop.append(ret)
        return pop

    def get_population(self):
        return self.population

    def get_pop_score(self):
        score = 0
        for path in self.population:
            score += path.score
        return score / len(self.population)

    def get_score(self, schedule):
        ## Check for conflicts. If conflicts return -10
        num_conflicts = 0
        for s in dtr.major_students:
            for day in s["reserved"]:
                for time in day:
                    if time > 1:
                        #print("Major students")
                        #print(s["major"], s["level"])
                        num_conflicts += time

        for s in dtr.rooms:
            for day in s["reserved"]:
                for time in day:
                    if time > 1:
                        #print("room")
                        #print(day)
                        num_conflicts += time
        for s in dtr.lecturers:
            for day in s["reserved"]:
                for time in day:
                    if time > 1:
                        #print("lecturers")
                        #print(day)
                        num_conflicts += time

        if num_conflicts != 0:
            return num_conflicts * -1
        # print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        fit = fitness.calculate_fitness(schedule)

        fit = fit / 2000000.0
        fit = fit * 8

        return fit

    def get_best(self):
        best_score = -100000
        best_path = Path([], -10000000)
        for path in self.population:
            if path.score > best_score:
                print("new best!")
                best_score = path.score
                best_path = path
        return best_path
