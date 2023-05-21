# 컴퓨터 프로그래밍 인터렉티 스토리 과제 - 메이즈러너를 차용한 미로게임
from random import *

def start_game():
    print("[미로 게임]\n")

    print("당신은 피터입니다.")
    print("깊은 잠에 들고 깨어났는데 눈을 뜬 곳은 미로 한가운데이고 옆에는 종이 하나가 놓여져 있습니다.\n")
    player_name = "피터"
    print(f"'미로 게임에 오신 것을 환영합니다, {player_name}!")
    print("2050년, 지구는 무정부 상태에 접어들었습니다.")
    print("자연 재앙으로 인해 인류는 황폐한 땅에서 살아가고 있습니다.")
    print("이런 상황 속에서 권력자들은 자신의 힘을 계속 유지하기 위해 경쟁자를 줄일 목적으로 '미로 게임'을 개최합니다.")
    print("살기 위해서는 미로를 탈출하세요! 그럼 행운을 빕니다.'")

    print("----------------------------------------------------------------------------")


def happy_ending():
    print("-----------------------------------------------------")

    print("피터는 마침내 빛이 보이는 통로를 발견하고 탈출에 성공하였습니다.")
    print("중간에는 갖은 시련과 위험한 상황들이 있었지만 두려움을 극복하며 얼려움을 해결했습니다.")
    print("하지만 행복함을 느끼기도 잠시 세상에 피터와 같이 아무 이유 없이 갇힌 사람들이 많았기에 더 큰 도전에 직면하였습니다.")
    print("미로 속에서 동료들과 협력했던 것처럼, 권력자들의 약점을 찾아내고 약화시키기 위해 노력했습니다.")
    print("용기있게 행동하고 재치있는 전략을 사용함으로써 권력자들의 힘을 무력화시키며,사회에 정의와 자유를 되찾아왔습니다.")
    print("피터의 이야기는 미로를 빠져나온 해피엔딩처럼 보일 수 있겠지만, 새로운 모험의 시작이기도 했습니다.")
    print("이제 그는 미로를 헤치며 겪었던 동료들과의 추억을 되새기며 스스로를 성장시키고 사회적인 변화를 이끌기 위해 노력할 것입니다.")


def explore_city():
    exit_north = "북쪽으로"
    exit_west = "서쪽으로"
    exit_east = "동쪽으로"

    print("여러 개의 길이 다양한 방향으로 펼쳐져 있습니다:")
    print("1. " + exit_north)
    print("2. " + exit_west)
    print("3. " + exit_east)

    choice = int(input("어느 방향으로 이동하시겠습니까? 각 길은 퀴즈를 푸는 곳일수도, 막다른 길일수도, 괴물이 있을 수도 있습니다. (행동할 숫자를 입력하세요): "))

    if choice == 1:
        print(exit_north + " 이동합니다.")

        print("[퀴즈를 풀어야합니다.]")

        print("피터가 그와 같은 처지에 있는 사람 3명을 만난다.")
        response = input("대화하시겠습니까? (예/아니오):\n ")
        if response == "예":

            print("피터: 안녕하세요. 전 피터입니다. 당신들도 지금 여기에 갇혀있나요?")
            print("에밀리: 맞아요. 저는 에밀리고, 눈을 떴더니 게임 초대장과 함께 미로 한복판에 있었어요.")
            print("톰: 저희는 톰과 잭이고 모두 친구입니다.")
            print("잭: 사람이 한명 더 늘어서 든든하군요. 얼른 같이 게임을 풀고 이 답답한 곳에서 탈출합시다.")
            print("피터: 좋습니다. 저희에게 주어진 게임이 무엇인가요?\n")

            choice = input("[게임을 시작하려면 숫자 '1'을 입력하세요]: \n")


        elif response == "아니오":
            print("혼자 해결해나간다.")

        solving_the_puzzle()

    elif choice == 2:
        print(exit_west + " 이동합니다.")

        print("[괴물과 싸워 이겨야합니다.]\n")
        monster()

    elif choice == 3:

        print("[막혀 있는 길입니다. 다른쪽으로 이동하세요.]\n")
        start_game()
        explore_city()

    else:
        print("막혀 있는 길입니다. 다른쪽으로 이동하세요.")
        start_game()
        explore_city()


