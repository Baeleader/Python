## 신한은행 기준 환전

# 각나라의 매매기준율
USD = 1171.00 ## 미국 달러 dollar
JPY = 1078.17 ## 일본 엔 yen
CNY = 165.68 ## 중국 위안 yuan
EUR = 1307.66 ## 유럽 유로 euro
GBP = 1519.67 ## 영국 파운드 pound

class Exchange:
    
    def __init__(self):
        
        #거래 종류 반복문
        while True:
            
            print("원하시는 거래의 종류를 선택해주세요.")
            bank = int(input("[1]. 현찰 살 때, [2]. 현찰 팔 때, [3] 송금 보낼 때\n"))
            if bank == 1 or bank == 2:
                self.bank = bank
                break
            elif bank == 3:
                self.bank = bank
                break
            else :
                print("거래항목에 없는 거래이십니다. \n")
                print("다시 선택해주세요")
                continue
                
        # 나라선택 반복문
        while True:
        
            print("\n원하시는 나라를 선택하세요")
            money = input("[U]. 미국, [J]. 일본, [C]. 중국, [E]. 유럽, [G]. 영국\n")

            if money == 'U' or money == 'u':
                self.money = money
                break
            elif money == 'J' or money == 'j':
                self.money = money
                break
            elif money == 'C' or money == 'c':
                self.money = money
                break
            elif money == 'E' or money == 'e':
                self.money = money
                break
            elif money == 'G' or money == 'g':
                self.money = money
                break
            else :
                print("선택하신 나라가 항목에 없습니다\n")
                print("다시 선택하여 주시겠습니까?\n")
                
    def commission(self):
        # 타국의 현찰을 구매할 시 가격
            buycny = 174.03
            buyjpy = 1097.50
            buyusd = 1192.00
            buyeur = 1334.00
            buygbp = 1550.36
        
        # 타국의 현찰을 판매할 시 가격
            sellcny = 157.47
            selljpy = 1059.76
            sellusd = 1151.00
            selleur = 1282.20
            sellgbp = 1490.16
        
        # 송금 보낼 때 가격
            tosscny = 167.40
            tossjpy = 1088.98
            tossusd = 1182.70
            tosseur = 1320.91
            tossgbp = 1535.15
        
        # 현찰 구매 수수료 = 현찰을 살 때 - 매매기준율
            self.commissioncny = buycny - CNY
            self.commissionjpy = buyjpy - JPY
            self.commissionusd = buyusd - USD
            self.commissioneur = buyeur - EUR
            self.commissiongbp = buygbp - GBP
            
        # 현찰 판매 수수료 = 매매기준율 - 현찰을 팔 때
            self.sellcommissioncny = CNY - sellcny
            self.sellcommissionjpy = JPY - selljpy
            self.sellcommissionusd = USD - sellusd
            self.sellcommissioneur = EUR - selleur
            self.sellcommissiongbp = GBP - sellgbp
            
        # 송금 보낼시 수수료 = 송금보낼떄 - 매매기준율
            self.tosscommissioncny = tosscny - CNY
            self.tosscommissionjpy = tossjpy - JPY
            self.tosscommissionusd = tossusd - USD
            self.tosscommissioneur = tosseur - EUR
            self.tosscommissiongbp = tossgbp - GBP
    
    def change(self):
        print("각 나라의 환율입니다.\n")
        print("중국 : %.2f(원), 일본 : %.2f(원), 미국 : %.2f(원), 유럽연합 : %.2f(원), 영국 : %.2f(원)" %(CNY, JPY, USD, EUR, GBP))
        
        
        # 현찰을 구매할 때
        if self.bank == 1:
            
            krw = int(input("얼마만큼의 돈(한국)을 환전하시겠습니까?\n"))
            
            # 수수료 보여주기
            print("\n타국의 현찰을 구매하실때의 수수료비용입니다")
            print("중국 : %.2f(yuan), 일본 : %.2f(yen), 미국 : %.2f(dollar), 유럽연합 : %.2f(euro), 영국 : %.2f(pound) \n"
                  %(self.commissioncny, self.commissionjpy, self.commissionusd, 
                    self.commissioneur, self.commissiongbp))
            
            # 은행에서 가져간 수수료 비용과 포함된 환전머니.
            if self.money == 'U' or self.money == 'u':  
                
                ExchangMoney = (krw - self.commissionusd) / USD
                
                print("수수료 포함 환전되신 금액은 %.2f(Dollar)입니다.\n" %ExchangMoney)
                
            elif self.money == 'J' or self.money == 'j':   
                
                ExchangMoney = (krw - self.commissionjpy) / JPY
                
                print("수수료 포함 환전되신 금액은 %.2f(Yen)입니다.\n" %ExchangMoney)
                
            elif self.money == 'C' or self.money == 'c':  
                
                ExchangMoney = (krw - self.commissioncny) / CNY
                
                print("수수료 포함 환전되신 금액은 %.2f(Yuan)입니다.\n" %ExchangMoney)
                
            elif self.money == 'E' or self.money == 'e':  
                
                ExchangMoney = (krw - self.commissioneur) / EUR
                
                print("수수료 포함 환전되신 금액은 %.2f(Euro)입니다.\n" %ExchangMoney)
                
            elif self.money == 'G' or self.money == 'g':  
                
                ExchangMoney = (krw - self.commissiongbp) / GBP
                
                print("수수료 포함 환전되신 금액은 %.2f(Pound)입니다.\n" %ExchangMoney)
            else: return
            
        #현찰을 팔 때
        elif self.bank == 2:
            
            # 수수료 보여주기
            print("\n타국의 현찰을 판매하실때의 수수료비용입니다")
            print("중국 : %.2f(yuan), 일본 : %.2f(yen), 미국 : %.2f(dollar), 유럽연합 : %.2f(euro), 영국 : %.2f(pound) \n"
                  %(self.sellcommissioncny, self.sellcommissionjpy, self.sellcommissionusd, self.sellcommissioneur,
                    self.sellcommissiongbp))
            
            # 수수료 포함 원화로 바꾼 금액
            
            if self.money == 'U' or self.money == 'u':  
                dolloar = int(input("환전하실 달러를 입력하세요\n"))
                ExchangMoney = (USD - self.sellcommissionusd) * dolloar
                
                print("수수료 포함 환전되신 금액은 %.2f(won)입니다.\n" %ExchangMoney)
                
            elif self.money == 'J' or self.money == 'j':  
                yen = int(input("환전하실 엔을 입력하세요\n"))
                ExchangMoney = (JPY - self.sellcommissionyen) * yen
                
                print("수수료 포함 환전되신 금액은 %.2f(won)입니다.\n" %ExchangMoney)
                
            elif self.money == 'C' or self.money == 'c':  
                yuan = int(input("환전하실 위안을 입력하세요\n"))
                ExchangMoney = (CNY - self.sellcommissioncny) * yuan
                
                print("수수료 포함 환전되신 금액은 %.2f(won)입니다.\n" %ExchangMoney)
                
            elif self.money == 'E' or self.money == 'e':  
                euro = int(input("환전하실 유로를 입력하세요\n"))
                ExchangMoney = (EUR - self.sellcommissioneur) * euro
                
                print("수수료 포함 환전되신 금액은 %.2f(won)입니다.\n" %ExchangMoney)
                
            elif self.money == 'G' or self.money == 'g':
                pound = int(input("환전하실 파운드를 입력하세요\n"))
                ExchangMoney = (GBP - self.sellcommissiongbp) * pound
                
                print("수수료 포함 환전되신 금액은 %.2f(won)입니다.\n" %ExchangMoney)
            else: return
        
        #송금 보낼 때
        elif self.bank == 3:
            
            krw = int(input("얼마만큼의 돈(한국)을 송금하시겠습니까?\n"))
            
            # 수수료 보여주기
            print("\n타국으로 송금하실 때의 수수료비용입니다")
            print("중국 : %.2f(yuan), 일본 : %.2f(yen), 미국 : %.2f(dollar), 유럽연합 : %.2f(euro), 영국 : %.2f(pound) \n"
                  %(self.tosscommissioncny, self.tosscommissionjpy, self.tosscommissionusd,
                    self.tosscommissioneur, self.tosscommissiongbp))
            
            
            # 은행에서 가져간 수수료 비용과 포함된 환전머니.
            if self.money == 'U' or self.money == 'u':  
                
                ExchangMoney = (krw - self.tosscommissionusd) / USD
                
                print("수수료 포함 송금하신 금액은 %.2f(Dollar)입니다.\n" %ExchangMoney)
                
            elif self.money == 'J' or self.money == 'j':   
                
                ExchangMoney = (krw - self.tosscommissionjpy) / JPY
                
                print("수수료 포함 송금하신 금액은 %.2f(Yen)입니다.\n" %ExchangMoney)
                
            elif self.money == 'C' or self.money == 'c':  
                
                ExchangMoney = (krw - self.tosscommissioncny) / CNY
                
                print("수수료 포함 송금하신 금액은 %.2f(Yuan)입니다.\n" %ExchangMoney)
                
            elif self.money == 'E' or self.money == 'e':  
                
                ExchangMoney = (krw - self.tosscommissioneur) / EUR
                
                print("수수료 포함 송금하신 금액은 %.2f(Euro)입니다.\n" %ExchangMoney)
                
            elif self.money == 'G' or self.money == 'g':  
                
                ExchangMoney = (krw - self.tosscommissiongbp) / GBP
                
                print("수수료 포함 송금하신 금액은 %.2f(Pound)입니다.\n" %ExchangMoney)
            else: return
            
        else :
            print('ERROR')
ex = Exchange()
ex.commission()
ex.change()