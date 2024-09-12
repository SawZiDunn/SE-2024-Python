class Poly:
    def __init__(self, x) -> None:
        self._x = x
        
    def add(self, p):
        end_index = 0
        p_poly: tuple = p._x
        result = []
        for i in range(min(len(p_poly), len(self._x))):
            result.append(p_poly[i] + self._x[i])
            end_index = i + 1
        
        if len(p_poly) > len(self._x):
            longer_poly = p_poly
        else:
            longer_poly = self._x
        result += longer_poly[end_index:]
        return Poly(result)
            
    def scalar_multiply(self, n):
        result = [x * n for x in self._x]
        return tuple(result)
    
    def multiply(self, p):
        result_poly_len = len(p._x) * len(self._x)
        result = [0 for _ in range(result_poly_len)] # initializing all places to 0
        
        for i in range(len(p._x)):
            for j in range(len(self._x)):
                result[i + j] += p._x[i] * self._x[j]
        return Poly(result)
    
    def power(self, n):
        result = list(self._x).copy()
        
        for i in range(n - 1):
            result = self.multiply(Poly(result))._x
        return Poly(result)
    
    def diff(self):
        new_poly_list = list()
        for i in range(len(self._x) - 1):
            new_poly_list.append(self._x[i + 1] * (i + 1))
        return Poly(new_poly_list)
    
    def integrate(self):
        new_poly_list = [0]
        for i in range(len(self._x)):
            new_poly_list.append(self._x[i] / (i + 1))
        return Poly(new_poly_list)
    
    def eval(self, n):
        total = 0
        for i in range(len(self._x)):
            total += self._x[i] * pow(n, i)
        print(total)
    
    def print(self):
        result = ""
        for (index, i) in enumerate(self._x):
            power = f"^{index}" if index != 1 else ""
            if i > 0 and index != 0:
                result += " + x{power}" if i == 1 else f" + {abs(i)}x{power}"
         
            elif i < 0 and index != 0:
                result += f" - x{power} " if i == -1 else f" - {abs(i)}x{power} "
                    
            elif i != 0 and index == 0:
                result += str(i)
        if result.startswith(" + "):
            result = result[3:]
        elif result.startswith(" - "):
            result = result[1:]
        print(result)
        
    
def main():
    p = Poly((1, 0, -2))
    p.print()
    q = p.power(2)
    q.print()
    
    p.eval(3)
    r = p.add(q)
    r.print()
    
    r.diff().print()
    
    
main()