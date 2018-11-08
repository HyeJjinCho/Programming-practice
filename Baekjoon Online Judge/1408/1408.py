h1, m1, s1=map(int,input().split(':'))
h2, m2, s2=map(int,input().split(':'))

h2+=23-h1
m2+=59-m1
s2+=60-s1
m2+=s2//60
h2+=m2//60

print('%02d:%02d:%02d' %(h2%24, m2%60, s2%60))
