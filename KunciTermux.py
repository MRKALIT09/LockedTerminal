#program Kunci Terminal By-Mando
#recode ? copy paste? Izin  Slur
#0853-6152-4681

import os,sys,time

x = "MR"
y = "KALIT09"

def login():
    user = raw_input("MASUKAN USURNAME NYA TOL : ")
    pasw = raw_input("MASUKAN PASSWORD NYA TOL : ")
    if user ==x and pasw ==y:
        print ("PASSWORD BETUL")
        time.sleep (2.5)
    else:
       print("PASSWORD SALAH")
       time.sleep (2.5)
       os.system("python2 KunciTermux.py")
if __name__ == "__main__":
       login()
