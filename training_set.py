class Training_set:
    def __init__(self, target_input, target_output, iterations=10):
        self.input = target_input
        self.output = target_output
        self.training_iterations = iterations
