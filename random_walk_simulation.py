import numpy as np
import matplotlib.pyplot as plt
def main():
    def numbers():
        global first,market1
        market1=np.array([80])
        first=80
        for i in range(99):
            first=round(first*(1+np.random.normal(0,0.02)))
            market1=np.append(market1,first)
        print(market1)
    numbers()
    def average():
        avg=np.mean(market1[1:8])
        print(avg)
    average()
    def extreme():
        max=np.max(market1)
        min=np.min(market1)
        std=np.std(market1)
        print(f'max:{max}')
        print(f'min:{min}')
        print(f'std:{std}')
    extreme()
    def graph():
        xcords=np.arange(1,101)
        ycords=market1
        plt.title('market')
        plt.xticks(np.arange(0,101,5))
        plt.yticks(np.arange(0,np.max(market1)+5,5))
        plt.plot(xcords,ycords)
        plt.xlabel('days')
        plt.ylabel('value')
        plt.show()
    graph()
main()
        


        
    
        
    
    



 
    
    
    
    
    





