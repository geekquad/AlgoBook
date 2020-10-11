//this is a program to sort numbers using an efficient sorting algorithm heap sort;

#include <iostream>

using namespace std;

void print(int*arr,int n){//Function to print numbers in array;

for(int i=1;i<n;i++){
    cout<<arr[i]<<" ";
}

}


void maxheapify(int arr[],int i,int n){//function which Maintain/Restore the max-heap property.

    /*Max-heaps (largest element at root), have the
max-heap property:
– for all nodes i, excluding the root:
A[PARENT(i)] ≥ A[i]*/

int largest;
int l=2*i;
int r=2*i+1;

if(l<=n && arr[l]>arr[i]){   //if the left child is greater than its parent then largest index is the index of the left child.
    largest=l;
}
else
    largest=i;   //else largest is still the parent.

if(r<=n && arr[r]>arr[largest]){ //Comparing the largest with the right child,if the right child is greater than replacing largest with the index of right child.
    largest=r;
}

  if(largest!=i){
    int temp=arr[i];     //swapping the larger element with its smaller parent.
    arr[i]=arr[largest];
    arr[largest]=temp;
    maxheapify(arr,largest,n);   //Calling max heapify to maintain max heap property on remaining heap.
  }


}

void buildmaxheap(int arr[],int n){//function which Create a max-heap from an unordered array.


/*• Convert an array A[1 … n] into a max-heap (n = length[A])
• The elements in the subarray A[(n/2+1) .. n] are leaves
• Apply MAX-HEAPIFY on elements between 1 and (n/2)*/

for(int i=n/2;i>=1;i--){

maxheapify(arr,i,n);
}

}



int main()
{
int n;

cout<<"Enter the size of array"<<endl;

 cin>>n;

 int *arr=new int[n+1];//Dynamically creating an array of input size n;

cout<<"Enter the numbers"<<endl;

 for(int i=1;i<=n;i++){//Taking  input in array;
cin>>arr[i];

 }

buildmaxheap(arr,n);//creating max heap from unordered array.

for(int i=n;i>=2;i--){

// Swap the root (the maximum element) with the last element in the array
int temp=arr[1];

arr[1]=arr[i];
arr[i]=temp;

/*– “Discard” this last node by decreasing the heap size
– Call MAX-HEAPIFY on the new root
– Repeat this process until only one node remains */

maxheapify(arr,1,i-1);

}

print(arr,n+1);//printing the sorted array.

}
