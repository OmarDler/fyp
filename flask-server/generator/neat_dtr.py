# import random
# import sys
# import os
# import fitness

# from sqlalchemy import true
# import generator.query as query


# # gene 1
# # Day

# # @description: pick a random int from 0 to 4


# def pick_day1():
#     day1 = random.randint(0, 4)
#     return day1

# # @description: pick a random int from 0 to 4 thats not day 1


# def pick_day2(day1):
#     r = random.random()
#     if r < 0.9:
#         if day1 <= 2:
#             day2 = day1 + 2
#         else:
#             day2 = day1 - 2
#     else:
#         day2 = random.randint(0, 4)
#         while day2 == day1:
#             day2 = random.randint(0, 4)
#     return day2

# # @description: call the functions to get the days


# def get_days():
#     day1 = pick_day1()
#     return ([day1, pick_day2(day1)])


# class Data():


# # gene 2
# # rooms

#     def __init__(self):
#         self.rooms = []
#         self.rooms.append({'id': 'B9', 'capacity': 40})
#         self.rooms.append({'id': 'B10', 'capacity': 24})
#         self.rooms.append({'id': 'B11', 'capacity': 24})
#         self.rooms.append({'id': 'G5', 'capacity': 35})
#         self.rooms.append({'id': 'F14', 'capacity': 35})
#         self.rooms.append({'id': 'S12', 'capacity': 24})
#         self.rooms.append({'id': 'S13', 'capacity': 49})
#         self.rooms.append({'id': 'S14', 'capacity': 42})
#         self.rooms.append({'id': 'S15', 'capacity': 46})
#         self.rooms.append({'id': 'S16', 'capacity': 30})
#         self.rooms.append({'id': 'T9', 'capacity': 24})
#         self.rooms.append({'id': 'T10', 'capacity': 24})
#         self.rooms.append({'id': 'T11', 'capacity': 24})
#         self.rooms.append({'id': 'T13', 'capacity': 42})
#         self.rooms.append({'id': 'T14', 'capacity': 24})
#         self.rooms.append({'id': 'T15', 'capacity': 30})
#         self.rooms.sort(key=lambda x: x['capacity'])

#         self.timeslots = []
#         self.timeslots.append({'id': 0, 'time': '8:30/10:00', 'weight': 0.15})
#         self.timeslots.append({'id': 1, 'time': '10:30/12:00', 'weight': 0.25})
#         self.timeslots.append({'id': 2, 'time': '12:30/2:00', 'weight': 0.3})
#         self.timeslots.append({'id': 3, 'time': '2:30/4:00', 'weight': 0.3})
#         self.options = []
#         for i in range(10):
#             for j in range(16):
#                 for k in range(16):
#                     self.options.append({"days" : self.get_days_internal(i), "timeslots" : self.get_timeslots_internal(j), "room":self.get_room_internal(k)})
#         self.init_rooms()


# # @description: add the reserved attribute to the each room
# # global lecturers
# # global major_students
#     def get_scheduling_data(self, val):
#         return self.options[int(val)]

#     def init_rooms(self):

#         self.lecturers = []
#         self.major_students = []
#         for r in self.rooms:
#             r["reserved"] = [
#                 [0, 0, 0, 0], [0, 0, 0, 0],
#                 [0, 0, 0, 0], [0, 0, 0, 0],
#                 [0, 0, 0, 0]
#             ]

#         for l in query.get_lecturers():
#             self.lecturers.append({"id": l[0], "name": l[1], "reserved": [
#                 [0, 0, 0, 0], [0, 0, 0, 0],
#                 [0, 0, 0, 0], [0, 0, 0, 0],
#                 [0, 0, 0, 0]
#             ]})
#         for s in query.get_major_students():
#             self.major_students.append({"major": s[0], "level": s[1], "reserved": [
#                 [0, 0, 0, 0], [0, 0, 0, 0],
#                 [0, 0, 0, 0], [0, 0, 0, 0],
#                 [0, 0, 0, 0]
#             ]})
#         # print(major_students)

#     def MCTS_reset(self):
#         for r in self.rooms:
#             r["reserved"] = [
#                 [0, 0, 0, 0], [0, 0, 0, 0],
#                 [0, 0, 0, 0], [0, 0, 0, 0],
#                 [0, 0, 0, 0]
#             ]
#         for l in self.lecturers:
#             l["reserved"] = [
#                 [0, 0, 0, 0], [0, 0, 0, 0],
#                 [0, 0, 0, 0], [0, 0, 0, 0],
#                 [0, 0, 0, 0]
#             ]
#         for s in self.major_students:
#             s["reserved"] = [
#                 [0, 0, 0, 0], [0, 0, 0, 0],
#                 [0, 0, 0, 0], [0, 0, 0, 0],
#                 [0, 0, 0, 0]
#             ]

