from dataclasses import dataclass

@dataclass
class Constants:
    
    sigma=10
    b=8/3
    w=5*(10**(-3))
    tfinal=50000 #the final time!
    dt=10**(-3) #our time step!
    n= 5*10**7
    check_radius = 1

    funcy=np.array([funcya,funcyc])
    funcylabel=np.array(['a','c'])
    
const = Constants()


