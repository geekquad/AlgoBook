#this programe checks wheather given sequence of parenthesis is balanced or not using stack


stk = []
def push(c):
    stk.append(c)

def pop():
    global stk
    if len(stk)>=1:
        stk.pop()
    else:
        print('Stack is empty now')


def is_empty():
   # print(len(stk))
    if len(stk)==0:
        return True
    else:
        return False


def check(s):
    flag=0
    for i in range(len(s)):
        if s[i]=='(':
            push(s[i])

        else:
            if is_empty():
                print('Stack is empty!!!')
                print('Operation fail!')
                flag=1
                break
            else:
                pop()
      #  print(s[i])

    if is_empty() and flag!=1:
        print('Operation successful!!!')
        return True
    else:
        return False


if __name__=='__main__':
    s=input("Enter a sequence containing either '(' or ')': ")
    chk=check(s)
    if chk:
        print('Yes! the sequence is balanced')
    else:
        print('No! there is something missing.')