def solving_the_puzzle():
    print("[숫자 게임을 시작합니다. 4개의 숫자로 24를 만들어야합니다.")
    print("어떠한 사칙연산 기호가 주어질지 모르니 신중하게 선택해야 합니다.]\n")
    print("(피터와 팀원들은 울려대는 초침소리에 당황한다.)\n")

    print("피터: 이렇게 벌써 시작한다고?")
    print("에밀리: 그러게 말이에요. 제한시간이 있는 것 같은데 빨리 아무 숫자나 입력할까요?")
    print("톰: 그랬다가 24를 만들지 못하면 어떡해.")
    print("피터: 그래도 일단 해보자고요!")

    numbers = []
    for i in range(4):
        number = int(input(f"{i + 1}번째 숫자를 입력하세요: \n"))
        numbers.append(number)

    operators = ['+', '-', '*', '/']
    equation = ""
    for i in range(3):
        operator = input(f"{i + 1}번째 사칙연산 기호를 입력하세요 (+, -, *, /) : ")

        equation += str(numbers[i]) + operator
    equation += str(numbers[3])

    result = eval(equation)
    if result == 24:
        print("피터,에밀리,톰,잭: 했다!!!\n")
        print("[축하합니다. 퍼즐을 해결했습니다. 마지막 한 관문이 남았습니다.]\n")
        print("잭: 그럼그렇지. 이렇게 쉽게 빠져나갈 수 있을거란 생각은 애초에 하지 않았어.")
        print("에밀리: 그래도 한 관문은 통과한거잖아?")
        print("피터: 에밀리 말이 맞아, 잭. 탈출할 방법이 보이니까 조금만 더 머리를 맞대보자!\n")
        print("톰: 저기.. 얘들아 여기 빨리 와봐야할 것 같아.")

        choice = input("계속하려면 키보드 내 어떤 문구든 입력하세요.\n")

        solving_the_number_puzzle()
    else:
        print("아쉽게도 24를 만들지 못했습니다. 미로에서 탈출할 수 없습니다. 다시 시도하세요.")
        solving_the_puzzle()


def solving_the_number_puzzle():
    print("------------------------")
    print(" 첫번째 관문을 넘었군요. 두번째 게임은 더욱 만만치 않습니다. 그럼 행운을 빕니다!\n")
    print(" [두번째 숫자 게임을 시작합니다. 1에서 100 사이의 랜덤 숫자가 지정되어 있습니다. 그 숫자를 맞춰보세요. 기회는 단 3번입니다.]\n")

    print("에밀리: 이건 또 뭐야.")
    print("잭: 완전 랜덤으로 찍어야 하는거 아니야?")
    print("피터: 단계가 있지 않을까? 이것도 한 번 차분히 해보자.")

    target_number = randint(1,100) #1부터 100사이의 임의의 정수
    guess_attempts = 3

    while guess_attempts > 0:
        guess = int(input("숫자를 입력하세요: "))

        if guess < target_number:
            print(" [더 큽니다.]")
            print("톰: 이게 힌트 전부야? ")
            print("잭: 그러게. 너무하긴하다.")
            print("에밀리: 신중하게 하자.")
        elif guess > target_number:
            print(" [더 작습니다.]")
            print("피터: 무슨 숫자를 해야할까...")

        else:
            print(" [정답입니다! 퍼즐을 해결했습니다. 열린 문을 통해 미로에서 탈출하세요!]\n")
            print("피터: 우리가 해냈어!!")
            print("잭: 역시 난 우리가 해낼 줄 알았어.얘들아 너무 수고했어.")
            print("톰: 다행이다. 여기서 드디어 탈출할 수 있다니!")
            print("에밀리: 우리 이런 잡담할 시간에 얼른 탈출할까?")
            print("피터: 하하 그러자!\n")

            happy_ending()
            break

        guess_attempts -= 1
        if guess_attempts > 0:
            print(f"[남은 기회: {guess_attempts}번]")

        else:
            print("기회를 모두 사용하였습니다. 퍼즐을 해결하지 못했습니다. 미로에서 탈출할 수 없습니다. 다시 시도하세요.")
            solving_the_number_puzzle()


