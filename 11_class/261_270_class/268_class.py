# 268 class �޼��� �߰�

# Ŭ���� ���� 
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
    
    # PER �޼��� �߰� 
    def set_per(self, per):
        self.per = per
    
    # PBR �޼��� �߰�
    def set_pbr(self, pbr):
        self.pbr = pbr     

    # ��޼��ͷ� �޼��� �߰�
    def set_dividend(self, dividend):
        self.dividend = dividend


    def get_name(self):
        return self.name

    def get_code(self):
        return self.code