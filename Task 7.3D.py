import RPi.GPIO as GPIO
import time




GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


TRG = 17
ECO = 27
LED = 25




GPIO.setup(TRG,GPIO.OUT)
GPIO.setup(ECO,GPIO.IN)
GPIO.setup(LED,GPIO.OUT)


PWM = GPIO.PWM(LED,80)
PWM.start(0);



def Dist():
    
    
    GPIO.output(TRG, True)
    time.sleep(0.01)
    
   
    GPIO.output(TRG,False)
    
    
    StartTime = time.time()
    StopTime = time.time()
    
    
    
    while GPIO.input(ECO) == 0:
        StartTime = time.time()
        
    while GPIO.input(ECO) == 1:
        StopTime = time.time()
        
        
    TimeElapsed = StopTime - StartTime
    
    Dist  = (TimeElapsed * 34300)/2
    
    
    if(Dist <=40):
        PWM.ChangeDutyCycle(100 - Dist * 2)
        
        time.sleep(0.7)
        
    else:
        PWM.ChangeDutyCycle(0)
        
        time.sleep(1)

if __name__=='__main__':
    
    try:
        while True:
            Dist()
            
        
    except KeyboardInterrupt:

        PWM.stop()
        GPIO.cleanup()
    