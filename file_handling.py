import os
try:
    while 1:
        print("FILE HANDLING MENU!")
        print("\n")
        print("0: create new file")
        print("1: read file")
        print("2: write file ")
        print("3: append file ")
        print("4: renaming file ")
        print("5: deleting file ")
        print("6: copying file ")
        print("7: encoding file ")
        print("\n")
        print("Enter your choice")
        ch=int(input())
        if ch<0 and ch>7:
            print('CHOICE ENTER IS INVALID!')
   
       
        elif ch==0:
            fname=input('enter name for file')
            f=open('C:\\Users\\HP\\Desktop\\'+fname+'.txt','wb+')
            print(f.read())
            f.close()

        elif ch==1:
            fname=input('enter name for file')
            f=open('C:\\Users\\HP\\Desktop\\'+fname+'.txt','r')
            fo=f.read()
            print(fo)
            f.close()

        elif ch==2:
            fname=input('enter name for file:')
            f=open('C:\\Users\\HP\\Desktop\\'+fname+'.txt','w+')
            inpt=input("enter text to print in file! \n")
            f.write("\n")
            f.write(inpt)
            f.close()

        elif ch==3:
            fname=input('enter name for file:')
            f=open('C:\\Users\\HP\\Desktop\\'+fname+'.txt','a+')
            inpt=input("enter text to append in file!")
            f.write("\n")
            f.write(inpt)
            f.close()

        elif ch==4:
            fname=("enter current file name")
            c_n='C:\\Users\\HP\\Desktop\\'+fname+'.txt'
            fnname=("enter current file name")
            n_n='C:\\Users\\HP\\Desktop\\'+fnname+'.txt'
            os.rename(c_n,n_n)
            print('file renamed from {} to {}'.format(c_n,n_n))
            f.close()

        elif ch==5:
            f_name=input("enter file name you want to delete")
            n='C:\\Users\\HP\\Desktop\\'+f_name+'.txt'
            os.remove(n)
            print('file name {} deleted '.format(f_name))
            f.close()

        elif ch==6:
            old=input("enter file name to copy content")
            no='C:\\Users\\HP\\Desktop\\'+old+'.txt'
            new=input("enter file name to copy content")
            nn='C:\\Users\\HP\\Desktop\\'+new+'.txt'
            with open(old) as f:
                with open(nn, 'w') as f1:
                    for line in f:
                        f1.write(line)
            f.close()

        elif ch==7:
            en=input("enter file name to encode")
            ne='C:\\Users\\HP\\Desktop\\'+en+'.txt'
            f=open(ne,'w')
            print(f.encoding)
            f.close()
        else:
            print('ENTERED CHOICE IS INVALID!')
            userreply=input('do you want to continue (y,n)?')
            if userreply.lower()=='y':
                continue
            elif userreply.lower()=='n':
                break
           
   
       
except IOError:
    print('Error: can\'t find file or read data')
    
    
        


