class Cache:
    """
    ac_order = access order = ordem de acesso
    """
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.ac_order = []

    def get(self, key):
        if key in self.cache:
            self.ac_order.remove(key)
            self.ac_order.append(key)
            return self.cache[key]
        else:
            return None

    def put(self, key, value):
        if key in self.cache:
            self.cache[key] = value
            self.ac_order.remove(key)
            self.ac_order.append(key)
        else:
            if len(self.cache) >= self.capacity:
                oldest_key = self.ac_order[0]
                del self.cache[oldest_key]
                del self.ac_order[0]

            self.cache[key] = value
            self.ac_order.append(key)