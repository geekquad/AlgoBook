/*
Stacks can be implemented using Queues.
A stack can be implemented using two queues. Let stack to be implemented be ‘s’ and queues used to implement be ‘q1’ and ‘q2’. Stack ‘s’ can be implemented in two ways:

Method 1 (By making push operation costly):
This method makes sure that newly entered element is always at the front of ‘q1’, so that pop operation just dequeues from ‘q1’. ‘q2’ is used to put every new element at front of ‘q1’.

push(s, x) operation’s step are described below:
1. Enqueue x to q2
2. One by one dequeue everything from q1 and enqueue to q2.
3. Swap the names of q1 and q2
pop(s) operation’s function are described below:
1. Dequeue an item from q1 and return it.


Method 2 (By making pop operation costly)
In push operation, the new element is always enqueued to q1. In pop() operation, if q2 is empty then all the elements except the last, are moved to q2. Finally the last element is dequeued from q1 and returned.

push(s, x) operation:
1. Enqueue x to q1 (assuming size of q1 is unlimited).
pop(s) operation:
1. One by one dequeue everything except the last element from q1 and enqueue to q2.
2. Dequeue the last item of q1, the dequeued item is result, store it.
3. Swap the names of q1 and q2
4. Return the item stored in step 2.
*/