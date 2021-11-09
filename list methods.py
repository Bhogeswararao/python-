# step 1:
Beatles = []
print("Step 1:", Beatles)

# step 2:

Beatles.append("John ")
Beatles.append("Paul ")
Beatles.append("George")
print("Step 2:", Beatles)

# step 3:
for members in range(2):
    Beatles.append(input("New member: "))
print("Step 3:", Beatles)

# step 4:
del Beatles[-1]
del Beatles[-1]
print("Step 4:", Beatles)

# step 5:
Beatles.insert(0, "Star")
print("Step 5:", Beatles)
print("The Fab:",len(Beatles))