#     # Experimental: function to get a new day pair
#     def get_days_internal(self, current):
#         if current == 0:
#             return ([0,1])
#         elif current < 4:
#             return ([0,current + 1])
#         elif current < 7:
#             return ([1, current - 2])
#         elif current < 9:
#             return ([2, current - 4])
#         elif current == 9:
#             return ([3,4])
#         else:
#             return None


#     #####
#     #current = 0 -> 3: 0,1 0,2 0,3 0,4
#     #current = 4 -> 6:  1,2 1,3 1,4
#     #current = 7 -> 8: 2,3, 2,4
#     #current = 9: 3,4
#     ####


#     ## TODO: incorporate weights
#     def get_timeslots_internal(self, current):
#         if current < 4:
#             val = ([0, current])
#         elif current < 8:
#             val = ([1, current - 4])
#         elif current < 12:
#             val = ([2, current - 8])
#         elif current < 16:
#             val = ([3, current - 12])
#         else:
#             return None

#         return val

#     ####
#     #current = 0 -> 3: 0,0 0,1 0,2 0,3
#     #current = 4 -> 7: 1,0 1,1 1,2 1,3
#     #etc.
#     ####


#     def schedule_guest(self, module, days, timeslots, lecturer):
#         for r in self.rooms:
#             if r["capacity"] >= module["students"] and r["reserved"][days[0]][timeslots[0]] == 0 and r["reserved"][days[1]][timeslots[1]] == 0:
#                 #print("1")
#                 for s in self.major_students:
#                     # print(s["major"] == module["major"] and s["level"] == module["level"])
#                     if s["major"] == module["major"] and s["level"] == module["level"] and s["reserved"][days[0]][timeslots[0]] == 0 and s["reserved"][days[1]][timeslots[1]] == 0:
#                         lecturer["reserved"][days[0]][timeslots[0]] = 1
#                         lecturer["reserved"][days[1]][timeslots[1]] = 1
#                         r["reserved"][days[1]][timeslots[1]] = 1
#                         r["reserved"][days[0]][timeslots[0]] = 1
#                         s["reserved"][days[0]][timeslots[0]] = 1
#                         s["reserved"][days[1]][timeslots[1]] = 1
#                         return r["id"]
#         return None

#     def print_rooms(self):
#         print(self.rooms)
#     # get a room that houses the students and is not reserved for the timeslot

#     def get_room(self, module, days, timeslots, remaining):
#         for r in self.rooms:
#             if r["capacity"] >= module["students"] and r["reserved"][days[0]][timeslots[0]] == 0 and r["reserved"][days[1]][timeslots[1]] == 0:
#                 #print("1")
#                 for l in self.lecturers:
#                     if l["name"] == module["lecturer"] and l["reserved"][days[0]][timeslots[0]] == 0 and l["reserved"][days[1]][timeslots[1]] == 0:
#                         #print("2")
#                         for s in self.major_students:
#                         # print(s["major"] == module["major"] and s["level"] == module["level"])
#                             if s["major"] == module["major"] and s["level"] == module["level"] and s["reserved"][days[0]][timeslots[0]] == 0 and s["reserved"][days[1]][timeslots[1]] == 0:
#                                 #print("3")
#                                 count_a = 0
#                                 count_b = 0
#                                 for i in range(4):
#                                     if s["reserved"][days[0]][i] != 0:
#                                         count_a += 1
#                                     if s["reserved"][days[1]][i] != 0:
#                                         count_b += 1

#                                 ## ensure students do not take more than 3 modules per day
#                                 if count_a < 3 and count_b < 3 or (days[0] > 2):

#                                     ## if we already have 2 classes scheduled for either of these days
#                                     ## Then only choose this day if this is the final class for this group

#                                     ## Also ensure that this is not the only module scheduled for this day
#                                     if ((count_a > 1 or count_b > 1) and remaining < 1) or ((count_a < 1 or count_b < 1) and remaining > 0) or (count_a < 2 and count_b < 2) or (days[0] > 2):
#                                         l["reserved"][days[0]][timeslots[0]] += 1
#                                         l["reserved"][days[1]][timeslots[1]] += 1
#                                         r["reserved"][days[1]][timeslots[1]] += 1
#                                         r["reserved"][days[0]][timeslots[0]] += 1
#                                         s["reserved"][days[0]][timeslots[0]] += 1
#                                         s["reserved"][days[1]][timeslots[1]] += 1
#                                         return r["id"]
#         return None


