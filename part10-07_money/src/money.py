# TEE RATKAISUSI TÄHÄN:
class Money:
    def __init__(self, euros: int, cents: int):
        self.__euros = euros
        self.__cents = cents
        self.__total = self.__euros + (self.__cents/100)
    def __str__(self):
        return f"{self.__total:.2f} eur"
    
    def __eq__(self, another):
        return self.__total == another.__total
    def __gt__(self, another):
        return self.__total > another.__total
    def __lt__(self, another):
        return self.__total < another.__total
    def __ne__(self, another):
        return self.__total != another.__total
    def __add__(self, another):
        result = self.__total + another.__total
        return f"{result:.2f} eur"
    def __sub__(self, another):
        result = self.__total - another.__total
        if result >= 0:
            return f"{result:.2f} eur"
        else:
            raise ValueError("a negative result is not allowed")
    
    

        
if __name__ == "__main__":
    e1 = Money(4, 5)
    print(e1)
    e1.euros = 1000
    print(e1)