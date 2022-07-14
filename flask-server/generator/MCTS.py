import dtr
import numpy as np
import random
import fitness


class Node:

    def __init__(self, parent, action, depth, terminal=False):
        self.parent = parent
        self.children = []
        self.action = action
        self.terminal = terminal
        self.num_visits = 0
        self.total_fitness = 0
        self.depth = depth

    def visit(self, reward):
        self.num_visits += 1
        self.total_fitness += reward

    def ucb(self, c):
        if self.depth != 0:
            return self.total_fitness / self.num_visits + c * np.sqrt(
                np.log(self.parent.num_visits) / self.num_visits)
        else:
            return self.total_fitness / self.num_visits + c * np.sqrt(
                np.log(self.num_visits) / self.num_visits)

    def get_depth(self):
        return self.depth

    def is_terminal(self):
        return self.depth >= 129

    def add_child(self, node):
        self.children.append(node)

    def get_action(self):
        return self.action

    def get_avg_fitness(self):
        return self.total_fitness / self.num_visits


class MCTSAgent:

    def __init__(self, modules):
        self.modules = modules
        self.options = []
        dtr.init_rooms()
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
        self.root = Node(None, None, -1)
        self.best = 0
        for i in range(len(self.options)):
            new_node = Node(self.root, i, 0)
            self.root.add_child(new_node)
            dtr.MCTS_reset()
            path = []
            path.append(new_node)
            mods = self.modules.copy()
            m = mods[0]
            state = self.options[i]
            m["days"] = state["days"]
            m["timeslots"] = state["timeslots"]
            m["room"] = state["room"]
            dtr.mcts_schedule(m)
            self.rollout(new_node, path)

        # print("Initialization Complete")


# if i % 200 == 0:
#                 print(i, "initialization steps complete out of", len(self.options))

    def expansion(self):
        path = []

        current_node = self.root
        mods = self.modules.copy()
        dtr.MCTS_reset()
        while current_node.children != [] and not (current_node.is_terminal()):
            max_index = 0
            max_score = -1
            i = 0
            for child in current_node.children:
                score = child.ucb(0.9)
                if score >= max_score:
                    max_index = i
                    max_score = score
                i += 1
            path.append(current_node.children[max_index])
            current_node = current_node.children[max_index]
            if current_node.parent == self.root:
                self.best = current_node.get_avg_fitness()
            m = mods[current_node.get_depth()]
            state = self.options[current_node.get_action()]

            m["days"] = state["days"]
            m["timeslots"] = state["timeslots"]
            m["room"] = state["room"]

            dtr.mcts_schedule(m)

        new_node = Node(current_node, random.randint(0,
                                                     len(self.options) - 1),
                        current_node.get_depth() + 1)
        path.append(new_node)
        current_node.add_child(new_node)

        self.rollout(current_node, path)

    def get_highest_score(self):
        #max_score = 0
        #for child in self.root.children:
        #if child.get_avg_fitness() > max_score:
        #max_score = child.get_avg_fitness()
        return self.best

    def rollout(self, node, path):
        index = node.get_depth()
        module_list = self.modules.copy()

        for i in range(index + 1, len(self.modules)):
            module = module_list[i]
            state = self.options[random.randint(0, len(self.options) - 1)]

            module["days"] = state["days"]
            module["timeslots"] = state["timeslots"]
            module["room"] = state["room"]

            dtr.mcts_schedule(module)
        fitness = self.reward(module_list)
        for n in path:
            n.visit(fitness)

    def reward(self, modules):
        ## Check for conflicts. If conflicts return -10

        num_conflicts = 0
        for s in dtr.major_students:
            for day in s["reserved"]:
                for time in day:
                    if time > 1:
                        #print("Major students")
                        #print(s["major"], s["level"])
                        num_conflicts += time - 1

        for s in dtr.rooms:
            for day in s["reserved"]:
                for time in day:
                    if time > 1:
                        #print("room")
                        #print(day)
                        num_conflicts += time - 1
        for s in dtr.lecturers:
            for day in s["reserved"]:
                for time in day:
                    if time > 1:
                        #print("lecturers")
                        #print(day)
                        num_conflicts += time - 1

        if num_conflicts != 0:
            return num_conflicts * -1

        fit = fitness.calculate_fitness(modules)

        fit = fit / 2000000.0
        fit = fit * 8

        return fit

    def train(self, iterations):
        for i in range(iterations):
            if i % 200 == 0:
                # print the results to file
                print(i, "training steps complete out of", iterations)
                with open("results.txt", "a") as f:
                    f.write(
                        str(i) + "," + str(self.get_highest_score()) + "\n")
                print(i, "iterations complete")
            if i % 750 == 0:
                print("current best:", self.get_highest_score())
            if i % 2000 == 0:
                for child in self.root.children:
                    print(child.ucb(0.9), child.get_avg_fitness())
            self.expansion()

    def get_best_path(self):
        current = self.root
        path = []
        mods = self.modules.copy()

        dtr.init_rooms()
        while current.children != [] and not (current.is_terminal()):
            max_index = 0
            max_score = -1
            i = 0
            for child in current.children:
                score = child.ucb(0.9)
                if score >= max_score:
                    max_index = i
                    max_score = score
                i += 1
            path.append(current.children[max_index])
            current = current.children[max_index]

            m = mods[current.get_depth()]
            state = self.options[current.get_action()]

            m["days"] = state["days"]
            m["timeslots"] = state["timeslots"]
            m["room"] = state["room"]

            dtr.mcts_schedule(m)

        return path, mods, self.reward(mods)
