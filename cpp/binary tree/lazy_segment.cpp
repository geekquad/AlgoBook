// Program to show segment tree to demonstrate lazy segment tree
#include <stdio.h> 
#include <math.h> 
#define MAX 1000 


// constant-sized arrays, we have done it here for simplicity. 
int tree[MAX] = {0}; // To store segment tree 
int lazy[MAX] = {0}; // To store pending updates 

/* si -> index of current node in segment tree 
	ss and se -> Starting and ending indexes of elements for 
				which current nodes stores sum. 
	us and ue -> starting and ending indexes of update query 
	diff -> which we need to add in the range us to ue */
void updateRangeUtil(int si, int ss, int se, int us, 
					int ue, int diff) 
{ 
	
	if (lazy[si] != 0) 
	{ 
		// Make pending updates using value stored in lazy 
		// nodes 
		tree[si] += (se-ss+1)*lazy[si]; 

		// checking if it is not leaf node because if 
		// it is leaf node then we cannot go further 
		if (ss != se) 
		{ 
			// We can postpone updating children we don't 
			// need their new values now. 
			// Since we are not yet updating children of si, 
			// we need to set lazy flags for the children 
			lazy[si*2 + 1] += lazy[si]; 
			lazy[si*2 + 2] += lazy[si]; 
		} 

		// Set the lazy value for current node as 0 as it 
		// has been updated 
		lazy[si] = 0; 
	} 

	// out of range 
	if (ss>se || ss>ue || se<us) 
		return ; 

	// Current segment is fully in range 
	if (ss>=us && se<=ue) 
	{ 
		// Add the difference to current node 
		tree[si] += (se-ss+1)*diff; 

		// same logic for checking leaf node or not 
		if (ss != se) 
		{ 
			// This is where we store values in lazy nodes, 
			// rather than updating the segment tree itelf 
			// Since we don't need these updated values now 
			// we postpone updates by storing values in lazy[] 
			lazy[si*2 + 1] += diff; 
			lazy[si*2 + 2] += diff; 
		} 
		return; 
	} 

	// If not completely in rang, but overlaps, recur for 
	// children, 
	int mid = (ss+se)/2; 
	updateRangeUtil(si*2+1, ss, mid, us, ue, diff); 
	updateRangeUtil(si*2+2, mid+1, se, us, ue, diff); 

	// And use the result of children calls to update this 
	// node 
	tree[si] = tree[si*2+1] + tree[si*2+2]; 
} 

// Function to update a range of values in segment 
// tree 
/* us and eu -> starting and ending indexes of update query 
	ue -> ending index of update query 
	diff -> which we need to add in the range us to ue */
void updateRange(int n, int us, int ue, int diff) 
{ 
updateRangeUtil(0, 0, n-1, us, ue, diff); 
} 


/* A recursive function to get the sum of values in given 
	range of the array. The following are parameters for 
	this function. 
	si --> Index of current node in the segment tree. 
		Initially 0 is passed as root is always at' 
		index 0 
	ss & se --> Starting and ending indexes of the 
				segment represented by current node, 
				i.e., tree[si] 
	qs & qe --> Starting and ending indexes of query 
				range */
int getSumUtil(int ss, int se, int qs, int qe, int si) 
{ 
	// If lazy flag is set for current node of segment tree, 
	// then there are some pending updates. So we need to 
	// make sure that the pending updates are done before 
	// processing the sub sum query 
	if (lazy[si] != 0) 
	{ 
		// Make pending updates to this node. Note that this 
		// node represents sum of elements in arr[ss..se] and 
		// all these elements must be increased by lazy[si] 
		tree[si] += (se-ss+1)*lazy[si]; 

		// checking if it is not leaf node because if 
		// it is leaf node then we cannot go further 
		if (ss != se) 
		{ 
			// Since we are not yet updating children os si, 
			// we need to set lazy values for the children 
			lazy[si*2+1] += lazy[si]; 
			lazy[si*2+2] += lazy[si]; 
		} 

		// unset the lazy value for current node as it has 
		// been updated 
		lazy[si] = 0; 
	} 

	// Out of range 
	if (ss>se || ss>qe || se<qs) 
		return 0; 

	// At this point we are sure that pending lazy updates 
	// are done for current node. So we can return value 
	// (same as it was for query in our previous post) 

	// If this segment lies in range 
	if (ss>=qs && se<=qe) 
		return tree[si]; 

	// If a part of this segment overlaps with the given 
	// range 
	int mid = (ss + se)/2; 
	return getSumUtil(ss, mid, qs, qe, 2*si+1) + 
		getSumUtil(mid+1, se, qs, qe, 2*si+2); 
} 

// Return sum of elements in range from index qs (query 
// start) to qe (query end). It mainly uses getSumUtil() 
int getSum(int n, int qs, int qe) 
{ 
	// Check for erroneous input values 
	if (qs < 0 || qe > n-1 || qs > qe) 
	{ 
		printf("Invalid Input"); 
		return -1; 
	} 

	return getSumUtil(0, n-1, qs, qe, 0); 
} 

// A recursive function that constructs Segment Tree for 
// array[ss..se]. si is index of current node in segment 
// tree st. 
void constructSTUtil(int arr[], int ss, int se, int si) 
{ 
	// out of range as ss can never be greater than se 
	if (ss > se) 
		return ; 

	// If there is one element in array, store it in 
	// current node of segment tree and return 
	if (ss == se) 
	{ 
		tree[si] = arr[ss]; 
		return; 
	} 

	// If there are more than one elements, then recur 
	// for left and right subtrees and store the sum 
	// of values in this node 
	int mid = (ss + se)/2; 
	constructSTUtil(arr, ss, mid, si*2+1); 
	constructSTUtil(arr, mid+1, se, si*2+2); 

	tree[si] = tree[si*2 + 1] + tree[si*2 + 2]; 
} 

/* Function to construct segment tree from given array. 
This function allocates memory for segment tree and 
calls constructSTUtil() to fill the allocated memory */
void constructST(int arr[], int n) 
{ 
	// Fill the allocated memory st 
	constructSTUtil(arr, 0, n-1, 0); 
} 


// Driver program to test above functions 
int main() 
{ 
	int arr[] = {1, 3, 5, 7, 9, 11}; 
	int n = sizeof(arr)/sizeof(arr[0]); 

	// Build segment tree from given array 
	constructST(arr, n); 

	// Print sum of values in array from index 1 to 3 
	printf("Sum of values in given range = %d\n", 
		getSum(n, 1, 3)); 

	// Add 10 to all nodes at indexes from 1 to 5. 
	updateRange(n, 1, 5, 10); 

	// Find sum after the value is updated 
	printf("Updated sum of values in given range = %d\n", 
			getSum( n, 1, 3)); 

	return 0; 
} 
