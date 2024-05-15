import java.util.ArrayList;
import java.util.List;

/**
 * SingleLinkedListImpl
 */
public class SingleLinkedListImpl<T> implements LinkedList<T> {

    protected SingleLinkedListNode<T> head;
    
    public SingleLinkedListImpl(){
        this.head = new SingleLinkedListNode<T>();
    }

    @Override
	public boolean isEmpty() {
		return (this.head.isNIL());
	}

    @Override
	public int size() {
		int length = 0;
		if (!isEmpty()) {
			SingleLinkedListNode<T> node = this.head;

			while (node.getData() != null) {
				length++;
				node = node.getNext();
			}
		}
		return length;
	}

	@Override
	public T search(T element) {
		T result = null;
		if (element != null && !isEmpty()) {
			SingleLinkedListNode<T> x = this.head;
			while (!x.isNIL() && !x.getData().equals(element)) {
				x = x.getNext();
			}
			if (!x.isNIL()) {
				result = x.getData();
			}
		}
		return result;
	}

	@Override
	public void insert(T element) {
		SingleLinkedListNode<T> auxHead = this.head;
		if (element != null) {
			if (this.head.isNIL()) {
				SingleLinkedListNode<T> newHead = new SingleLinkedListNode(element, new SingleLinkedListNode<T>());
				this.setHead(newHead);
			} else {
				while (!auxHead.isNIL()) {
					auxHead = auxHead.getNext();
				}
				auxHead.setData(element);
				auxHead.setNext(new SingleLinkedListNode());
			}
		}
	}

	@Override
	public void remove(T element) {
		if (element != null && !isEmpty()) {
			if (this.head.getData().equals(element)) {
				this.head = this.head.getNext();
			} else {
				SingleLinkedListNode<T> aux = this.head;
				SingleLinkedListNode<T> previous = this.head;

				while (!aux.isNIL() && !aux.getData().equals(element)) {
					previous = aux;
					aux = aux.getNext();
				}

				if (!aux.isNIL()) {
					previous.setNext(aux.getNext());
				}
			}
		}
	}


	@Override
	public T[] toArray() {
		List<T> array = new ArrayList<>();
		SingleLinkedListNode<T> aux = this.head;

		while (!aux.isNIL()) {
			array.add(aux.getData());
			aux = aux.getNext();
		}
		return (T[]) array.toArray();
	}

	public SingleLinkedListNode<T> getHead() {
		return head;
	}

	public void setHead(SingleLinkedListNode<T> head) {
		this.head = head;
	}



}