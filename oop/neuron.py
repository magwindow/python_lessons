class Neuron:
    def __init__(self):
        self.weight = 0.6209990000282116  # default 0.001
        self.last_error = 1.1
        self.smoothing = 0.00001
        
    def get_last_error(self):
        return self.last_error
    
    def get_weight(self):
        return self.weight
    
    def get_smoothing(self):
        return self.smoothing
    
    def process_input_data(self, input_data):
        return input_data * self.weight
    
    def train(self, input, expectedResult):
        result_now = input * self.weight
        self.last_error = expectedResult - result_now
        correction = self.last_error / result_now
        correction = correction * self.smoothing
        self.weight += correction
        
    def check_training(self):
        return True if self.last_error > self.smoothing or self.last_error < -self.smoothing else False
    
    
neuron = Neuron()

input_data = 10  # 10 km
expectedResult = 6.21 # 6.21 miles

print(neuron.process_input_data(input_data))  # 1.0 



def start_training():
    iteration = 1
    while neuron.check_training():
        neuron.train(input_data, expectedResult)
        # print(f'Iteration {iteration}: Weight: {neuron.process_input_data(input_data)}')
        iteration += 1
        
    print('Successful training!')
    print(neuron.get_weight())  # 0.6209990000282116
    print(neuron.process_input_data(input_data))  # 6.209990000282116
    

# start_training()