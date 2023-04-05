Alignment matrix:

def alignment_matrix(string1, string2, match_score=1, mismatch_score=-1, gap_penalty=-1):

    m = len(string1)
    n = len(string2)
    alignment_matrix = [[0 for j in range(n+1)] for i in range(m+1)]
    
    
    for i in range(1, m+1):
        alignment_matrix[i][0] = i * gap_penalty
    for j in range(1, n+1):
        alignment_matrix[0][j] = j * gap_penalty
    
    
    for i in range(1, m+1):
        for j in range(1, n+1):
            if string1[i-1] == string2[j-1]:
                match = match_score
            else:
                match = mismatch_score
            alignment_matrix[i][j] = max(alignment_matrix[i-1][j-1] + match,
                                          alignment_matrix[i-1][j] + gap_penalty,
                                          alignment_matrix[i][j-1] + gap_penalty)
    
    return alignment_matrix
