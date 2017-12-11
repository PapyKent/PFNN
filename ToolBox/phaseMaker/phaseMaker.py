import numpy

def main():
    f = open('LocomotionFlat01_000_footsteps.txt')
    p = open('test.phase','w')
    p = open('test.phase','a')
    lines = f.readlines()
    i = 1;
    first = lines[0].split(" ")
    while(i<int(first[0])):
        p.writelines("0.00000\n")
        i+=1

    for line in lines:
        line = line.rstrip()
        data=line.split(" ")
        if(len(data)!=2):
            print("break")
            break;
        if(i<int(data[0])):
            start = i
            while(i<int(data[0])):
                n=float(i-start)/(float(int(data[0])-start)*2)+0.5
                p.write("{0:.5f}".format(n)+'\n')
                i=i+1

        while(i<int(data[1])):
            n=(float(i)-float(data[0]))/((float(data[1])-float(data[0]))*2.0)
            p.write("{0:.5f}".format(n)+'\n')
            i=i+1

    f.close
    p.close


if __name__ == "__main__":
    main()