#     def is_valid(self, full_list, index, remaining):


#         module = full_list[index]
#         days = module["days"]
#         timeslots = module["timeslots"]

#         for room in self.rooms:
#             if module["room"] == room["id"]:
#                 r = room
#                 break

#         for lecturer in self.lecturers:
#             if lecturer["name"] == module["lecturer"]:
#                 l = lecturer
#                 break

#         for student in self.major_students:
#             if student["major"] == module["major"] and student["level"] == module["level"]:
#                 s = student
#                 break

#         if r["capacity"] >= module["students"] and r["reserved"][days[0]][timeslots[0]] == 0 and r["reserved"][days[1]][timeslots[1]] == 0:
#             #print("1")

#             if l["reserved"][days[0]][timeslots[0]] == 0 and l["reserved"][days[1]][timeslots[1]] == 0:
#                     #print("2")
#                     # print(s["major"] == module["major"] and s["level"] == module["level"])
#                 if s["reserved"][days[0]][timeslots[0]] == 0 and s["reserved"][days[1]][timeslots[1]] == 0:

#                     return True
#                     #print("3")
#                     count_d1 = 0
#                     count_d2 = 0
#                     for i in range(4):
#                         if s["reserved"][days[0]][i] != 0:
#                             count_d1 += 1
#                         if s["reserved"][days[1]][i] != 0:
#                             count_d2 += 1

#                     total = 0
#                     for i in range(5):
#                         for j in range(4):
#                             if s["reserved"][i][j] != 0:
#                                 total += 1
#                     ## ensure students do not take more than 3 modules per day
#                     if count_d1 < 4 and count_d2 < 4:
#                         return True
#                     elif total >= 10:
#                         return True
#                     else:
#                         return False
#         return False


#     def backtrack(self, module, remaining):
#         #start with changing days
#         for i in range(10):
#             days = self.get_days_internal(i)
#             #change timeslots
#             for j in range(16):
#                 times = self.get_timeslots_internal(j)
#                 r = self.get_room(module, days, times, remaining)
#                 if r != None:
#                     return r, self.get_days_internal(i), self.get_timeslots_internal(j)
#         return None, None, None


#     def mcts_schedule(self, module):
#         days = module["days"]
#         timeslots = module["timeslots"]

#         for room in self.rooms:
#             if module["room"] == room["id"]:
#                 r = room
#                 break

#         for lecturer in self.lecturers:
#             if lecturer["name"] == module["lecturer"]:
#                 l = lecturer
#                 break

#         for student in self.major_students:
#             if student["major"] == module["major"] and student["level"] == module["level"]:
#                 s = student
#                 break

#         l["reserved"][days[0]][timeslots[0]] += 1
#         l["reserved"][days[1]][timeslots[1]] += 1
#         r["reserved"][days[1]][timeslots[1]] += 1
#         r["reserved"][days[0]][timeslots[0]] += 1
#         s["reserved"][days[0]][timeslots[0]] += 1
#         s["reserved"][days[1]][timeslots[1]] += 1


#     def mcts_unschedule(self, module):
#         days = module["days"]
#         timeslots = module["timeslots"]

#         for room in self.rooms:
#             if module["room"] == room["id"]:
#                 r = room
#                 break

#         for lecturer in self.lecturers:
#             if lecturer["name"] == module["lecturer"]:
#                 l = lecturer
#                 break

#         for student in self.major_students:
#             if student["major"] == module["major"] and student["level"] == module["level"]:
#                 s = student
#                 break

#         l["reserved"][days[0]][timeslots[0]] -= 1
#         l["reserved"][days[1]][timeslots[1]] -= 1
#         r["reserved"][days[1]][timeslots[1]] -= 1
#         r["reserved"][days[0]][timeslots[0]] -= 1
#         s["reserved"][days[0]][timeslots[0]] -= 1
#         s["reserved"][days[1]][timeslots[1]] -= 1


#     def get_room_internal(self, index):
#         return self.rooms[index]["id"]

#     def backtrack_helper(self, full_list, index):

#         ## base case, we have scheduled all modules
#         if index >= len(full_list):
#             return True

