# 269 class ��ü�� �Ӽ� ���� 

# Stock Ŭ���� ���� 
class Stock:
    # ������ ����
    # �����, �����ڵ�, PER, PBR, �����ͷ� ������
    def __init__(self, name, code, per, pbr,dividend ):
        self.name = name
        self.code = code 
        self.per = per
        self.pbr = pbr 
        self.dividend = dividend
    
    def set_name(self, name):
        self.name = name

    def set_code(self, code):
        self.code = code

    def set_per(self, per):
        self.per = per

    # PBR �޼��� 
    def set_pbr(self, pbr):
        self.pbr = pbr     

    def set_dividend(self, dividend):
        self.dividend = dividend


    def get_name(self):
        return self.name

    def get_code(self):
        return self.code

# ���� ��ü 
samsung = Stock("�Ｚ����", "005930", 15.79, 1.33, 2.83)
# PER ��ü �Ӽ� ����
samsung.set_per(12.75)
# �Ӽ� ȣ��
print(samsung.per)