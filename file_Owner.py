def group_by_owners(dictionary):
    db = {}
    for key, val in dictionary.items():
        if val in db:
            db[val].append(key)
        else:
            db[val] = [key]
    return db


inp = {'Input.txt': 'Randy', 'Code.py': 'Stan', 'Output.txt': 'Randy'}
if __name__ == "__main__":
    op = group_by_owners(inp)
    print(op)
