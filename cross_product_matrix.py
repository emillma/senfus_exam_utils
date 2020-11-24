def cross_product_matrix(vector):

    S = [[0, -vector[2], vector[1]],
         [vector[2], 0, -vector[0]],
         [-vector[1], vector[0], 0]]

    return S
