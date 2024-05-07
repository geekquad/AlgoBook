import java.util.EmptyStackException;

/**
 * An array implementation of the Stack interface.
 */
public class ArrayStack<T> implements Stack<T> {

    private static final int DEFAULT_CAPACITY = 10;

    private T[] array;
    private int top;

    /**
     * Constructs an empty stack with the default capacity.
     */
    public ArrayStack() {
        this(DEFAULT_CAPACITY);
    }

    /**
     * Constructs an empty stack with the specified capacity.
     *
     * @param capacity the initial capacity of the stack
     */
    public ArrayStack(int capacity) {
        array = (T[]) new Object[capacity];
        top = -1;
    }

    /**
     * {@inheritDoc}
     */
    @Override
    public void push(T element) {
        if (top == array.length - 1) {
            expandCapacity();
        }
        top++;
        array[top] = element;
    }

    /**
     * {@inheritDoc}
     */
    @Override
    public T pop() {
        if (isEmpty()) {
            throw new EmptyStackException();
        }
        T element = array[top];
        array[top] = null;
        top--;
        return element;
    }

    /**
     * {@inheritDoc}
     */
    @Override
    public T peek() {
        if (isEmpty()) {
            throw new EmptyStackException();
        }
        return array[top];
    }

    /**
     * {@inheritDoc}
     */
    @Override
    public boolean isEmpty() {
        return top == -1;
    }

    /**
     * {@inheritDoc}
     */
    @Override
    public int size() {
        return top + 1;
    }

    private void expandCapacity() {
        T[] newArray = (T[]) new Object[array.length * 2];
        System.arraycopy(array, 0, newArray, 0, array.length);
        array = newArray;
    }
}