#         if index % 5 == 0:
#             print("At", index)


#         module = full_list[index]
#         for lecturer in self.lecturers:
#             if lecturer["name"] == module["lecturer"]:
#                 l = lecturer

#         for student in self.major_students:
#             if student["major"] == module["major"] and student["level"] == module["level"]:
#                 s = student


#         remaining = self.calculate_remaining(full_list, index)
#         for i in range(10):
#             for j in range(16):
#                 for k in range(len(self.rooms)):
#                     module["days"] = self.get_days_internal(i)
#                     module["timeslots"] = self.get_timeslots_internal(j)
#                     module["room"] = self.get_room_internal(k)


#                     if self.is_valid(full_list, index, remaining):

#                         for room in self.rooms:
#                             if module["room"] == room["id"]:
#                                 r = room

#                         l["reserved"][module["days"][0]][module["timeslots"][0]] = 1
#                         l["reserved"][module["days"][1]][module["timeslots"][1]] = 1
#                         r["reserved"][module["days"][1]][module["timeslots"][1]] = 1
#                         r["reserved"][module["days"][0]][module["timeslots"][0]] = 1
#                         s["reserved"][module["days"][0]][module["timeslots"][0]] = 1
#                         s["reserved"][module["days"][1]][module["timeslots"][1]] = 1

#                         result =  self.backtrack_helper(full_list, index + 1)

#                         if result: return True
#                         else:
#                             l["reserved"][module["days"][0]][module["timeslots"][0]] = 0
#                             l["reserved"][module["days"][1]][module["timeslots"][1]] = 0
#                             r["reserved"][module["days"][1]][module["timeslots"][1]] = 0
#                             r["reserved"][module["days"][0]][module["timeslots"][0]] = 0
#                             s["reserved"][module["days"][0]][module["timeslots"][0]] = 0
#                             s["reserved"][module["days"][1]][module["timeslots"][1]] = 0
#         return False


#     def calculate_remaining(self, full_list, index):
#         count = 0
#         b = full_list[index]
#         for i in range(index + 1, len(full_list)):
#             mod = full_list[i]
#             if mod["major"] == b["major"] and mod["level"] == b["level"]:
#                 count += 1
#         return count


#     # gene 3
#     # timeslots


#     def pick_timeslot1(self):
#         index = 0
#         r = random.random()
#         while(r > 0):
#             r -= self.timeslots[index]["weight"]
#             index += 1
#         index -= 1
#         return self.timeslots[index]["id"]


#     def pick_timeslot2(self):
#         index = 0
#         r = random.random()
#         while(r > 0):
#             r -= self.timeslots[index]["weight"]
#             index += 1
#         index -= 1
#         return self.timeslots[index]["id"]


#     def get_timeslots(self):
#         return ([self.pick_timeslot1(), self.pick_timeslot2()])


#     def neat_inputs(self, module):
#         for lecturer in self.lecturers:
#             if lecturer["name"] == module["lecturer"]:
#                 l = lecturer

#         for student in self.major_students:
#             if student["major"] == module["major"] and student["level"] == module["level"]:
#                 s = student

#         inputs = []

#         availability = l["reserved"]

#         for day in availability:
#             for timeslot in day:
#                 inputs.append(timeslot)

#         availability = s["reserved"]

#         for day in availability:
#             for timeslot in day:
#                 inputs.append(timeslot)

#         for room in self.rooms:
#             availability = room["reserved"]

#             for day in availability:
#                 for timeslot in day:
#                     inputs.append(timeslot)

#         return inputs

#     def get_score(self, schedule):
#         ## Check for conflicts. If conflicts return -10
#         num_conflicts = 0
#         for s in self.major_students:
#             for day in s["reserved"]:
#                 for time in day:
#                     if time > 1:
#                         #print("Major students")
#                         #print(s["major"], s["level"])
#                         num_conflicts += time

#         for s in self.rooms:
#             for day in s["reserved"]:
#                 for time in day:
#                     if time > 1:
#                         #print("room")
#                         #print(day)
#                         num_conflicts += time
#         for s in self.lecturers:
#             for day in s["reserved"]:
#                 for time in day:
#                     if time > 1:
#                         #print("lecturers")
#                         #print(day)
#                         num_conflicts += time

#         if num_conflicts != 0:
#             return num_conflicts * -1

#         fit = fitness.calculate_fitness(schedule)

#         fit = fit / 2000000.0
#         fit = fit * 8

#         return fit
