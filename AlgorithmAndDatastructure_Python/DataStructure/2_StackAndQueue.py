
print("####################### Stack : LIFO #########################")

stack = []
stack.append(1)
stack.append(2)
stack.append(3)
stack.append(4)

print("stack pop1:", stack.pop())
print("stack pop2:", stack.pop())
print("stack pop3:", stack.pop())
print("stack pop4:", stack.pop())

print("####################### Queue : FIFO ########################")

queue = []
queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)

nums = len(queue)
for i in range(0, nums):
    print(f"queue pop{i+1}:", queue.pop(0))


