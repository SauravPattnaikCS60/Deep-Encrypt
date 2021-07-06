#enigma library
from enigma.machine import EnigmaMachine

def getRotor(pin):
    '''Converts 3 digit pin into rotor keywords'''
    s = []
    for i in range(3):
        s1 = pin%10
        if s1 is 1:
            s.append('I');
        elif s1 is 2:
            s.append('II');
        elif s1 is 3:
            s.append('III');
        elif s1 is 4:
            s.append('IV');
        elif s1 is 5:
            s.append('V');
        pin = pin//10
        
    mstr = s[2]+" "+s[1]+" "+s[0]
    return mstr

def getPlug(plug):
    '''Converts 20 len password into 2char grouped space separated plug settings'''
    return ' '.join(plug[i:i+2] for i in range(0,len(plug),2))

class EnigmaEncrypt():
    def __init__(self,pin,plug):
        plug = plug.upper()
        self.machine = EnigmaMachine.from_key_sheet(
                rotors=getRotor(pin),
                reflector='B',
                ring_settings='21 15 16',
                plugboard_settings=getPlug(plug))

    def setRotorPosition(self,pos):
        '''sets initial rotor position'''
        self.machine.set_display(pos.upper());
    
    def process(self,string):
        '''Processes a string'''
        return self.machine.process_text(string)