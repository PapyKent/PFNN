import numpy

def main():
    
    file_path = '../data/injuries/'
    file_name = 'Injured_Walk_RUL_extended_converted'
    
    f = open(file_path+file_name+'_footsteps.txt')
    p = open(file_path+file_name+'.phase','w') #output file name
    p = open(file_path+file_name+'.phase','a')
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
