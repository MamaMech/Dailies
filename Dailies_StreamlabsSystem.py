# ---------------------------
#   Import Libraries
# ---------------------------
import os
import sys
import json
import codecs
import clr

sys.path.append(os.path.join(os.path.dirname(__file__), "lib"))  # point at lib folder for classes / references

clr.AddReference("IronPython.SQLite.dll")
clr.AddReference("IronPython.Modules.dll")

# Import your Settings class
# from Settings_Module import MySettings

# ---------------------------
#   [Required] Script Information
# ---------------------------

ScriptName = "Dailies"
Website = "https://www.twitch.tv/mamamech"
Description = "Keeps track of daily activities and makes them interactive."
Creator = "MamaMech"
Version = "1.0.0"

# ---------------------------
#   [Required] Initialize Data (Only called on load)
# ---------------------------
def Init():
    return

# ---------------------------
#   [Required] Execute Data / Process messages
# ---------------------------
def Execute(data):
    if data.GetParam(0).lower() == "!resetdailies" and Parent.HasPermission(data.User, "Moderator", ""):
        clear_entries()
        write_entries()
        Parent.SendStreamMessage("Dailies have been reset!")
    elif data.GetParam(0).lower() == "!outfit" and "!outfit" in get_entries():
        Parent.AddPoints(data.User, data.UserName, 100)
        clear_entry("!outfit")
        Parent.SendStreamMessage(data.UserName + ", thanks for marking this off my list. Here is 100 bells!")
    elif data.GetParam(0).lower() == "!mail" and "!mail" in get_entries():
        Parent.AddPoints(data.User, data.UserName, 100)
        clear_entry("!mail")
        Parent.SendStreamMessage(data.UserName + ", thanks for marking this off my list. Here is 100 bells!")
    elif data.GetParam(0).lower() == "!recycle" and "!recycle" in get_entries():
        Parent.AddPoints(data.User, data.UserName, 100)
        clear_entry("!recycle")
        Parent.SendStreamMessage(data.UserName + ", thanks for marking this off my list. Here is 100 bells!")
    elif data.GetParam(0).lower() == "!abd" and "!abd" in get_entries():
        Parent.AddPoints(data.User, data.UserName, 100)
        clear_entry("!abd")
        Parent.SendStreamMessage(data.UserName + ", thanks for marking this off my list. Here is 100 bells!")
    elif data.GetParam(0).lower() == "!shake" and "!shake" in get_entries():
        Parent.AddPoints(data.User, data.UserName, 100)
        clear_entry("!shake")
        Parent.SendStreamMessage(data.UserName + ", thanks for marking this off my list. Here is 100 bells!")
    elif data.GetParam(0).lower() == "!chop" and "!chop" in get_entries():
        Parent.AddPoints(data.User, data.UserName, 100)
        clear_entry("!chop")
        Parent.SendStreamMessage(data.UserName + ", thanks for marking this off my list. Here is 100 bells!")
    elif data.GetParam(0).lower() == "!pull" and "!pull" in get_entries():
        Parent.AddPoints(data.User, data.UserName, 100)
        clear_entry("!pull")
        Parent.SendStreamMessage(data.UserName + ", thanks for marking this off my list. Here is 100 bells!")
    elif data.GetParam(0).lower() == "!fossils" and "!fossils" in get_entries():
        Parent.AddPoints(data.User, data.UserName, 100)
        clear_entry("!fossils")
        Parent.SendStreamMessage(data.UserName + ", thanks for marking this off my list. Here is 100 bells!")
    elif data.GetParam(0).lower() == "!rocks" and "!rocks" in get_entries():
        Parent.AddPoints(data.User, data.UserName, 100)
        clear_entry("!rocks")
        Parent.SendStreamMessage(data.UserName + ", thanks for marking this off my list. Here is 100 bells!")
    elif data.GetParam(0).lower() == "!branches" and "!branches" in get_entries():
        Parent.AddPoints(data.User, data.UserName, 100)
        clear_entry("!branches")
        Parent.SendStreamMessage(data.UserName + ", thanks for marking this off my list. Here is 100 bells!")
    elif data.GetParam(0).lower() == "!bottle" and "!bottle" in get_entries():
        Parent.AddPoints(data.User, data.UserName, 100)
        clear_entry("!bottle")
        Parent.SendStreamMessage(data.UserName + ", thanks for marking this off my list. Here is 100 bells!")
    elif data.GetParam(0).lower() == "!water" and "!water" in get_entries():
        Parent.AddPoints(data.User, data.UserName, 100)
        clear_entry("!water")
        Parent.SendStreamMessage(data.UserName + ", thanks for marking this off my list. Here is 100 bells!")
    elif data.GetParam(0).lower() == "!roscoe" and "!roscoe" in get_entries():
        Parent.AddPoints(data.User, data.UserName, 100)
        clear_entry("!roscoe")
        Parent.SendStreamMessage(data.UserName + ", thanks for marking this off my list. Here is 100 bells!")
    elif data.GetParam(0).lower() == "!judy" and "!judy" in get_entries():
        Parent.AddPoints(data.User, data.UserName, 100)
        clear_entry("!judy")
        Parent.SendStreamMessage(data.UserName + ", thanks for marking this off my list. Here is 100 bells!")
    elif data.GetParam(0).lower() == "!muffy" and "!muffy" in get_entries():
        Parent.AddPoints(data.User, data.UserName, 100)
        clear_entry("!muffy")
        Parent.SendStreamMessage(data.UserName + ", thanks for marking this off my list. Here is 100 bells!")
    elif data.GetParam(0).lower() == "!sherb" and "!sherb" in get_entries():
        Parent.AddPoints(data.User, data.UserName, 100)
        clear_entry("!sherb")
        Parent.SendStreamMessage(data.UserName + ", thanks for marking this off my list. Here is 100 bells!")
    elif data.GetParam(0).lower() == "!ankha" and "!ankha" in get_entries():
        Parent.AddPoints(data.User, data.UserName, 100)
        clear_entry("!ankha")
        Parent.SendStreamMessage(data.UserName + ", thanks for marking this off my list. Here is 100 bells!")
    elif data.GetParam(0).lower() == "!undo" and Parent.HasPermission(data.User, "Moderator", ""):
        write_entry("!" + data.GetParam(1))
        Parent.SendStreamMessage("!" + data.GetParam(1) + " has been added back to the list. Please manually remove bells and take appropriate displinary action.")
    elif data.GetParam(0).lower() == "!dailies":
        Parent.SendStreamMessage(", ".join(get_entries()))




