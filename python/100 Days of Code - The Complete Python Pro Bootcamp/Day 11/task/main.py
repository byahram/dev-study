import random
from art import logo

# Step 1: 카드 뽑기 함수 만들기
def deal_card():
    """Returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]  # # 11은 에이스, 10은 J, Q, K
    card = random.choice(cards)
    return card

# Step 2: 점수 계산 함수 만들기
def calculate_score(cards):
    """Take a list of cards and return the score calculated from the cards"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0  # 블랙잭

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)  # 에이스를 1로 처리

    return sum(cards)

# Step 3: 승패 비교 함수 만들기
def compare(u_score, c_score):
    """Compares the user score u_score against the computer score c_score."""
    if u_score == c_score:
        return "Draw 🙃"
    elif c_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif u_score == 0:
        return "Win with a Blackjack 😎"
    elif u_score > 21:
        return "You went over. You lose 😭"
    elif c_score > 21:
        return "Opponent went over. You win 😁"
    elif u_score > c_score:
        return "You win 😃"
    else:
        return "You lose 😤"

# Step 4: 게임 전체 흐름을 관리하는 함수 play_game() 만들기
def play_game():
    print(logo)  # 게임 시작 시 로고 출력
    user_cards = []
    computer_cards = []
    computer_score = -1
    user_score = -1
    is_game_over = False

    # 사용자와 컴퓨터에게 각각 2장씩 카드 배분
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    # 사용자 턴
    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    # 컴퓨터 턴: 점수가 17 미만이면 계속 받음
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    # 결과 출력
    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))


while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    print("\n" * 20)  # 콘솔 화면 초기화 효과
    play_game()
