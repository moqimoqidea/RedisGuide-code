# coding:utf-8

from redis import Redis
from transaction_fixed_length_queue import FixedLengthQueue

r = Redis()
r.flushdb()

max_length = 5
q = FixedLengthQueue(r, "fixed-length-queue", max_length)

#

assert q.len() == 0

assert q.enqueue("a")  # 进行 5 次有效推入
assert q.enqueue("b")
assert q.enqueue("c")
assert q.enqueue("d")
assert q.enqueue("e")

assert q.enqueue("f") is False  # 进行 2 次无效推入
assert q.enqueue("g") is False

assert q.len() == max_length

#

result = []
for i in range(max_length):
    result.append(q.dequeue())

assert result == ["a", "b", "c", "d", "e"]

assert q.len() == 0


#

r.flushdb()

print("all tests passed!")
