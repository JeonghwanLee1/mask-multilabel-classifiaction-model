import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.autograd import Variable

def to_one_hot(y, n_dims=None):
    """ Take integer y (tensor or variable) with n dims and convert it to 1-hot representation with n+1 dims. """
    y_tensor = y.data if isinstance(y, Variable) else y
    y_tensor = y_tensor.type(torch.LongTensor).view(-1, 1)
    n_dims = n_dims if n_dims is not None else int(torch.max(y_tensor)) + 1
    y_one_hot = torch.zeros(y_tensor.size()[0], n_dims).scatter_(1, y_tensor, 1)
    y_one_hot = y_one_hot.view(*y.shape, -1)
    return Variable(y_one_hot) if isinstance(y, Variable) else y_one_hot

def get_label(path):
    label = 0 
    splitted = path.split('/')
    dr = splitted[-2]
    name = splitted[-1]
    if 'incorrect' in name:
        base = 6
    elif 'mask' in name:
        base = 0
    elif 'normal' in name:
        base = 12
    else:
        print(f"error : {f}")
        return -1
    
    label+=base
    
    if 'female' in dr:
        label+=3
    else:
        label+=0
    
    age = int(dr.split('_')[-1])
    if age<30:
        label+=0
    elif age<60:
        label+=1
    else:
        label+=2
    return label