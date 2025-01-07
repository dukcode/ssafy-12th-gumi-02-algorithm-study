# A + B - 4



import sys

# while 1:
#     a, b = map(int, sys.stdin.readline().split())
#     print(a + b)


while 1:
    try :
        a, b = map(int, sys.stdin.readline().split())
        print(a + b)
    except :
        break




# while문의 조건은 1을 이용해 True로 돌릴 수 있따!

# 근데 런타임 에러가 나옴 이유는 sys.stdin.readline() 사용때문에

# 질문 게시판 답안

# 채점 데이터 파일에 수많은 데이터 줄을 한 줄씩 읽어서 a,b로 받아 채점을 하게 될텐데, 
# 해당 파일의 끝을 EOF(End of File)라고 합니다.

# 파이썬에서 input()함수는 EOF를 만나면 EOFError를 발생시키지만, 
# sys.stdin.readline()은 에러를 발생시키지 않고 빈 문자열을 내놓습니다

# 그래서 첫번째 코드는 EOFError가 발생하면, except EOFError:에 의해 무한반복문을 탈출해서 통과하지만,
# 두번째 코드는 sys.stdin.readline() = ''이기 때문에 
# a,b = map(int, ''.split())을 실행시켜보시면 ValueError가 발생하는 것을g 알 수 있습니다.
# (''.split() = []이라서, a,b 두 변수에 할당할 수 없기 때문입니다)

# 그래서 except EOFError:를 실행하기 전에 
# a, b = map(int, sys.stdin.readline().split())에서 ValueError로 런타임에러가 납니다.

# sys.stdin.readline()으로 통과하고 싶다면, 
# 1) except ValueError:를 사용하거나, 
# 2) 어떠한 에러가 일어날지 몰라 모든 에러처리를 하고 싶어서 except:만 사용하면 됩니다 



# error를 제거해야함!

# 근데 eof 구분을 어케하란거지..?