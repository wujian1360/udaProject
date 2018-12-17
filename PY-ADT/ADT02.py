'''
线性结构：
1、内存连续
2、下标访问
'''
# Array:同一类型
# from array import array

# arr = array('u','asdf')

# print(arr[1])

# help(array)

'''
# list：实现复杂度

1、新建空列表对象o-1

2、list[index]:实现复杂度o-1

3、append后一次新建四个空位，就是内存分配容量，
超出4个以后，重新分配四个resize，变成8个，实现复杂度o-1的

4、insert后是中间插入，需要重新内存分配，
capercity容量翻倍，开辟空间，实现复杂度o-n的

5、pop：默认pop最后一个元素，实现复杂度o-1的

6、实现复杂度o-n的，需要把后面的元素全部移动，

'''

# 实现一个固定长度的Array
class Array(object):
    def __init__(self, size=32):
        self.size = size
        self._items = [None] * size
    
    # 魔术方法，用[]访问元素，代理到_items[index]
    def __getitem__(self, index):
        return self._items[index]

    def __setitem__(self, index, value):
        self._items[index] = value

    def __len__(self):
        return len(self.size)
    
    def clear(self, value=None): 
        for i in range(len(self._items)):
            self._items[i] = value

    def __iter__(self):
        for item in self._items:
            yield item

def test_array():
    size = 10
    arr = Array(size)
    arr[0] = 1
    arr[2] = 2
    assert arr[0] == 1
    assert arr[2] == 2
    # assert 0 验证pytest

    arr.clear()
    assert arr[0] is None

