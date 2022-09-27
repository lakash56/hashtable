class HashTable:

	def __init__(self, m):
		self.m = m
		self.hash_table = self.create_hash_table()

	def create_hash_table(self):
		return [[] for _ in range(self.m)]

	
	def insert(self, key, val):
		
		
		hashed_key = hash(key) % self.m
		
	
		bucket = self.hash_table[hashed_key]

		found_key = False
		for index, record in enumerate(bucket):
			record_key, record_val = record
			
			
			if record_key == key:
				found_key = True
				break

		
		if found_key:
			bucket[index] = (key, val)
		else:
			bucket.append((key, val))

	def search(self, key):
		hashed_key = hash(key) % self.m	
		bucket = self.hash_table[hashed_key]
		found_key = False
		for index, record in enumerate(bucket):
			record_key, record_val = record
			if record_key == key:
				found_key = True
				break
		if found_key:
			return record_val
		else:
			return "No record found"

	def delete(self, key):
		
		hashed_key = hash(key) % self.m
		
	
		bucket = self.hash_table[hashed_key]

		found_key = False
		for index, record in enumerate(bucket):
			record_key, record_val = record
			
			if record_key == key:
				found_key = True
				break
		if found_key:
			bucket.pop(index)
		return

	def __str__(self):
		return "".join(str(item) for item in self.hash_table)


hash_table = HashTable(4)

hash_table.insert('Lakash Maharjan', 'CS')
print(hash_table)
print()

hash_table.insert('Abhi', 'DSAI')
print(hash_table)
print()

hash_table.insert('Max', 'IOT')
print(hash_table)
print()

hash_table.insert('Srijan', 'IM')
print(hash_table)
print()

print(hash_table.search('Max'))
print()

hash_table.delete('Max')
print(hash_table)
