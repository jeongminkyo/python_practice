N = int(input())

book_dic = {}
for _ in range(N):
    book = input()

    if book in book_dic:
        book_dic[book] += 1
    else:
        book_dic[book] = 1

result = sorted(book_dic.items(), key=lambda kv: (-kv[1], kv[0]))

print(result[0][0])