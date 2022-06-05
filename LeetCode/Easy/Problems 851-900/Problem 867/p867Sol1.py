class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        transpose = []
        firstPass = True
            
        for row in matrix:
            for i in range(len(row)):
                if firstPass:
                    transpose.append([])
                transpose[i].append(row[i])
            firstPass = False
        
        return transpose