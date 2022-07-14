A linkedin list is a linear collection of data elements
whose order is not given by their physical placement in memory. Instead, each element
points to the next. It is a data structure consisting of a collection of nodes which together
represent a sequence.

### Advantages:
1. Dynamic data structure: A linked list is a dynamic arrangement,
so it can grow and shrink at runtime by allocating and deallocating memory.
So there is no need to give the initial size of the linked list.

2. No memory wastage: In the Linked list, efficient memory utilization can be achieved
since the size of the linked list increase or decrease at run time so there is no memory
wastage and there is no need to pre-allocate the memory.

3.Implementation: Linear data structures like stack and queues are often easily implemented using a linked list.

4. Insertion and Deletion Operations: Insertion and deletion operations are quite easier in the linked list.
There is no need to shift elements after the insertion or deletion of an element only the address
present in the next pointer needs to be updated.

### Disadvantages:
1. Memory usage: More memory is required in the linked list as compared to an array.
Because in a linked list, a pointer is also required to store the address of the next element,
and it requires extra memory for itself.

2. Traversal: In a Linked list traversal is more time-consuming as compared to an array.
Direct access to an element is not possible in a linked list as in an array by index.
For example, for accessing a node at position n, one has to traverse all the nodes before it.

3. Reverse Traversing: In a singly linked list reverse traversing is not possible,
but in the case of a doubly-linked list, it can be possible as it contains a pointer to the previously
connected nodes with each node. For performing this extra memory is required for the back pointer hence,
there is a wastage of memory.

4. Random Access: Random access is not possible in a linked list due to its dynamic memory allocation.