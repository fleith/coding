''' Implement LRU Cache
    @see @functools.lru_cache(maxsize=128, typed=False)
    @see OrderedDict
    and implement Double-linked list and use a Dict
'''

#
# # LRUCache .....
#
# # Doubly Linked List.
#
# class Node:
#     key
#     value
#     prev_node
#     next_node
#
#
# # 1 -> 3 -> 5 -> 7 -> 9(tail)
# #   1 <- 3 <- 5 <- 7 <- 9(tail)
#
# class DoublyLinkedList:
#     def add_to_tail(self, node):
#         pass
#
#     def remove_from_head(self, node):
#
#     def move_node_tail(self, node):
#         before = node.prev_node
#         after = node.next_node
#         before.next_node = after
#         after.prev_node = before
#         self._tail.next_node = node
#         node.prev_node = self._tail
#         self._tail = node
#
#     def tail(self):
#         return self._tail
#
#     def head(self)
#         return self._head
#
#
# class LRUCache:
#     def __init__(self, capacity):
#         self._capacity = capacity
#         self._cache = dict()
#         self._dl = DoublyLinkedList()
#
#     def get(key):
#         if key in self._cache:
#             self._dl.move_node_tail(self._cache[key])
#             return self._cache[key].value
#         return None
#
#     def put(key, value):
#         if key in self._cache:
#             self._dl.move_node_tail(self._cache[key])
#             self._cache[key].value = value
#             return
#
#         if len(self._cache) >= self._capacity:
#             node = self._dl.get_head()
#             del self._cache[node.key]
#             self._dl.remove_from_head()
#
#         new_node = Node(key, value)
#         self._dl.add_to_tail(new_node)
#         self._cache[new_node.key] = new_node
#
#
# # My Application
# # show student record
# c = LRUCache()
# id = 10
# studen
# t = c.get(id)
#
# st = Student("name,", "agE")
# c.put(20, st)

