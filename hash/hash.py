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

    def closed_collision(self, key, value):
        # Força a colisão de chaves com o mesmo índice na tabela hash
        index = hash(key) % self.capacity
        # Encontra a próxima posição disponível usando sondagem linear
        while index in self.cache:
            index = (index + 1) % self.capacity
        # Insere a chave forçando a colisão
        self.cache[index] = value
        self.access_order.append(index)

    def open_collision(self, key, value):
        # Força a colisão de chaves na mesma posição usando listas ligadas
        index = hash(key) % self.capacity
        # Verifica se já há um item nesta posição
        if index in self.cache:
            # Se já existir, cria uma lista ligada
            if not isinstance(self.cache[index], list):
                self.cache[index] = [self.cache[index]]
            # Adiciona o novo item à lista ligada
            self.cache[index].append(value)
        else:
            # Se não houver colisão, insere o valor normalmente
            self.cache[index] = value
        self.access_order.append(index)

    def hash_perfeito(self, key):
        A = (5 ** 0.5 - 1) / 2
        frac_part = key *A - int(key * A)
        index = int(self.capacity * frac_part)
        return index
        
    def hash_imperfeito(self, key):
        #usa a propria função hash embutida
        return hash(key) % self.capacity