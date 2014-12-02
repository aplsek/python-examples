

def dictizeString(string, dictionary):
    while string.startswith('/'):
        string = string[1:]
    parts = string.split('/', 1)
    if len(parts) > 1:
        branch = dictionary.setdefault(parts[0], {})
        dictizeString(parts[1], branch)
    else:
        if dictionary.has_key(parts[0]):
             # If there's an addition error here, it's because invalid data was added
             dictionary[parts[0]] += 1
        else:
             dictionary[parts[0]] = 1



d = {}
dictizeString('/a/b/c/d', d)
dictizeString('/a/b/c/d', d)
dictizeString('/a/b/e', d)
dictizeString('/c', d)
print d