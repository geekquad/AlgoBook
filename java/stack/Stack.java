/**
 * The Stack interface represents a last-in-first-out (LIFO) stack of elements.
 */
public interface Stack<E> {

    /**
     * Returns the number of elements in the stack.
     *
     * Complexity: O(1)
     *
     * @return the number of elements in the stack
     */
    int size();

    /**
     * Returns true if the stack is empty, false otherwise.
     *
     * Complexity: O(1)
     *
     * @return true if the stack is empty, false otherwise
     */
    boolean isEmpty();

    /**
     * Pushes an element onto the top of the stack.
     *
     * Complexity: O(1)
     *
     * @param element the element to be pushed onto the stack
     */
    void push(E element);

    /**
     * Removes and returns the element at the top of the stack.
     *
     * Complexity: O(1)
     *
     * @return the element at the top of the stack
     * @throws EmptyStackException if the stack is empty
     */
    E pop();

    /**
     * Returns the element at the top of the stack without removing it.
     *
     * Complexity: O(1)
     *
     * @return the element at the top of the stack
     * @throws EmptyStackException if the stack is empty
     */
    E peek();
}
