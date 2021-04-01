class Path:
    def __init__(self, path):
        self.current_path = path

    def cd(self, new_path):
        cd_split = new_path.split("/")
        curr_split = self.current_path.split("/")
        for i in cd_split:
           if i == '..':
               curr_split = curr_split[:-1]
           else:
               curr_split.append(i)
        self.current_path = "/".join(curr_split)

# Driver code
path = Path('/a/b/c/d')
path.cd('../x')
print(path.current_path)
