
try:
    f = open('testfile.txt')
    # var = bar_var

except FileNotFoundError as e:
    print(e)
except Exception as e:
    print('Sorry, something went wrong')
else:
    print(f.read())
    f.close()
