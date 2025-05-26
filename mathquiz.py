import random

def generate_qn():
    num1=random.randint(1,10)
    num2=random.randint(1,10)

    operator = random.choice(['+','-','*','/'])

    if operator=='+':
        ans= num1+num2
    elif operator=='-':
        ans= num1-num2
    elif operator=='*':
        ans= num1*num2
    else:
        ans=num1/num2

    return f"{num1} {operator} {num2}",float(f"{ans:.2f}")
def main():

    
    print("-----Math Quiz-----")
    print("various math questions will be asked and u will have to give the correct answer")

    score=0
    round=5

    for i in range(round):
        question,correctans=generate_qn()
        

        print(f"Question {i+1}:",question)
        answer=float(input("enter the answer:"))

        if answer==correctans:
            print("Correct ans")
            score=score+10

    
    print(f"score={score}")
    if score==50:
        print("Congrats! u have got the perfect marks ")



main()