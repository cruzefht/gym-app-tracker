import json
import matplotlib.pyplot as plt # type: ignore
exercise_list = ("pushups", "pull ups" , "bench press", "squats" , "cardio" , "leg press" , "overhead press" )

workout_plan = {}

num_exercises = int(input("how many exercises do you want to add to your workout plan? "))

for i in range(num_exercises): 
    exercise_name = input("enter the name of the exercise: ").lower()
   
    if exercise_name not in exercise_list:
        print("invalid exercise. Try again")
        continue
   
    rep_goal = int(input(f"enter the rep goal for {exercise_name}: "))
    set_goal = int(input(f"enter the set goal for {exercise_name}: "))
   
    workout_plan[exercise_name] = {
        "rep_goal": rep_goal,
        "set_goal": set_goal
    }
#ask user to input their current reps and sets for the chosen exercise
exercise_chosen = input("enter the exercise you want to log: ").lower()


if exercise_chosen not in exercise_list:
    print("invalid exercise. Try again")
    exit()


current_reps = int(input(f"enter the number of reps you did for {exercise_chosen}: "))
current_sets = int(input(f"enter the number of sets you did for {exercise_chosen}: "))

if exercise_chosen in workout_plan:
    rep_goal = workout_plan[exercise_chosen]["rep_goal"]
    set_goal = workout_plan[exercise_chosen]["set_goal"]
else:
    print("exercise not found in workout plan. Please add it first.")
    exit()

#evaluate performance for reps
if current_reps > rep_goal:
    print(f"well done you beat the rep goal by {current_reps - rep_goal} keep it up")
elif current_reps == rep_goal:
    print("well done you're on spot cuh! keep up the spirit")
else: 
    print(f"you're {rep_goal - current_reps} reps short of the goal, don't give up")

#evaluate performance for sets
if current_sets > set_goal:
    print(f"well done you beat the set goal by {current_sets - set_goal} keep it up")
elif current_sets == set_goal:
    print("well done you're on spot cuh!keep up the spirit")
else: 
    print(f"you're {set_goal - current_sets} sets short of the goal, don't give up")  

#------------------------------
#DATA STORAGE
#------------------------------
workout_data = {
    "exercise": exercise_chosen,
    "reps_done": current_reps,
    "sets_done": current_sets
} 
#-------------------------------
#LOAD EXISTING DATA SAFELY
#-------------------------------
try:
    with open("gymapp.json", "r") as file:
        workouts = json.load(file)
except FileNotFoundError:
    workouts = []   
#add new workout data 
workouts.append(workout_data)

#save updated workout data back to file
with open("gymapp.json","w") as file :
    json.dump(workouts, file, indent=4)  


exercise = exercise_chosen 
reps = []

for workout in workouts:
    if workout.get("exercise") == exercise:
        reps.append(workout["reps_done"])
if reps:
    plt.plot(reps)
    plt.title(f"{exercise} progress (reps)") 
    plt.xlabel("Workout Sessions")
    plt.ylabel("Reps Completed")
    plt.show()
else:
    print(f"No workout data found for {exercise}. Unable to plot progress.")    

#display workout history    
print("\n==================GYM HISTORY=========================")       
if len(workouts) == 0:
    print("no workouts recorded yet")
else: 
    for index,workout in enumerate(workouts, start=1):
        print(f"{index}. {workout['exercise']:<15} {workout['reps_done']:<10} {workout['sets_done']:<10}") 