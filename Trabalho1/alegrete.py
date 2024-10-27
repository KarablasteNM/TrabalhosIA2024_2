import numpy as np

def compute_mse(b, w, data):
    
    erro = 0
    for i, j in data:
        erro += ((b + w * i) - j) ** 2
    erro /= len(data)
    return erro

def step_gradient(b, w, data, alpha):
    
    deriv_theta_zero = 0
    deriv_theta_um = 0
    m = len(data)

    for x, y in data:
        deriv_theta_zero += 2 * ((w * x + b) - y)
        deriv_theta_um += 2 * x * ((w * x + b) - y)

    deriv_theta_zero /= m
    deriv_theta_um /= m
   
    b -= alpha * deriv_theta_zero
    w -= alpha * deriv_theta_um

    return b, w

def fit(data, b, w, alpha, num_iterations):
    b_s = []
    w_s = []

    for i in range(num_iterations):
        b, w = step_gradient(b, w, data, alpha)

        b_s.append(b)
        w_s.append(w)

    return b_s, w_s
