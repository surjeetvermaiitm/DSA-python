def div(n):
    e,o=0,0
    x=int(pow(n,0.5))
    for i in range(1,x+1):
        if n%i==0:
            a=i
            b=n/i
            if a!=b:
                if a%2==0:
                    e+=1
                else:
                    o+=1
                if b%2==0:
                    e+=1
                else:
                    o+=1
            else:
                if a%2==0:
                    e+=1
                else:
                    o+=1
    return [o,e]
def div1(n):
    e,o=0,0
    a=2
    while n>0 and a<=n:
        if n%a==0:
            n=n/a
            if a%2==0:
                e+=1
            else:
                o+=1
        else:
            a+=1
    total=2**(o+e)-1
    od=2**o-1
    ev=total-od
    return [od+1,ev]
      
        
              


def solution(n):
    # Write solution here
    o,e=div1(n)
    #print(o,e)
    if o==e:
        return "PASS"
    elif o>e:
        return "SELL"
    else:
        return "BUY"


def main():
    n = int(input())
    #n=2
    print(solution(n))


if __name__ == "__main__":
    main()