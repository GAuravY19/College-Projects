import os
import time

def WritingFunction(files): # FILE WRITING THE CONTENT FROM APPLIANCE FILE TO CONCLUION FILE
    with open('Conclusion.txt', 'w') as out_file:
        for line in files:
            out_file.write(line)


def concluding(name:str, energy): # FUNCTION TO DECIDE WHICH APPLIANCES ARE USING MORE ENERGY AND WHICH ARE IN OPTIMUM CONDITIONS
    print(energy)
    print(name)
    for i in range(len(name)):

        # ------------------- TUBE LIGHT --------------------------------
        if (name[i].lower() == 'tube light' and (energy[i] > 500)):
            file2 = '\solutions\TubeLight.txt'
            path = os.getcwd() + file2
            files = open(path, '+r')
            WritingFunction(files)


        # ------------------- AC --------------------------------
        elif (name[i].lower() == 'ac' and (energy[i] > 3500)):
            file1 = '\solutions\Ac.txt'
            path = os.getcwd() + file1
            files = open(path , 'r+')
            WritingFunction(files)


        # ------------------- FAN --------------------------------
        elif (name[i].lower() == 'fan' and (energy[i] > 2000)):
            file1 = '\solutions\Fans.txt'
            path = os.getcwd() + file1
            files = open(path, 'r+')
            WritingFunction(files)


        # ------------------- FRIDGE --------------------------------
        elif (name[i].lower() == 'fridge' and (energy[i] > 1500)):
            file1 = '\solutions\Fridge.txt'
            path = os.getcwd() + file1
            files = open(path, 'r+')
            WritingFunction(files)


        # ------------------- GEYSER --------------------------------
        elif (name[i].lower() == 'geyser' and (energy[i] > 2000)):
            file1 = '\solutions\Geyser.txt'
            path = os.getcwd() + file1
            files = open(path, 'r+')
            WritingFunction(files)


        # ------------------- LAPTOP --------------------------------
        elif (name[i].lower() == 'laptop' and (energy[i] > 2000)):
            file1 = '\solutions\Laptop.txt'
            path = os.getcwd() + file1
            files = open(path, 'r+')
            WritingFunction(files)



        # ------------------- MIXER --------------------------------
        elif (name[i].lower() == 'mixi' and (energy[i] > 2000)):
            file1 = '\solutions\mixer.txt'
            path = os.getcwd() + file1
            files = open(path, 'r+')
            WritingFunction(files)


        # ------------------- OVEN --------------------------------
        elif (name[i].lower() == 'microwave oven' and (energy[i] > 2000)):
            file1 = '\solutions\oven.txt'
            path = os.getcwd() + file1
            files = open(path, 'r+')
            WritingFunction(files)


        # ------------------- TV --------------------------------
        elif name[i].lower() == 'tv' and (energy[i] > 2000):
            file1 = '\solutions\Tv.txt'
            path = os.getcwd() + file1
            files = open(path, 'r+')
            WritingFunction(files)


        # ------------------- WASHING MACHINE --------------------------------
        elif name[i].lower() == 'washing machine' and (energy[i] > 2000):
            file1 = '\solutions\washing.txt'
            path = os.getcwd() + file1
            files = open(path, 'r+')
            WritingFunction(files)


if __name__ == "__main__":
    # ---------------- REMOVING THE CONCLUSION FILE IF ALREADY EXISTS ------------------------------

    con = 'Conclusion.txt'
    location = 'C:/Users/sunil/OneDrive/Desktop/green computing web app/'
    conpath = os.path.join(location, con)

    if os.path.exists(conpath):
        os.remove(conpath)

    # ---------------- REMOVING THE CONCLUSION FILE IF ALREADY EXISTS ------------------------------

    time.sleep(1)

    concluding()




