
class Prompt:
    def __init__(self, prompt, code_block, goal):
        self.prompt = prompt
        self.code_block = code_block
        self.goal = goal
    
    def enter_prompt(self):
        return self.prompt == ""

    def desired_outcome(self):
        pass


