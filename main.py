from stack import Stack

stack = Stack()

print("Stack using Linked List")
print("-----------------------")

# Add elements
stack.put(10)
stack.put(20)
stack.put(30)

print("\nTop element:", stack.peek())
print("Size:", stack.size)

# Remove first element
removed = stack.remove()

print("\nRemoved:", removed)
print("Top element:", stack.peek())
print("Size:", stack.size)

# Remove second element
removed = stack.remove()

print("\nRemoved:", removed)
print("Top element:", stack.peek())
print("Size:", stack.size)

# Add another element
stack.put(40)

print("\nAdded: 40")
print("Top element:", stack.peek())
print("Size:", stack.size)