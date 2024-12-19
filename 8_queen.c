#include<stdio.h>
#include<stdbool.h>
int count_sol=0;
void place_queen(int* board,int n){//n == column
    for(int i=0;i<8;i++){// i == row
        bool conflict=false;
        for(int j=0;j<n;j++){//前n個column
            if(board[j]==i||board[j]-j==i-n||board[j]+j==i+n){
                conflict=true;
                break;
            }
        }
        if(!conflict){
            board[n]=i;
            if(n==7){
                printf("%d: ",++count_sol);
                for(int i=0;i<8;i++){
                    printf("%d",board[i]+1);
                }
                printf("\n");
            }
            else{
                conflict=false;
                place_queen(board,n+1);
            }
        }
    }
}
int main(){
    int arr[8]={-1,-1,-1,-1,-1,-1,-1,-1};
    place_queen(arr,0);
    return 0;
}