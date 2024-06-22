# Homework3
def word_counter(file_path):
    tu_dien_dem = {}
    with open(file_path, 'r') as file:
        for line in file:
            words = line.split()
            for word in words:
                word = word.lower()  # chuyển đổi thành chữ thường
                if word in tu_dien_dem:
                    tu_dien_dem[word] += 1
                else:
                    tu_dien_dem[word] = 1
    return tu_dien_dem
file_path = r'C:\Users\Hello!!\OneDrive\Desktop\Demo Git\P1_data.txt'
print(word_counter(file_path))