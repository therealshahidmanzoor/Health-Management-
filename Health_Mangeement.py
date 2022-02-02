from datetime import *
def Shahid_food():
    f1=open("python\Mini-Project\Shahid_food.txt",'a')
    curr_time=str(datetime.now())
    food_list=[]
    global i
    num1=int(input("Enter the no.of items of food you ate:->"))
    for i in range(num1):
        food_item=input("Enter food item:->")
        food_list.append(food_item)
    f1.write(f"{curr_time}:->")
    for i in food_list:
        f1.write(f"|{i}\n")
    f1.close()

def Shahid_exe():
    f2=open("python\Mini-Project\Shahid_exercise.txt",'a')
    curr_time=str(datetime.now())
    exe_list=[]
    num2=int(input("Enter the no.of items of exercise you've done:->"))
    global i 
    for i in range(num2):
        exe=input("Enter Exercise:->")
        exe_list.append(exe)
    f2.write(f"{curr_time}:->")
    for i in exe_list:
        f2.write(f"|{i}\n")
    f2.close()

def John_food():
    f3=open("python\Mini-Project\John_food.txt",'a')
    curr_time=str(datetime.now())
    food_list=[]
    global i
    num1=int(input("Enter the no.of items of food you ate:->"))
    for i in range(num1):
        food_item=input("Enter food item:->")
        food_list.append(food_item)
    f3.write(f"{curr_time}:->")
    for i in food_list:
        f3.write(f"|{i}\n")
    f3.close()

def John_exe():
    f4=open("python\Mini-Project\John_exercise.txt",'a')
    curr_time=str(datetime.now())
    exe_list=[]
    num2=int(input("Enter the no.of items of exercise you've done:->"))
    global i 
    for i in range(num2):
        exe=input("Enter Exercise:->")
        exe_list.append(exe)
    f4.write(f"{curr_time:}:->")
    for i in exe_list:
        f4.writelines(f"{i}\n")
    f4.close()

print("========HEALTH MANAGEMENT SYSTEM MINIPROJECT========")
while True:
    name=int(input("1.Shahid\n2.john:->\nEnter your choice:->"))
    if name==1:
        ch=int(input("1.Food\n2.Exercise\nEnter your choice:->"))
        if ch==1:
            Shahid_food()
        else:
            Shahid_exe()
    else:
        ch=int(input("1.Food\n2.Exercise\nEnter your choice:->"))
        if ch==1:
            John_food()
        else:
            John_exe()



    
    
    

    