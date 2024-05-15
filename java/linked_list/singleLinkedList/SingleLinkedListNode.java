

public class SingleLinkedListNode<T> {
    protected T data;
    protected SingleLinkedListNode<T> next;

    public SingleLinkedListNode(){

    }

    public SingleLinkedListNode(T data, SingleLinkedListNode<T> next){
        this.data = data;
        this.next = next;
    }   

    public T getData(){
        return this.data;
    }

    public SingleLinkedListNode<T> getNext(){
        return this.next;
    }

    public boolean isNIL() {
		return (this.data == null);
	}

    public void setData(T data) {
		this.data = data;
	}

	public void setNext(SingleLinkedListNode<T> next) {
		this.next = next;
	}

    @Override
    public int hashCode() {
        final int prime = 31;
        int result = 1;
        result = prime * result + ((data == null) ? 0 : data.hashCode());
        return result;
    }

    @Override
    public boolean equals(Object obj) {
        if (this == obj)
            return true;
        if (obj == null)
            return false;
        if (getClass() != obj.getClass())
            return false;
        SingleLinkedListNode<T> other = (SingleLinkedListNode) obj;
        if (data == null) {
            if (other.data != null)
                return false;
        } else if (!data.equals(other.data))
            return false;
        return true;
    }

    @Override
    public String toString() {
        String resp = null;
		if (!isNIL()) {
			resp = this.data.toString();
		} else {
			resp = "NIL";
		}
		return resp;
    }

    

}
