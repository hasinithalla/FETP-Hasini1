#code1
s = "formulaqsolutions"
n = int(input())

if n % 2 == 0:
    n = n + 1

s = (s * ((n + len(s) - 1) // len(s)))[:n]

for a1 in range(1, (n + 1) // 2 + 1):
    for a2 in range((n + 1) // 2 - a1):
        print(" ", end="")
    for a3 in range(a1 * 2 - 1):
        print(s[a3 + a1 - 1], end="")
    print()

for a1 in range((n + 1) // 2 - 1, 0, -1):
    for a2 in range((n + 1) // 2 - a1):
        print(" ", end="")
    for a3 in range(a1 * 2 - 1):
        print(s[a3 + (n + 1) // 2 - a1 - 1], end="")
    print()
"""Output                                                                                                                                                                                            
        f
       orm
      rmula
     mulaqso
    ulaqsolut
   laqsolution
  aqsolutions
---------------------------------------------------------------------------
IndexError                                Traceback (most recent call last)
<ipython-input-71-75e2e77ba6ba> in <cell line: 9>()
     11         print(" ", end="")
     12     for a3 in range(a1 * 2 - 1):
---> 13         print(s[a3 + a1 - 1], end="")
     14     print()
     15 

IndexError: string index out of range"""
#code2
s = "formulaqsolutions"
n = int(input())
if n%2==0:
  n=n+1


s = (s * ((n + len(s) - 1) // len(s)))[:n]

for a1 in range(1, (n + 1) // 2 + 1): 
    for a2 in range((n + 1) // 2 - a1-1):
        print(" ", end="")
    for a3 in range((a1 * 2) - 1):
        print(s[(a3 + a1) % len(s)], end="")
    print()

for a1 in range((n + 1) // 2 - 1, 0, -1):
    for a2 in range((n + 1) // 2 - a1):
        print(" ", end="")
    for a3 in range((a1 * 2) - 1):
        print(s[(a3 + a1) % len(s)], end="")
    print()
"""Output

         o
        rmu
       mulaq
      ulaqsol
     laqsoluti
    aqsolutions
   qsolutionsfor
  solutionsformfo
 olutionsformformu
lutionsformformulaq
utionsformformulaqsol
 lutionsformformulaq
  olutionsformformu
   solutionsformfo
    qsolutionsfor
     aqsolutions
      laqsoluti
       ulaqsol
        mulaq
         rmu
          o"""
