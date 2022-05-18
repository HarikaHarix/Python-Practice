f=open('poem.txt')
t=f.read()

if 'twinkle' in t:
    print("twinkle is present in the poem")
else:
    print("twinkle is not present in the poem")

f.close()