import sys


class BTree:
    def __init__(self, root, left, right):
        self.root, self.left, self.right = root, left, right

    def __init__(self, root):
        self.root, self.left, self.right = root, None, None

    @staticmethod
    def makeBTree(pre, mid):
        if not pre:
            return None
        tree = BTree(pre[0])
        leftMid, rightMid = mid.split(pre[0])
        leftPre = ''.join(char for char in pre if char in leftMid)
        rightPre = ''.join(char for char in pre if char in rightMid)
        # print pre[0], leftPre, rightPre
        if leftMid:
            tree.left = BTree.makeBTree(leftPre, leftMid)
        if rightMid:
            tree.right = BTree.makeBTree(rightPre, rightMid)
        return tree

    def postVist(self):
        if self.left:
            self.left.postVist()
        if self.right:
            self.right.postVist()
        sys.stdout.write(self.root)


while True:
    pre = raw_input().strip()
    mid = raw_input().strip()
    tree = BTree.makeBTree(pre, mid)
    tree.postVist()
    print