# ---------------------------
#   [Required] Tick method (Gets called during every iteration even when there is no incoming data)
# ---------------------------
def Tick():
    return

def get_entries():
    try:
        with open('dailies.txt') as file:
            lines = file.readlines()
            lines = [line.rstrip() for line in lines]
            return lines
    except:
        return[]

def write_entries():
    textfile = open("dailies.txt", "w")
    for element in dailies_list:
        textfile.write(element + "\n")
    textfile.close()

def write_entry(task):
    entries = "\n".join(get_entries())
    with open('dailies.txt', 'w') as file:
        file.write(str(entries) + "\n" + str(task))

def clear_entry(task):
    with open("dailies.txt", "r") as f:
        lines = f.readlines()
    with open("dailies.txt", "w") as f:
        for line in lines:
            if line.strip("\n") != task:
                f.write(line)

def clear_entries():
    f = open('dailies.txt', 'r+')
    f.truncate(0)

dailies_list = [
"!outfit",
"!mail",
"!recycle",
"!abd",
"!shake",
"!chop",
"!pull",
"!fossils",
"!rocks",
"!branches",
"!bottle",
"!water",
"!roscoe",
"!judy",
"!muffy",
"!sherb",
"!ankha"
]

# test code

# class Data:
#     message = ""
#     User = "Sierra"
#     UserName = "Sierra"
#
#     def __init__(self, message):
#         self.message = message
#
#     def IsChatMessage(self):
#         return True
#
#     def GetParam(self, index):
#         try:
#             return self.message.split()[index]
#         except:
#             return ""
#
# class Parent:
#     user_points = 5001
#     user_is_mod = True
#
#     def Log(self, message):
#         return
#
#     def SendStreamMessage(self, message):
#         print(message)
#
#     def GetPoints(self, user):
#         return self.user_points
#
#     def RemovePoints(self, user, user_name, point_cost):
#         self.user_points = 5000 - point_cost
#
#     def HasPermission(self, user, perm, ignore):
#         return self.user_is_mod
#
#
# Init()
# Parent = Parent()
# while True:
#     msg = Data(raw_input())
#     Execute(msg)