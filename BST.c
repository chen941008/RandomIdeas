#include <stdio.h>
#include <stdlib.h>
typedef struct treenode{
    int data;
    struct treenode* left;
    struct treenode* right;
}treenode_t;
treenode_t *insert_tree(treenode_t *root,int data_t){
    // If the tree is empty, create a new node with the given data
    if(root==NULL){
        treenode_t* current=malloc(sizeof(treenode_t));
        current->data=data_t;
        current->right=current->left=NULL;
        return current;
    }
    // If the given data is less than the current node, insert it into the left subtree
    else if(data_t<root->data){
        root->left=insert_tree(root->left,data_t);
    }
    // If the given data is greater than the current node, insert it into the right subtree
    else{
        root->right=insert_tree(root->right,data_t);
    }
    // Return the modified root node
    return root;
}
void print_tree(treenode_t *root){
    if(root==NULL){
        return;
    }
    print_tree(root->left);
    printf("%d ",root->data);
    print_tree(root->right);
}
int main(){
    int n;
    treenode_t *root = NULL;
    scanf("%d",&n);
    int arr[n];
    for(int i=0;i<n;i++){
        scanf("%d",&arr[i]);
        root=insert_tree(root,arr[i]);
    }
    print_tree(root);
}