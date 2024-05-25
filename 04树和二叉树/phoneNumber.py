class Node:
    def __init__(self):
        self.children = [None] * 10
        self.visited = False


def main():
    test_cases = int(input())
    for _ in range(test_cases):
        num_strings = int(input())
        root = Node()
        l=[]
        for _ in range(num_strings):
            # 读取字符串
            s = input()
            l.append(s)
            l.sort(key=len)
            for s in l:

                    # 初始化当前节点为根节点
                current_node = root
                for char in s:
                    # 转换为整数索引（0-9）
                    index = int(char)
                    # 如果下一个节点已经存在且已经被访问过，则设置重复路径标志并跳出循环
                    if current_node.children[index] is not None and current_node.children[index].visited:
                        return True

                        # 如果下一个节点不存在，则创建新节点
                    if current_node.children[index] is None:
                        current_node.children[index] = Node()
                        # 移动到下一个节点
                    current_node = current_node.children[index]

                    # 如果遍历完整个字符串都没有找到重复路径，则标记当前叶子节点为已访问

                current_node.visited = True
                # 输出结果
        return False


if __name__ == "__main__":
    r=main()
    if r:
        print("NO")
    else:
        print("YES")