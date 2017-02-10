void reverseString(char stringVar[]){
   
    int length = 0;
    while(stringVar[length] != '\0'){
        length++;
    }
    
    int headPtr = 0, rearPtr = length-1;
    while(headPtr < rearPtr){
        char swapVar;
        swapVar = stringVar[headPtr];
        stringVar[headPtr] = stringVar[rearPtr];
        stringVar[rearPtr] = swapVar;
        headPtr++;
        rearPtr--;
    }
}
