import time

InvasionTimer = 1550448000  #18.03.2019 02:00
InvasionDur = 68400         #19 saat
InvasionActiveDur = 25200   #7 saat
def checkInv():
    currTime = time.time()
    
    print(currTime)
    elapsed = currTime - InvasionTimer
    print("Elapsed = "+str(elapsed))

    while elapsed > InvasionDur:
        elapsed = elapsed - InvasionDur
    t = InvasionDur - elapsed
    print("Elapsed = "+str(elapsed))
    print("T = "+str(t/60/60))
    print(InvasionActiveDur/60/60)
    if(t>InvasionActiveDur):
        
        diff_dived = (InvasionDur-t)/60
        diff_nodiv = (InvasionDur-t)
        if(InvasionDur-t)<60:
            print("Invasion is currently active for: "+str(diff_nodiv/60))
        else:
            print("Invasion is currently active for: "+str(diff_dived/60))
    else:
        print("Invasion will start in: "+str(t/60/60))
        


checkInv()
print(time.time())