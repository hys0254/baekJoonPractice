caseCnt = int(input())
books={}
for _ in range(caseCnt):
    book = input()
    books[book]=books.get(book,0)+1
max = max(books.values())
ans =[]
for book,cnt in books.items():
    if cnt == max :
        ans.append(book)
ans.sort()
print(ans[0])