def monster():
    print("문을 열고 들어가면 괴물이 있습니다.")
    print("무기가 무엇인지도, 괴물의 크기가 어떤지도 알 방법이 없습니다.")
    print("혼자 하시겠습니까, 동료들과 같이 도전하시겠습니까?\n")

    choice = input("1. 혼자 한다.   2. 동료들과 같이 한다.\n")

    if choice == '1':
        one_player()
    elif choice == '2':
        multi_player()
    else:
        print("잘못된 선택입니다.")
        monster()


def one_player():
    print("피터는 혼자 맞서 싸우기로 결정합니다.")
    print("용감하게 싸우지만 괴물의 수가 늘어나고 점점 지쳐갑니다.")
    print("어떤 선택을 하시겠습니까?")

    choice = input("1.계속 싸운다.  2. 도망간다.\n")

    if choice == '1':
        continue_fighting()
    elif choice == '2':
        run_away()
    else:
        print("잘못된 선택입니다.")
        one_player()


def continue_fighting():
    print("피터가 힘겹게 싸우고 있던 그 때 ")

    print("갑자기 멀리서 동료들이 괴물을 물리치며 등장한다.")
    print("희망을 가진 피터는 그들에게 다가간다.\n")
    multi_player()


def run_away():
    print("도망을 치다 우연히 다른 사람들이 괴물과 싸우는 모습을 목격하고 합류한다.")
    multi_player()


def multi_player():
    print("피터: 안녕하세요. 전 피터에요!")
    print("에밀리: 지금 이 상황에서 인사가 나오나요? 얼른 괴물부터 해치우고 얘기합시다!")
    print("톰: 이쪽이야 도와줘!\n")

    print("[피터와 에밀리, 톰, 잭은 전투에 돌입합니다.]")

    print("피터: 제가 갈게요. 저에게 무기가 있어요")
    print("톰: 저에게 무기를 던져주세요!")

    choice = input("1. 무기를 건네준다  2. 믿을 수 없는 사람이니 건네주지 않는다.\n")

    if choice == "1":
        print("톰: 감사합니다! 이쪽은 제게 맡기세요!")
        print("피터: 네 제가 뒤를 맡을게요!")
        print("피터, 에밀리, 톰, 잭은 이름도 모르는 상태에서 서로를 믿고 협력하여 괴물과의 전투에 승리한다.\n")
        after_monster()

    elif choice == "2":
        print("피터: '방금 봤는데 내가 어떻게 믿고 나의 무기를 건네줘'")
        print("피터: '나 혼자 싸워야겠다'\n")

        print("당신은 동료를 믿지 않고 본인만 생각하였다가 괴물에 패하였습니다.미로를 탈출할 수 없습니다. 다시 시도하세요.\n")
        monster()


def after_monster():
    print("피터: 이제야 정식으로 인사를 드리네요. 전 피터입니다. 아까 너무 멋지셨어요!")
    print("톰: 하하 감사합니다 건네주신 무기 덕분에 성공적으로 할 수 있었어요")
    print("에밀리, 잭: 저희도 여기 있어요!!")
    print("피터: 앗 죄송합니다. 승리했다는 사실에 너무 신이 나서 그만.. 이름이 어떻게 되세요?")
    print("에밀리: 전 에밀리이고 여기 옆은 제 친구 잭이에요.")
    print("잭: 안녕하세요! 그럼 저쪽으로 나가볼까요?")
    print("피터,톰: 네 그럽시다!\n")

    choice = input("결말을 보려면 키보드 내 아무 문자나 입력하세요.")
    happy_ending()


start_game()
explore_city()
