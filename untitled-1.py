# Test

def main():
    print ("hello world")

if __name__ == '__main__':
    None

##version 0.0.1
##Trying to make a simple text-based adventure

#Variables

q1 = "asdf"

#Functions

def ask(question):
    print (question)
    ans = input()
    print(ans)
    print("-----")
    return ans

#Start of i/o

ans = ask(q1)