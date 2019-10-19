import time
from espeak import espeak

def main():
    f = open("data.txt","r")
    f1 = f.readlines()
    classa = {}
    for x in f1:
        time.sleep(1)
        print x
        print
        print time.time()
        if x in classa.keys():
            if((time.time() - classa[x])>5):
                classa[x] = time.time()
                espeak.synth(x)
        else:
            classa[x] = time.time()
            espeak.synth(x)
        for item in classa.items():
            print item
        print

if __name__ == "__main__":
    main()