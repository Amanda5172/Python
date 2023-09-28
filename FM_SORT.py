import random
import string

def bubblesort(mylist, order):
    ans=[]
    ub = len(mylist)
    swap=True

    if order=='ascending':
        while swap==True and ub!=0:
            swap=False
            for i in range(0,ub-1):
                if mylist[i] > mylist[i+1]:
                    t= mylist[i]
                    mylist[i]= mylist[i+1]
                    mylist[i+1] = t
                    swap=True
            ub = ub-1
            ans.append(list(mylist))            
            
    elif order=='descending':
        while swap==True and ub!=0:
            swap=False
            for i in range(0,ub-1):
                if mylist[i] < mylist[i+1]:
                    t= mylist[i]
                    mylist[i]= mylist[i+1]
                    mylist[i+1] = t
                    swap=True
            ub = ub-1
            ans.append(list(mylist))
            
    return ans

def quicksort(mylist,order):
    
    return [[1,2],[3,4]]


def randomlist(n, data):
    r=[]
    for i in range(n):
        if data == 'numbers':
            val = random.randint(0,50)
        elif data == 'letters':
            val = random.choice(string.ascii_uppercase)
        r.append(val)
    return r


def question():
    n = int(input("Length of list: "))
    print()
    so=random.randint(0,1)
    d=random.randint(0,1)
    other=random.randint(0,1)
    data = ['numbers', 'letters'][d]
    mylist = randomlist(n,data)
    if so==0:
        order = ['ascending', 'descending'][other]
        print(f"Arrange the {data} below in {order} order using a:")
        print("(a) bubble sort", "(b) quick sort")
        ans1 = bubblesort(mylist,order)
        ans2 = quicksort(mylist,order)
    elif so==1:
        sort = ['bubble','quick'][other]
        print(f"Use a {sort} sort to arrange the {data} below in:")
        print("(a) ascending order", "(b) descending order")
        if sort=='bubble':
            ans1 = bubblesort(mylist,'ascending')
            ans2 = bubblesort(mylist,'descending')
        elif sort=='quick':
            ans1 = quicksort(mylist,'ascending')
            ans2 = quicksort(mylist,'descending')
        
    print(mylist)
    print()
    sol=input("Check the solutions? ")
    print("(a)")
    ansprint(ans1)
    print()
    print("(b)")
    ansprint(ans2)

def ansprint(ans):
    for i in range(len(ans)):
        print(ans[i])


def main():
    question()

if __name__ == "__main__":
    main()






