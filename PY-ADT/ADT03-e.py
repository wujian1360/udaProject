# 定义实现节点类
# 定义实现单链表类
# 初始化：最大限制，链表长度，根节点，尾节点
# 实现长度获取
# 添加元素
# 添加头部元素
# 实现可迭代
# 查找元素，根据值
# 删除元素，根据值
# 头部弹出，并返回值
# 清空链表，删除所有元素

# （可选）尾部弹出，并返回值 
# （可选）去掉重复元素  
# （可选）在第一次出现的某个值之前插入一个值 insert(value, newValue) 


class Node(object):
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

class Single_Linked_List(object):
    def __init__(self, maxsize=None):
        self.maxsize = maxsize
        node = Node()
        self.root = node
        self.tailnode = None
        
        self.length = 0

    def __len__(self):
        currNode = self.root.next
        count = 0
        while currNode is not None:
            count += 1
            currNode = currNode.next
        self.length = count
        return self.length

    def append(self, value):
        # 检查是否超过容量
        if self.maxsize is not None and self.length > self.maxsize:
            raise Exception("溢出！")
        node = Node(value)
        if self.tailnode is None:
            self.root.next = node
        else:
            self.tailnode.next = node
        self.tailnode = node
        self.length += 1

    def appendLeft(self, value):
        if self.maxsize is not None and self.length > self.maxsize:
            raise Exception("溢出！")
        node = Node(value)
        if self.tailnode is None:
            self.root.next = node
            self.tailnode = node # 空链表时，尾部==node
        else:
            node.next = self.root.next
            self.root.next = node
        self.length += 1

    def iterNode(self):
        currnode = self.root.next
        while currnode.next is not None:
            yield currnode
            currnode = currnode.next
        yield currnode

    def __iter__(self):
        for node in self.iterNode():
            yield node.value

    def find(self, value):
        index = 0
        for node in self.iterNode():
            if node.value == value:
                return index
            index += 1
        return -1


    def remove(self, value):
        currNode = self.root.next
        prevNode = None
        while currNode is not None:
            if currNode.value == value:
                if currNode == self.root.next:
                    self.root.next = currNode.next
                else:
                    prevNode.next = currNode.next
                self.tailnode = prevNode
                del currNode
                break
            else:
                prevNode = currNode
                currNode = currNode.next
        

    def popleft(self): 
        if self.root.next is None:
            raise Exception("列表已经为空！")
        headNode = self.root.next
        self.root.next = headNode.next
        value = headNode.value
        del headNode
        self.length -= 1
        return value


    def clear(self):
        for node in self.iterNode():
            del node
        self.root.next = None
        self.tailnode = None
        self.length = 0

 

        
def test_SLL():
    sll = Single_Linked_List()
    sll.append(100)
    sll.append(101)
    sll.append(102)
    assert len(sll) == 3
    # 正常头部添加
    sll.appendLeft(1)
    assert len(sll) == 4
    assert sll.root.next.value == 1
    assert list(sll) == [1, 100, 101, 102]
    assert sll.find(101) == 2
    sll.remove(1)

    assert sll.find(1) == -1

    assert list(sll) == [100, 101, 102]
    sll.remove(102)
    assert list(sll) == [100, 101]
    assert sll.tailnode.value == 101
    sll.append(99)
    assert sll.tailnode.value == 99

    sll.clear()
    assert len(sll) == 0
    assert sll.root.next == None
    assert sll.tailnode == None



    # 空链表头部添加
    sll2 = Single_Linked_List()
    sll2.appendLeft(100)
    assert sll2.tailnode.value == 100
    assert len(sll2) == 1
    sll2.append(101)
    assert list(sll2) == [100, 101]
    assert sll2.find(101) == 1

    