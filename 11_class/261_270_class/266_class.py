# 266 class 객체의 속성값 업데이트
# *답안 확인 

# 클래스 정의 
class Stock:
    # 메서드 정의
    # 생성자 정의
    # 종목명, 종목코드 생성자
    # PER, PBR, 배당수익률 생성자 추가
    def __init__(self, name, code, per, pbr, money):
        self.name = name
        self.code = code 
        # 속성 없데이트
        self.per = per #PER 생성자 추가
        self.pbr = pbr # PBR 생성자 추가
        self.money = money # 배당수익률 생성자 추가
    
    # 종목명 메서드 추가
    def set_name(self, name):
        self.name = name

    # 종목코드 메서드 추가 
    def set_code(self, code):
        self.code = code
    
    # 종목명 속성 업데이트   
    def get_name(self):
        return self.name
    
    # 종목코드 속성 업데이트
    def get_code(self):
        return self.code