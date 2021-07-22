#import numpy and other neccessary prerequisites
try:
    import numpy as np
    ###############################
    from hypo_modules import *
    ###############################
    from time import sleep as nappy

except:
    print('error-> phase-I')


#constucting a matix
crude_matrix  = np.array(
    [['1', '2', '3'],
     ['4', '5', '6'],
     ['7', '8', '9']]

)

#guidlines to play the game
instructions =  ['1) This game mandatorily requires 2 users or players for playing it...',
                 '2) Input the empty aisled numbers to clinch your element(X or O) there...',
                 '3) It starts with X',
                 "4) Enjoy.. that's all.. yup seriously that's all."]

#rendering out the instructions
for i in instructions:
    print(i)
    nappy(1)


#turn initialization
total_turns = 0

while total_turns<9:

    if total_turns%2==0:
        char = 'X'
    
    else:
        char = 'O'
    

    
    final_output = F'''

{crude_matrix[0,0]} | {crude_matrix[0,1]} | {crude_matrix[0,2]}

__  __  __

{crude_matrix[1,0]} | {crude_matrix[1,1]} | {crude_matrix[1,2]}

__  __  __

{crude_matrix[2,0]} | {crude_matrix[2,1]} | {crude_matrix[2,2]}

'''

    print(final_output)
     

    #----------------------------------------------------------------->>>>>

    while True:        
        try:
            swap_val = (int(input('enter the number you wanna place {0} in: '.format(char))))
            ########
            break

        except:
            print('Ooopss.. invalid input.. give it a shot again!!!')
    
    #---------------------------------------------------------------------->>>>>

    swap_val_func(int(swap_val), char, crude_matrix)
    
    

    #---------------------------------------------------------------------->>>>>

    a = first_row(crude_matrix)
    b = second_row(crude_matrix)
    c = third_row(crude_matrix)
    d = first_clmn(crude_matrix)
    e = second_clmn(crude_matrix)
    f = third_clmn(crude_matrix)
    g = left_diag(crude_matrix)
    h = right_diag(crude_matrix)


    if a[0]:
        nappy(0.5)
        print(F'{a[1]} savored victory this time ')
        break

    elif b[0]:
        nappy(0.5)
        print(F'{b[1]} savored victory this time ')
        break

    elif c[0]:
        nappy(0.5)
        print(F'{c[1]} savored victory this time ')
        break

    elif d[0]:
        nappy(0.5)
        print(F'{d[1]} savored victory this time ')
        break

    elif e[0]:
        nappy(0.5)
        print(F'{e[1]} savored victory this time ')
        break

    elif f[0]:
        nappy(0.5)
        print(F'{f[1]} savored victory this time ')
        break

    elif g[0]:
        nappy(0.5)
        print(F'{g[1]} savored victory this time ')
        break

    elif h[0]:
        nappy(0.5)
        print(F'{h[1]} savored victory this time ')
        break

    else:
        pass
    
    total_turns+=1


    nappy(0.5)











