import time
import sys # ignore
sys.path.insert(0,'.') # ignore
from Root.pswd import real_password

def check_password(password): # Don't change it
    if len(password) != len(real_password):
        return False
    for x, y in zip(password, real_password):
        time.sleep(0.1) # Simulates the wait time of the safe's mechanism
        if int(x) != int(y):
            return False
    return True

def crack_password():
    crack_time = 0.2
    attack_password = [0,0,0,0]
    position = 0
    while position != 4:
        #print("position: ",position)
        for digit in range(10):
            attack_password[position] = digit
            t1 = time.time()
            #print(attack_password)
            result = check_password(attack_password)
            t2 = time.time()
            if result == True:
                return "".join(str(n) for n in attack_password)
            check_time = t2-t1
            #print("time:",check_time)
            if(check_time >= crack_time):
                position += 1
                crack_time += 0.1
                break
        
password = crack_password()
print(password)
