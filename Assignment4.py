# Jacob Onbreyt
# EMPLID: 23756110
# CSc 33200
# Assignment 4 - Assignment4.py


import random # to generate random cylinder values
from tabulate import tabulate # to print results as a table

# FCFS (First Come First Serve) Algorithm
def FCFS(head_position, requests):
    head_movement = 0 # initializing head movement
    temp = requests.copy() # creating temporary array to hold requests
    temp.insert(0, head_position) # adding initial disk head position to temporary array as first request
    # Going through the array and subtracting adjacent requests
    # and adding each of the calculated values together for total head movement
    for i in range(len(temp)):
        if i != len(temp)-1:
            head_movement += abs(temp[i]-temp[i+1])
    return head_movement

# SCAN Algorithm (Elevator Algorithm)
def SCAN(head_position, requests, direction):
    head_movement = 0 # initializing head movement
    disk_arm_left = [] # for when disk arm goes left
    disk_arm_right = [] # for when disk arm goes right
    temp = [] # creating temporary array to hold requests
    temp.append(head_position) 
    if (direction == "Left" or "left"): # if arm is going in the left direction initially
        for i in requests:
            if i < head_position: # if cylinder is less than the initial head_position append it to the left array
                disk_arm_left.append(i)
            else: # if cylinder is greater than initial head position append it to the right array
                disk_arm_right.append(i)
        # combining arrays to make new temporary request array of SCAN traversal on disk
        disk_arm_left.sort(reverse = True)
        for i in disk_arm_left:
            temp.append(i)
        temp.append(0)
        disk_arm_right.sort()
        for i in disk_arm_right:
            temp.append(i)
    elif (direction == "Right" or "right"): # if arm is going in right direction initially
        for i in requests:
            if i > head_position: # if cylinder is greater than initial head position append it to the right array
                disk_arm_right.append(i)
            else:
                disk_arm_left.append(i) # if cylinder is less than the initial head_position append it to the left array
        # combining arrays to make new temporary request array of SCAN traversal on disk
        disk_arm_right.sort()
        for i in disk_arm_right:
            temp.append(i)
        temp.append(9999)
        disk_arm_left.sort(reverse = True)
        for i in disk_arm_left:
            temp.append(i)
    # Going through the array sorted in the manner SCAN traverses and subtracting adjacent requests
    # and adding each of the calculated values together for total head movement
    for i in range(len(temp)):
        if i != len(temp)-1:
            head_movement += abs(temp[i]-temp[i+1])
    return head_movement
    

# C-SCAN (Circular Scan) Algorithm
def CSCAN(head_position, requests, direction):
    head_movement = 0 # initializing head movement
    disk_arm_left = [] # for when disk arm goes left
    disk_arm_right = [] # for when disk arm goes right
    temp = [] # creating temporary array to hold requests
    temp.append(head_position)
    if (direction == "Left" or "left"): # if arm is going left initially
        for i in requests:
            if i < head_position:
                disk_arm_left.append(i)
            else:
                disk_arm_right.append(i)
        # combining arrays to make new temporary request array of SCAN traversal on disk
        disk_arm_left.sort(reverse = True)
        for i in disk_arm_left:
            temp.append(i)
        temp.append(0)
        temp.append(9999) # back to start 
        disk_arm_right.sort(reverse = True)
        for i in disk_arm_right:
            temp.append(i)
    elif (direction == "Right" or "right"): # if arm is going right initially
        for i in requests:
            if i > head_position:
                disk_arm_right.append(i)
            else:
                disk_arm_left.append(i)
        # combining arrays to make new temporary request array of SCAN traversal on disk
        disk_arm_right.sort()
        for i in disk_arm_right:
            temp.append(i)
        temp.append(9999)
        temp.append(0) # back to start
        disk_arm_left.sort()
        for i in disk_arm_left:
            temp.append(i)
    # Going through the array sorted in the manner that C-SCAN traverses and subtracting adjacent requests
    # and adding each of the calculated values together for total head movement
    for i in range(len(temp)):
        if i != len(temp)-1:
            head_movement += abs(temp[i]-temp[i+1])
    return head_movement


print("\t\t******** DISK SCHEDULING ALGORITHMS ******** ")
cylinders = 10000
requests_range = 1000
head_position = int(input("Provide the Initial Position of the Disk Head (0-9999 cylinders): "))
while (head_position > 9999):
    print("Position Invalid! Please enter a better integer")
    head_position = int(input())
print("Total Number of Cylinders = ", cylinders)
print("Total Number of Requests = ", requests_range, "\n")
requests = []
for i in range(requests_range):
    req = random.randint(0,cylinders) # generating 1000 random requests of cylinders 0-9999
    requests.append(req)
# Printing Total Head Movement for each algorithm as a table
data = [["FCFS", FCFS(head_position, requests)],
["SCAN (from left)", SCAN(head_position,requests,"left")],
["SCAN (from right)", SCAN(head_position,requests,"right")],
["C-SCAN (from left)", CSCAN(head_position,requests,"left")],
["C-SCAN (from right)", CSCAN(head_position,requests,"right")]]
print(tabulate(data, headers=["Disk-Scheduling Algorithm", "Total Head Movement"]), "\n")


