# -*- coding:utf-8 -*-
# /usr/anaconda3/bin/python3
# @ DATE: 2020/3/20
# @ Author: TomTao
# @ PRODUCT_NAME: PyCharm

'''
这个题目是中等难度,23倒过来遍历是简单难度,为啥???
代码整体就改了一个insert变成append???
我佛了
'''


def levelOrderBottom(self, root: TreeNode) -> list:
    if root is None:
        return []
    # 初始化两个队列
    queue_root = [root]
    queue_val = []
    # 如果树结构还存在,那就继续走,
    while queue_root:
        n = len(queue_root)
        # 按照题意是列表嵌套列表,定义一个临时列表存树节点的值
        temp_li = []
        # 遍历这个队列,对树进行拆分查看
        for _ in range(n):
            # 获取节点
            tree = queue_root.pop(0)
            # 将当前节点的值放入临时列表
            temp_li.append(tree.val)
            # 遍历树的下一层
            # 先把同层左子树放入,后面放右子树,先进先出,从左往右
            if tree.left:
                queue_root.append(tree.left)
            if tree.right:
                queue_root.append(tree.right)
        # 遍历结束之后我们要把临时数组给插入到结果数组去
        # 第一次是根节点,第二次是下一层的数据,每次数据处理完先保存在了临时列表中
        queue_val.append(temp_li)
    return queue_val