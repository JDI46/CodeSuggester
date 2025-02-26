# class GetWorkout:
#     def __init__(self):
#
#
#     def recieved_workout(self):
#         pass
#
#     def difficulty_check():
#         pass
#
class Suggest:
    def __init__(self, code_block, goal):
        self.day = day
        self.excercise = exercise
        self.sets = sets
        self.reps = reps
        self.storage = {}
    
    def enter_workout(self):
        workout = f"Workout: {self.exercise}; Sets: {self.sets}; Reps: {self.reps}"
        return self.storage[self.day] == workout 

    def find_workouts(self):
    #looks for key and returns the string
    find_key = self.storage.get(self.day)
    return find_key

# class UserProfile:
#     pass
#
# class ProgressTracker:
#     pass
#
# class Suggestions:
#     pass
#
#
#
# class WeeklyResults:
#     pass

workout1 = Exercise("Biceps", 3, 12)
print(workout1)
