data = { "members": [
    {
        "id": 1,
        "name": "John Doe",
        "email": "john.doe@example.com"
    },
    {
        "id": 2,
        "name": "Jane Smith",
        "email": "jane.smith@example.com"
    }
] }


members = data["members"]
print(members)

print(members[0])

memCount = len(members)
print(memCount)