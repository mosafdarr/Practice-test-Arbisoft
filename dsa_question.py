import sys

def dequeue_PQ(PQ):
        try:
            max_val = 0
            for i in range(len(PQ)):
                if PQ[i] > PQ[max_val]:
                    max_val = i
            item = PQ[max_val]
            del PQ[max_val]
            return item
        
        except IndexError:
            print()
            exit()

def read_file(file_path):
    input_file = []

    try: 
        with open(file_path, "r") as file:
            next(file)

            for line in file:
                operation, element = line.split(" ")
                input_file.append((operation, int(element)))

            return input_file
            
    except FileNotFoundError as err:
        print("File Not Found", err)

def misterious_DS(file_path):
    stack = []
    queue = []
    pq = []

    stack_flag = False
    queue_flag = False
    pq_flag = False
    
    count_of_flags = 0
    count_of_push = 0
    count_of_pop = 0

    input_file = read_file(file_path)

    for operation, element in input_file:
        if operation.lower() == "push":
            stack.append(element)
            pq.append(element)
            queue.append(element)

            count_of_push += 1
        
        if operation.lower() == "pop":
            if stack.pop() != element:
                stack.append(element)
            
            if queue.pop(0) != element:
                queue.append(element)
            
            if dequeue_PQ(pq) != element:
                pq.append(element)

            count_of_pop += 1

    remaining_element_count = count_of_push - count_of_pop
    
    if len(stack) == remaining_element_count:
        stack_flag = True
        count_of_flags += 1

    if len(queue) == remaining_element_count:
        queue_flag = True
        count_of_flags += 1

    if len(pq) == remaining_element_count:
        pq_flag = True
        count_of_flags += 1

    if count_of_flags > 1:
        return "NOT SURE"
    
    elif count_of_flags == 0:
        return "IMPOSSIBLE"
    
    else:
        if stack_flag:
            return "LIFO"
        
        if queue_flag: 
            return "FIFO"
        
        if pq_flag:
            return "PQ"
        

file_path = sys.argv[1]
result = misterious_DS(file_path)
print(result)
