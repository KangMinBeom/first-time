import random

def generate_lotto_numbers():
    lotto_numbers = random.sample(range(1, 46), 6)
    lotto_numbers.sort()
    return lotto_numbers


if __name__ == "__main__":
    lotto_numbers = generate_lotto_numbers()
    print("로또 추천 번호:", lotto_numbers)

def count_common_elements(list1, list2):
    # 두 리스트에서 공통 요소를 찾고 세는 방법
    common_elements = set(list1) & set(list2)
    count = len(common_elements)
    return count

 # 예제 리스트
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]

common_count = count_common_elements(list1, list2)
print("두 리스트에서 공통된 요소의 개수:", common_count)
