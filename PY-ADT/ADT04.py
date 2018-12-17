
# 实现 双端循环列表

# 定义并实现节点类
# 定义并实现双向循环链表
# 初始化：最大容量，长度，根节点定义
# 实现获取长度
# 获取头节点
# 获取尾节点
# 添加值到尾部
# 添加值到头部
# 删除某节点，并返回它
# 遍历节点
# 实现可迭代
# 反向遍历

# （可选）去掉重复元素  
# （可选）LRU Cache 会用到双端循环链表

# 如何将一个可迭代对象 转换成 双向循环链表？？

# 定义节点类
class Node(object):
    def __init__(self, value=None, prev=None, next=None):
        self.value, self.prev, self.next = value, prev, next

# 定义双向循环链表
class Circle_Double_Linked_List(object):
    # 定义长度
    # 定义一个自成闭环的节点
    # 将根节点指向它
    def __init__(self, maxsize=None):
        self.maxsize = maxsize # 为空代表无限容量
        node = Node()
        node.next = node
        node.prev = node
        self.root = node
        self.length = 0

    # 长度
    def __len__(self):
        return self.length

    # 头结点
    def headNode(self):
        return self.root.next
    # 尾节点
    def tailNode(self):
        return self.root.prev

    # 添加节点到尾部
    def append(self, value):
        # 判断范围是否为空，同时有没有超出限制范围，
        # 如果范围为空，代表无限链表
        if self.maxsize is not None and len(self) > self.maxsize:
            raise Exception("I am Full")

        # 创建node对象，作为当前节点
        # 获取尾节点
        # 尾节点和当前节点，互指
        # 根节点和当前节点，互指
        node = Node(value)
        tailNode = self.tailNode()
        tailNode.next = node
        node.prev = tailNode
        node.next = self.root
        self.root.prev = node

        self.length += 1

    # 添加节点到头部
    def appendLeft(self, value):
        # 同上
        if self.maxsize is not None and len(self) > self.maxsize:
            raise Exception("I am Full")
        # 创建node，获取头节点，与头节点互指，与根节点互指
        node = Node(value)

        # 判断一下链表是否为空？？
        # 上面append为何不判断？
        if self.root.next is self.root:
            node.prev = self.root
            node.next = self.root
            self.root.next = node
            self.root.prev = node
        else:
            node.prev = self.root
            headNode = self.headNode()
            node.next = headNode
            headNode.prev = node
            self.root.next = node

        self.length += 1

    # 删除节点o(1)，注意这里参数是node，不是value
    def remove(self, node):
        if node is self.root:
            return -1
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
        self.length -= 1
        return node # 返回还是直接del

    # 遍历每个节点
    def iterNode(self):
        # 先判断链表是否为空，为空就return
        if self.root.next is self.root:
            return
        # 每次判断当前节点的下一个节点是不是根节点
        # 注意最后要yeild最后一个当前节点
        currNode = self.root.next
        while currNode.next is not self.root:
            yield currNode
            currNode = currNode.next
        yield currNode

    # 遍历每个节点的velue
    def __iter__(self):
        for node in self.iterNode():
            yield node.value

    # 反向遍历
    def iterNodeReverse(self):
        if self.root.prev is self.root:
            return
        currNode = self.root.prev
        while currNode.prev is not self.root:
            yield currNode
            currNode = currNode.prev
        yield currNode

# 单测
def test_Circle_Double_Linked_List():
    dll = Circle_Double_Linked_List()

    assert dll.length == 0
    dll.append(1)
    dll.append(11)
    dll.append(100)
    assert list(dll) == [1, 11, 100]

    headNode = dll.headNode()
    tailNode = dll.tailNode()
    assert headNode.value == 1
    assert tailNode.value == 100
    assert len(dll) == 3

    dll.appendLeft(0)
    dll.appendLeft(-11)
    dll.appendLeft(-101)
    dll.append(100)
    assert list(dll) == [-101, -11, 0, 1, 11, 100,100]

    dll.remove(dll.tailNode()) # o(1)的remove操作
    dll.remove(dll.tailNode())
    dll.remove(dll.headNode())
    assert list(dll) == [-11, 0, 1, 11]
    assert dll.length == 4
    assert len(dll) == 4

    assert [node.value for node in dll.iterNode()] == [-11, 0, 1, 11]
    assert [node.value for node in dll.iterNodeReverse()] == [11, 1, 0, -11]
    
    dll.appendLeft("ok")
    assert [node.value for node in dll.iterNode()] == ["ok", -11, 0, 1, 11]



