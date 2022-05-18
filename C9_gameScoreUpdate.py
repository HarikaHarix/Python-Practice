# def game():
#     return 64

# score=game()

# with open ("hiScore.txt") as f:
#     hiscore=int(f.read())

# if hiscore<score:
#     with open('hiScore.txt','w') as f:
#         f.write(str(score))



def game():
    return 644

score=game()

with open ("hiScore.txt") as f:
    hiScoreStr=f.read()

if hiScoreStr==" ":
    with open('hiScore.txt','w') as f:
        f.write(str(score))

elif int(hiScoreStr)<score :
    with open('hiScore.txt','w') as f:
        f.write(str(score))
