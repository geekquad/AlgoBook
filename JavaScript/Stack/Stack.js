
    // Time Complexity
    // ---------------
    // Push        O(1)
    // Pop         O(1)
    // is_empty    O(1)
    // is_full     O(1)
    // peek        O(1)
    // size        O(1)




class Stack {
    constructor(capacity = 5) {
        this.items = [];
        this.capacity = capacity;
    }

    is_empty(){
        return this.items.length <= 0;
     }

     is_full(){
        return this.items.length == 5;
     }
    
    
    Push(element) {
        if (this.is_full()) console.log("Stack Overflow!");
        else this.items.push(element);
    }
    
    
    Pop() {
        if (this.is_empty()) console.log("Stack Underflow!")
        else {return this.items.pop();}
        
    }
    
    peek() {
        return this.items[this.items.length - 1];
    }
    
    

    size(){
        return this.items.length;
    }
 
}

//main
let stack = new Stack();
stack.Pop()
stack.Push(10);
stack.Push(20);
stack.Push(30);
stack.Push(40);
stack.Push(50);
stack.Push(60);

console.log(stack.size());
stack.Pop()
stack.Pop()
console.log(stack.peek())

