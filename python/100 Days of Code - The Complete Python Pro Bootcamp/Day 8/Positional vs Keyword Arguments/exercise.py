def calculate_love_score(name1, name2):
    # 소문자로 변환
    name1 = name1.lower()
    name2 = name2.lower()

    # 이름 합치기
    combined_names = name1 + name2

    # TRUE 각 글자 수 세기
    true_score = 0
    for letter in "true":
        true_score += combined_names.count(letter)

    # LOVE 각 글자 수 세기
    love_score = 0
    for letter in "love":
        love_score += combined_names.count(letter)

    # 두 수를 이어붙여 love score 생성
    love_score_str = str(true_score) + str(love_score)
    love_score_int = int(love_score_str)

    print(love_score_int)


calculate_love_score("Kanye West", "Kim Kardashian")