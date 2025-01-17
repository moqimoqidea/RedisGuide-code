# coding:utf-8

VALUE_OF_LOCK = "this-key-is-an-acquired-lock"


class TimingLock:
    def __init__(self, client, key):
        self.client = client
        self.key = key

    def acquire(self, timeout):
        """
        尝试获取一个带有最大使用时限的锁，
        成功时返回 True ，失败时返回 False 。
        """
        result = self.client.set(self.key, VALUE_OF_LOCK, nx=True)
        if result is True:
            self.client.expire(self.key, timeout)
            return True
        else:
            return False

    def release(self):
        """
        释放锁。
        """
        self.client.delete(self.key)
