a='-'
lst=[]
pas=open('password.txt')
users=pas.read().split()
users1=tuple(users)
for c in users1:
    lst.append(c.split('-'))
print(a*30)
print("Welcome to Database System")
print(a*30)
print("\nEnter Your Choice")
print("\n1.Login For Student")
print("\n2.Login For Instructor")
choice=int(input("Choice is:"))
#print(choice)
print(type(choice))

if choice==1:
    uname=input("Enter your ID:")
    psd=input("Enter Your Password:")

    for matchid,matchpsd in lst:
        if matchid == uname:
            if matchpsd == psd:
                print("Authenticated")
                f=1
                break
if f==1:
    print(a*30)
    print("Welcome",uname)
    print(a*30)
    print("1.Display your Marks")
    print("\n2.Calculate Percentage")
    print("\n3.Maximum abd Minimum Marks scored")
    print("\n4.Failed in how many Subjects")
    print("\n5.Change Password")
    print("\nEnter Your choice")
    choice1=int(input("choice is:"))
    if choice1==1:
        marks=open('marks.txt')
        marks1=tuple(marks.read().split())
        #print(marks1)
        i=0
        while i<7:
            strat=str(marks1[i])
            strat3=strat.split('-')
            strat2=str(strat3[0])
            #print(strat2)
            #strat2=str(strat1[0])
            if strat2==uname:
                print("Here are the Marks")
                print(marks1[i])
                break
            i=i+1
    elif choice1==2:
        marks=open('marks.txt')
        marks1=tuple(marks.read().split())
        print("hi")
        print(marks1)
        i=0
        while i<5:
            strat=str(marks1[i])
            strat3=strat.split('-')
            print(strat3)
            strat2=str(strat3[0])
            print(strat2)
            if strat2==uname:
                strat3[0]=0
                alpha=0
                for j in strat3:
                    alpha=alpha+int(j)
                perc=float(alpha/5)
                print("\nThe Percentage is",perc)
                break

            print(i)
            i=i+1
    elif choice1==3:
        marks=open('marks.txt')
        marks1=marks.read().split()

# hey i added comment at last
#add this
pas.close()
marks.close()
