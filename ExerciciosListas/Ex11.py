"""Altere o programa anterior, intercalando 3 vetores de 10 elementos cada."""
vetor1 = [1,4,7,10,13,16,19,22,25,28]
vetor2 = [2,5,8,11,14,17,20,23,26,29]
vetor3 = [3,6,9,12,15,18,21,24,27,30]
vetor = []

for a,b,c in zip(vetor1, vetor2, vetor3):
    vetor.append(a)
    vetor.append(b)
    vetor.append(c)
    
print(vetor)