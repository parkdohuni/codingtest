def count_cards(card_str, tc):
    counts = {'S': 13, 'D': 13, 'H': 13, 'C': 13}
    cards = set()

    for i in range(0, len(card_str), 3):
        card = card_str[i:i + 3]
        suit, number = card[0], card[1:]

        if card in cards:
            print("#{} {}".format(tc, "ERROR"))
            return

        cards.add(card)

        if counts[suit] == 0:
            print("#{} {}".format(tc, "ERROR"))
            return

        if int(number) <= 13:
            counts[suit] -= 1
        else:
            print("#{} {}".format(tc, "ERROR"))
            return

    print("#{} {} {} {} {}".format(tc, counts['S'], counts['D'], counts['H'], counts['C']))


# 테스트케이스 수 입력
t = int(input())

for tc in range(1, t + 1):
    # 카드 정보 입력
    card_info = input().strip()
    count_cards(card_info, tc)