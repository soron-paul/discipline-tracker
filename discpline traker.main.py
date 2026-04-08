import os

print("1.new account")
print('2.old acound')

a=int(input("Your choice:"))

dictionary={}
if(a==1):
    b=int(input("how many discplins do you want?"))
    print("your discplines:")
    for i in range(b):
        dec=input()
        dictionary[dec]=0
        
       
    with open("C:/Users/USER/Desktop/python/dec.py/dec.store","w") as f :
        for key,value in dictionary.items():
            f.write(f"{key}:{value}\n") 

#resating day count
    with open("C:/Users/USER/Desktop/python/dec.py/dec.totalday","w") as f:
        f.write("0")
        

   


    print("i'd created")   

elif(a==2):

#checking for existing file

    if not os.path.exists("C:/Users/USER/Desktop/python/dec.py/dec.store") or os.path.getsize("C:/Users/USER/Desktop/python/dec.py/dec.store") == 0:
    
        print("Please create your account first")
    else:
        print("1.Daily input")
        print("2.Analyse")
        m=int(input("Your choice"))

        if(m==1):

#Adding the count of days

            with open("C:/Users/USER/Desktop/python/dec.py/dec.totalday") as f:
                h=int(f.read())
                h+=1
            with open("C:/Users/USER/Desktop/python/dec.py/dec.totalday","w") as f:
                f.write(str(h))

#making dictionary and list of keys

            with open("C:/Users/USER/Desktop/python/dec.py/dec.store") as f:
                for line in f:
                    line=line.strip()
                    key,value = line.split(":")
                    dictionary[key]=int(value)

            list=list(dictionary.keys())

            for k in list:
                values=input(f"{k}:yes/no ")
    
                if(values=="yes"):

                    dictionary[k]+=1

                elif(values!="yes" and values!="no"):
                    print("pls chose only yes or no")

            with open("C:/Users/USER/Desktop/python/dec.py/dec.store","w") as f:
                for key,value in dictionary.items():
                    f.write(f"{key}:{value}\n")

        elif(m==2):

#making dictionary 

            with open("C:/Users/USER/Desktop/python/dec.py/dec.store") as f:
                for line in f:
                    line.strip()
                    key,value = line.split(":")
                    dictionary[key]=int(value)
        

            with open("C:/Users/USER/Desktop/python/dec.py/dec.totalday") as f:
                days=int(f.read())




            for key,value in dictionary.items():
                x=value/days*100
                print(key,":",x,"%","consistancy",value,"/",days)


        else:
            print("Pls chose 1 or 2")












else:
    print("Pls enter righr number. Thenk you")