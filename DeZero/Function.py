import numpy as np
from .Variable import Variable
def as_array(input_data):
    """
    将输入数据转换为numpy ndarray
    """
    if not isinstance(input_data, np.ndarray):
        input_data = np.array(input_data)
    return input_data

class Function:
    def __call__(self, *inputs):
        xs = [x for x in inputs]
        ys = self.forward(xs)
        outputs = [Variable(as_array(y)) for y in ys]
        for output in outputs:
            output.set_creator(self)
        self.inputs = inputs
        self.outputs = ys
        return outputs if len(outputs) > 1 else outputs[0]

    def forward(self, inputs):
        raise NotImplementedError()
    
    def backward(self, *output_grads):
        raise NotImplementedError()