key=['f','i','s','h',' ','s','t','i','c','k','s']
ans=['*','*','*','*',' ','*','*','*','*','*','*']
alp1=0;alp2=0;alp3=0;alp4=0;alp5=0;alp6=0;alp7=0;lives=0
print("Hangman\n",ans)
while True:
    if ans==key:break
    else:
        a=input()
        if a=='f':
            alp1=alp1+1
            if alp1<=1:
                ans[0] = 'f'
                print(ans)
            else:
                print(ans)
                lives=lives+1
        elif a=='i':
            alp2=alp2+1
            if alp2<=1:
                ans[1] = 'i'
                ans[7] = 'i'
                print(ans)
            else:
                print(ans)
                lives=lives+1
        elif a=='s':
            alp3=alp3+1
            if alp3<=1:
                ans[2] = 's'
                ans[5] = 's'
                ans[10] = 's'
                print(ans)
            else:
                print(ans)
                lives=lives+1
        elif a=='h':
            alp4=alp4+1
            if alp4<=1:
                ans[3] = 'h'
                print(ans)
            else:
                print(ans)
                lives=lives+1
        elif a=='t':
            alp5=alp5+1
            if alp5<=1:
                ans[6] = 't'
                print(ans)
            else:
                print(ans)
                lives=lives+1
        elif a=='c':
            alp6=alp6+1
            if alp6<=1:
                ans[8] = 'c'
                print(ans)
            else:
                print(ans)
                lives=lives+1
        elif a=='k':
            alp7=alp7+1
            if alp7<=1:
                ans[9]='k'
                print(ans)
            else:
                print(ans)
                lives=lives+1
        else:
            print(ans)
            lives=lives+1
        if lives == 1:
            print('______')
        elif lives == 2:
            print('+\n|\n|\n|\n|\n______')
        elif lives == 3:
            print('+--+--\n|\n|\n|\n|\n______')
        elif lives == 4:
            print('+--+--\n|  |\n|\n|\n|\n______')
        elif lives == 5:
            print('+--+--\n|  |\n|  o\n|\n|\n______')
        elif lives == 6:
            print('+--+--\n|  |\n|  o\n|  |\n|\n______')
        elif lives == 7:
            print('+--+--\n|  |\n| \\o\n|  |\n|\n______')
        elif lives == 8:
            print('+--+--\n|  |\n| \\o/\n|  |\n|\n______')
        elif lives == 9:
            print('+--+--\n|  |\n| \\o/\n|  |\n| /\n______')
        elif lives == 10:
            print('+--+--\n|  |\n| \\o/\n|  |\n| / \\\n______')
            print("Game Over")
            break