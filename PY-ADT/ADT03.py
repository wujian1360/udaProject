'''
链式结构
1、内存不连续
2、不能通过下标访问
3、追加元素很方便
4、遍历操作和查找操作比较复杂


单链表
1、通过指针的方式首尾相连
2、根节点，入口，用来遍历，首节点，尾节点
3、node：包括value，和指针next，指向下一个元素
4、可以定义一个class来体现node对象
5、实现单链表结构

单链表类的属性和方法
1、数据data：root、lenth、

2、method：
init、append、append_left、append_right、
iter_node、remove、find、pop_left(right)、
clear
'''

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
    # 定义节点类
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next
        
class linkedlist(object):
    def __init__(self, maxsize=None):
        self.maxsize = maxsize
        self.root = Node()
        self.tailnode = None

        self.length = 0
    
    def __len__(self):
        # 获取长度
        currNode = self.root.next
        count = 0
        while currNode is not None:
            count += 1
            currNode = currNode.next
        self.length = count
        return self.length
    
    def append(self, value):
        # 从尾部添加元素
        # 判断容量不为空,同时没有超过最大容量，否则抛出异常
        if self.maxsize is not None and len(self) > self.maxsize:
            raise Exception('is Full')
        # 创建一个新节点
        node = Node(value)
        tailnode = self.tailnode
        # 判断tailnode是否为空，是代表链表只有根节点，将根节点的next指向新节点
        # 否则将尾部节点的next指向新节点
        if tailnode is None:
            self.root.next = node
        else:
            tailnode.next = node

        self.tailnode = node
        self.length += 1

    def appendleft(self, value):
        # 从头部添加元素
        headnode = self.root.next
        node = Node(value)
        self.root.next = node
        node.next = headnode
        self.length += 1

    def iter_node(self):
        # 迭代节点
        curnode = self.root.next
        while curnode is not self.tailnode:
            yield curnode
            curnode = curnode.next
        yield curnode

    def __iter__(self):
        # self可迭代
        for node in self.iter_node():
            yield node.value



 
    def find(self, value):
        index = 0
        for node in self.iter_node():
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
        
        

    def popleft(self): # o(n) 复杂度
        # 从左边弹出一个元素，并返回它
        if self.root.next is None: # 判断是否为空
            raise Exception('pop from empty linkedList')

        headnode = self.root.next
        self.root.next = headnode.next
        self.length -= 1
        value = headnode.value
        del headnode
        return value

    def clear(self):
        for node in self.iter_node():
            del node
        self.root.next = None
        self.length = 0



# 单测
def test_linked_list():
    ll = linkedlist()
    ll.append(0)
    ll.append(1)
    ll.append(2)

    assert len(ll) == 3
    assert ll.find(2) == 2
    assert ll.find(3) == -1

    ll.remove(0)
    assert len(ll) == 2
    # assert ll.find(0) == -1

    assert list(ll) == [1,2]

    ll.appendleft(100)
    assert list(ll) == [100,1,2]
    assert len(ll) == 3
    
    headvalue = ll.popleft()
    assert headvalue == 100
    assert list(ll) == [1,2]
    assert len(ll) == 2
    # ll.remove(2)
    # assert list(ll) == [1]

    ll.clear()
    assert len(ll) == 0


