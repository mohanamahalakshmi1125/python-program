def isPossible(books, students, maxPages):
    count = 1
    pages = 0

    for book in books:
        if pages + book > maxPages:
            count += 1
            pages = book
            if count > students:
                return False
        else:
            pages += book
    return True


def distributeBooks(books, students):
    low = max(books)
    high = sum(books)
    answer = high

    while low <= high:
        mid = (low + high) // 2
        if isPossible(books, students, mid):
            answer = mid
            high = mid - 1
        else:
            low = mid + 1

    return answer


# Example
books = [10, 20, 30, 40]
students = 2

print("Minimum maximum pages =", distributeBooks(books, students))
