#include <stdio.h>
#include <stdlib.h>
/*************  ✨ Codeium Command 🌟  *************/
#include <assert.h>
int main(){
    long long int n,m;
    printf("輸入n和m\n");
    scanf("%lld %lld",&n,&m);
    long long int* arr=malloc(m*sizeof(long long int));
    assert(arr!=NULL);
    for(int i=0;i<m;i++){
        printf("輸入第%d個數字\n",i+1);
        scanf("%lld",&arr[i]);
    }
    long long int sum=0;
    for(long long int i = 1; i < n; i++){
        for(long long int j = 0; j < m; j++){
            if(i%arr[j]==0){
                sum+=1;
                break;
            }
        }
    }
    printf("%lld",sum);
    free(arr);
}
