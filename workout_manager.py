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
class Exercise:
    def __init__(self, exercise, sets, reps):
        self.excercise = exercise
        self.sets = sets
        self.reps = reps
        self.storage = {}
    
    def enter_workout(self):
        f"Workout: {self.exercise}; Sets: {self.sets}; Reps: {self.reps}"
        return self.storage[self.exercise] = [self.sets, self.reps]
        

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
