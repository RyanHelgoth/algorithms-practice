/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** transpose(int** matrix, int matrixSize, int* matrixColSize, int* returnSize, int** returnColumnSizes){
    *returnSize = *matrixColSize; 
    *returnColumnSizes = malloc((*returnSize)*sizeof(int)); //number of rows in transposed matrix * siz of int
    
    int** transposed = malloc((*returnSize) * sizeof(int *)); //number of rows in transposed matrix * size of int pointer
    for (int i = 0; i < *returnSize; i++) {
        transposed[i] = malloc(matrixSize * sizeof(int)); //for each row in the transposed matrix allocate sapce to fit a column of the original matrix
        (*returnColumnSizes)[i] = matrixSize; //set each column size of the tranposed matrix to the number of rows in the original matrix.
    }
    
    for (int i = 0; i < matrixSize; i++) {
        for (int j = 0; j < *matrixColSize; j++) {
            transposed[j][i] = matrix[i][j];
        } 
    }
    
    return transposed;     
}