v1 = [3, -7, -2]
v2 = [2, 12, 5]
v3 = []
alpha = 5
def alpha_x_v(v1,alpha):
    v3 = [x*alpha for x in v1]
    return(v3)
alpha_x_v(v1,alpha)

#def vec_eq():
    #if v1 == v2:
    #    print("Those vectors are equal.")
    #else:
    #    print("False.")
#vec_eq()

v1 = [3, -7, -2]
v2 = [2, 12, 5]
v3 = []
alpha = 5
def v_mult_v(v1,v2):
    result = [x*y for x,y in zip(v1,v2)]
    return(result)
v_mult_v(v1,v2)

v1 = [3, -7, -2]
v2 = [2, 12, 5]
alpha = 5
def v_add_v(v1,v2):
    new_result = [x+y for x,y in zip(v1,v2)]
    return(new_result)
v_add_v(v1,v2)

v1 = [3, -7, -2]
v2 = [2, 12, 5]
alpha = 5
def solution_to_problem():
        print(v_add_v(alpha_x_v(v1,alpha)),(alpha_x_v(v2,-1))))
solution_to_problem()
