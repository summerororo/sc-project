"""
File: add2.py
Name: Summer黃兆嘉
------------------------
TODO:
"""

import sys


class ListNode:
    def __init__(self, data=0, pointer=None):
        self.val = data
        self.next = pointer


def add_2_numbers(l1: ListNode, l2: ListNode) -> ListNode:
    # ########### l1 ###########
    # cur = l1
    # l1_str = ''
    # l1_num = ''
    # while cur.next is not None:
    #     l1_str += str(cur.val)
    #     cur = cur.next
    # l1_str += str(cur.val)
    # # reverse
    # for i in range(len(l1_str)):
    #     l1_num += l1_str[-1-i]
    # l1_num = int(l1_num)
    # ########### l2 ############
    # cur = l2
    # l2_str = ''
    # l2_num = ''
    # while cur.next is not None:
    #     l2_str += str(cur.val)
    #     cur = cur.next
    # l2_str += str(cur.val)
    # # reverse
    # for i in range(len(l2_str)):
    #     l2_num += l2_str[-1 - i]
    # l2_num = int(l2_num)
    # ######### total ###########
    # total = str(l1_num + l2_num)
    # # ans
    # if len(total) == 1:
    #     ans = ListNode(int(total[-1]), None)
    # else:
    #     ans = ListNode(int(total[-1]), None)
    #     cur = ans
    #     for i in range(len(total)-1):
    #         cur.next = ListNode(int(total[-2-i]))
    #         cur = cur.next
    # return ans

    # solution2
    dummy = ListNode(data=0, pointer=None)
    cur = dummy
    carry = 0
    while l1 is not None or l2 is not None or carry != 0:
        val1 = l1.val if l1 is not None else 0
        val2 = l2.val if l2 is not None else 0
        val = val1 + val2 + carry
        carry = val//10
        val = val % 10

        cur.next = ListNode(data=val)  # 做新的linklist

        l1 = l1.next if l1 is not None else None
        l2 = l2.next if l2 is not None else None
        cur = cur.next
    return dummy.next

####### DO NOT EDIT CODE BELOW THIS LINE ########


def traversal(head):
    """
    :param head: ListNode, the first node to a linked list
    -------------------------------------------
    This function prints out the linked list starting with head
    """
    cur = head
    while cur.next is not None:
        print(cur.val, end='->')
        cur = cur.next
    print(cur.val)


def main():
    args = sys.argv[1:]
    if not args:
        print('Error: Please type"python3 add2.py test1"')
    else:
        if args[0] == 'test1':
            l1 = ListNode(2, None)
            l1.next = ListNode(4, None)
            l1.next.next = ListNode(3, None)
            l2 = ListNode(5, None)
            l2.next = ListNode(6, None)
            l2.next.next = ListNode(4, None)
            ans = add_2_numbers(l1, l2)
            print('---------test1---------')
            print('l1: ', end='')
            traversal(l1)
            print('l2: ', end='')
            traversal(l2)
            print('ans: ', end='')
            traversal(ans)
            print('-----------------------')
        elif args[0] == 'test2':
            l1 = ListNode(9, None)
            l1.next = ListNode(9, None)
            l1.next.next = ListNode(9, None)
            l1.next.next.next = ListNode(9, None)
            l1.next.next.next.next = ListNode(9, None)
            l1.next.next.next.next.next = ListNode(9, None)
            l1.next.next.next.next.next.next = ListNode(9, None)
            l2 = ListNode(9, None)
            l2.next = ListNode(9, None)
            l2.next.next = ListNode(9, None)
            l2.next.next.next = ListNode(9, None)
            ans = add_2_numbers(l1, l2)
            print('---------test2---------')
            print('l1: ', end='')
            traversal(l1)
            print('l2: ', end='')
            traversal(l2)
            print('ans: ', end='')
            traversal(ans)
            print('-----------------------')
        elif args[0] == 'test3':
            l1 = ListNode(0, None)
            l2 = ListNode(0, None)
            ans = add_2_numbers(l1, l2)
            print('---------test3---------')
            print('l1: ', end='')
            traversal(l1)
            print('l2: ', end='')
            traversal(l2)
            print('ans: ', end='')
            traversal(ans)
            print('-----------------------')
        else:
            print('Error: Please type"python3 add2.py test1"')


if __name__ == '__main__':
    main()
