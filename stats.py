def count_words(file_contents):
    words = file_contents.split()
    return len(words)

def count_char(file_contents):
    if not isinstance(file_contents, str):
      return {}
    
    file_contents = file_contents.lower()
    counts = {}
    for char in file_contents:
        counts[char] = counts.get(char, 0) +1
    return counts

def sort_char_counts(char_counts):
    sorted_list = []
    for char, count in char_counts.items():
        sorted_list.append({"char": char, "count": count})
    sorted_list.sort(key=lambda x: x["count"], reverse=True)
    return sorted_list