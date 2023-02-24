from Stack import Stack

def test_stack_pop():
  obj=Stack()
  obj.push(10)
  obj.push(20)
  obj.push(30)
  assert obj.peek()==30