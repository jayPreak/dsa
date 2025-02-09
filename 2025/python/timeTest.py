import time

# Adding 1M elements to a list
lst = []
start = time.time()
for i in range(10_000_000):
    lst.append(i)
print("List append time:", time.time() - start)

# Adding 1M elements to a set
st = set()
start = time.time()
for i in range(10_000_000):
    st.add(i)
print("Set add time:", time.time() - start)
