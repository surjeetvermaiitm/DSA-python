def solution(files):
    # Write solution here
    m={k:files.count(k) for k in files}
    ans=0
    for k in m:
        if m[k]%2==0:
            ans+=m[k]
        else:
            ans=ans+m[k]-1
    ans=ans+1
    return ans


def main():
    #str = input()
    str="aa"
    answer = solution(str)
    print(answer)


if __name__ == '__main__':
    main()