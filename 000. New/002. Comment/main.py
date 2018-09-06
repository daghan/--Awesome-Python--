# 파이썬은 쉘 스크립트(.sh), YAML(.yaml), Ruby(.rb)처럼, 라인 주석에 sharp(#) 기호를 사용한다

"""
블록 주석에는 이처럼 세 개의 작은 따옴표, 또는 큰 따옴표로 감싸진
문자열 리터럴을 사용한다
"""
'''
문자열 리터럴만 분리되어 expression으로 존재하기에, 코드의 흐름에 별도의 영향을 끼치지 않기도 하고
값으로써 관리하기에 더 유연하기 때문에, 함수나 클래스 정의의 가장 top level에 사용하여
docstring(문서화 문자열)이라는 이름의 주석으로 사용하도록 권고한다
'''
# 따라서 여러 줄에 걸쳐 주석 처리를 하는 것을 포함한
# 일반적인 경우에는 #을 사용하는 것이 좋다