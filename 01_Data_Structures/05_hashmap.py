class HashMap:

    def __init__(self, capacity):
        self.capacity = capacity 
        self.size = 0 
        self.buckets = [[] for _ in range(capacity)]

    # O(1) - constant time
    def __len__(self):
        return self.size

    # Average: O(1) - contant time
    # Worst: O(n) - linear time
    # Depends on the quality of the hash function
    def __contains__(self, key):
        index = self._hash_function(key)
        bucket = self.buckets[index]

        for k, v in bucket:
            if k == key:
                return True
            
        return False    
        
    # Average: O(1) - contant time
    # Worst: O(n) - linear time
    # Depends on the quality of the hash function
    def put(self, key, value):
        index = self._hash_function(key)
        bucket = self.buckets[index]

        for i, (k,v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                break
        else:
            bucket.append((key, value))
            self.size += 1

    # Average: O(1) - contant time
    # Worst: O(n) - linear time
    # Depends on the quality of the hash function
    def get(self, key):
        index = self._hash_function(key)
        bucket = self.buckets[index]

        for k,v in bucket:
            if k == key:
                return v
            
        raise KeyError('Key not found')

    # Average: O(1) - contant time
    # Worst: O(n) - linear time
    # Depends on the quality of the hash function
    def remove(self, key):
        index = self._hash_function(key)
        bucket = self.buckets[index]

        for i, (k,v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                self.size -= 1
                break
        else:
            raise KeyError('Key not found')

    # O(n) - linear time
    def keys(self):
        return [k for bucket in self.buckets for k, _ in bucket]

    # O(n) - linear time
    def values(self):
        return [v for bucket in self.buckets for _, v in bucket]

    # O(n) - linear time
    def items(self):
        return [(k, v) for bucket in self.buckets for k, v in bucket]

    # O(k) - linear in key length (practically: O(1))
    def _hash_function(self, key):
        key_string = str(key)
        hash_result = 0
        
        for c in key_string:
            hash_result = (hash_result * 31 + ord(c)) % self.capacity

        return hash_result

if __name__ == '__main__':
    hash_map = HashMap(32)
    
    hash_map.put('name', 'Mike')
    hash_map.put('age', 30)
    hash_map.put('job', 'Programmer')
    hash_map.put('country', 'USA')

    hash_map.put('age', 31) 

    print('name' in hash_map)
    print('salary' in hash_map)

    print(hash_map.get('job'))

    print(f"Keys  : {hash_map.keys()}")
    print(f"Values: {hash_map.values()}")
    print(f"Items : {hash_map.items()}")

    hash_map.remove('country')
    print('country' in hash_map) 
    
    print(len(hash_map)) 

    print(hash_map.buckets)

    ### Visualization Codes for checking distibution of hash function results
    
    # import uuid
    # import matplotlib.pyplot as plt

    # hash_map = HashMap(1000)

    # for _ in range(100000):
    #     hash_map.put(uuid.uuid4(), 'some_value')
    
    # X = []
    # Y = []

    # for i, bucket in enumerate(hash_map.buckets):
    #     X.append(i)
    #     Y.append(len(bucket))
    
    # plt.bar(X,Y)
    # plt.show()
