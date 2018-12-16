'''
Little Petya has gotten a lot of homework to do tonight.
Luckily, her best friend Vasya has finished her homework and gave the book to Petya so our Petya can now simply copy the homework.
Petya is too lazy and doesn't even want to do this, hence she asked you to copy Vasya's homework into her book.
The teacher might suspect copying, hence she has asked you to replace all the capital letters to small letters in the homework as she believes this change will be sufficient to fool the teacher.
Formally, write a program to take Vasya's homework as input and print it with all small letters.

Input consists of multiple lines of text that denotes Vasya's answers

Output Print Vasya's answer in the exact same manner as she wrote it. Only make all the capital letters as small and everything else must remain the same
'''

lines = []
while True:
    line = input()
    if line:
        lines.append(line)
    else:
        break
text = '\n'.join(lines)

for x in lines:
    y=x.lower()
    print(y,end="\n")