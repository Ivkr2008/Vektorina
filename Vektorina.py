from random import shuffle


file=open("Вопросы.txt","r",encoding="utf-8")
questions=[]
score = 0
for line in file:
    questions.append(line.strip().split("#"))
    
for x in questions:
    print(x[0])
    answers=x[1:]
    shuffle(answers)
    for e in range (1, len(answers)+1):
        print(e,") " ,answers [e-1],sep='')

 
    number=int(input("Номер ответа: ")) - 1
    s=x[1]
    
    if answers[number] == s:
        score += 1
        print("Всё верно!")
    else:
        print("Что то не так.")
name = input("Имя: ")
score = int(score / len(questions) * 100)
print("Ты ныбрал", score, "очков")      
file=open("Record.txt","a",encoding="utf-8")
file.write(name + " " + str(score)+"\n")

file.close()
file=open("Record.txt","r",encoding="utf-8")
Records = file.read().strip(). split("\n")
b =[]
for i in Records:
    a = i.split(" ")
    a[1] = int(a[1])
    b.append(a)
for i in range(len(b)):
    for q in range(len(b)-1):
        if b[q][1] > b[q+1][1]:
            b[q],b[q+1] = b[q+1], b[q]

print(join(b))