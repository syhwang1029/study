# 266 class ��ü�� �Ӽ��� ������Ʈ
# *��� Ȯ�� 

# Ŭ���� ���� 
class Stock:
    # ������ ����
    # �����, �����ڵ�, PER, PBR, �����ͷ� ������
    def __init__(self, name, code, per, pbr, money):
        self.name = name
        self.code = code 
        self.per = per
        self.pbr = pbr 
        self.money = money
    
    # ����� �޼��� �߰�
    def set_name(self, name):
        self.name = name

    # �����ڵ� �޼��� �߰� 
    def set_code(self, code):
        self.code = code
    
    
    # ����� �Ӽ� ������Ʈ 
    def get_name(self):
        return self.name
    
    # �����ڵ� �Ӽ� ������Ʈ
    def get_code(self):
        return self.code