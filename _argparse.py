import argparse

parser = argparse.ArgumentParser(description='Testning av argparse')

group1 = parser.add_mutually_exclusive_group(required=True)

parser.add_argument('-a', default=1, type=int, help='This is variable a')
parser.add_argument('-name', required=True, default=None, type=str, help='Your name')
parser.add_argument('-education', required=True, choices=['highschool', 'college', 'other'], type=str, help='Your name')
group1.add_argument('-b', action='store_true', help='this is b')
group1.add_argument('-c', action='store_const', const=10, help='this is b')

args = parser.parse_args()
a = args.a
name = args.name
edu = args.education
b = args.b
c = args.c

# print(f'YOu entered a = {a}, name = {name}, education = {edu}')

print(b)
print(c)
