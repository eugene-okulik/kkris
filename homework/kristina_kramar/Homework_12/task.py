class Flower():
    def __init__(self, name, color, price, freshness, length):
        self.name = name
        self.color = color
        self.price = price
        self.freshness = freshness
        self.length = length

    def __str__(self):
        return f'{self.name}'

    def __repr__(self):
        return f'{self.name}'


class Rose(Flower):
    def __init__(self, name, color, price, freshness, length, thorns):
        super().__init__(name, color, price, freshness, length)
        self.thorns = thorns


class Tulip(Flower):
    def __init__(self, name, color, price, freshness, length, blume_stage):
        super().__init__(name, color, price, freshness, length)
        self.blume_stage = blume_stage


class Lily(Flower):
    def __init__(self, name, color, price, freshness, length, aroma_intensity):
        super().__init__(name, color, price, freshness, length)
        self.aroma_intensity = aroma_intensity


class Bunch():
    def __init__(self, *args):
        self.list_flowers = self.create_bunch(*args)
        self.total_price = self.count_price()

    def create_bunch(self, *args):
        return list(args)
    
    def count_price(self):
        total_price = 0
        for flower in self.list_flowers:
            total_price += int(flower.price)
        return total_price

    def count_wilting_time(self):
        wilting_time = 0
        for flower in self.list_flowers:
            wilting_time += int(flower.freshness)
        return round(wilting_time / len(self.list_flowers))
    
    def sort_by_freshness(self):
        self.list_flowers.sort(key=lambda flower: int(flower.freshness))

    def sort_by_price(self):
        self.list_flowers.sort(key=lambda flower: int(flower.price))
    
    def sort_by_length(self):
        self.list_flowers.sort(key=lambda flower: int(flower.length))

    def find_by(self, param, value, type_of_comparison):
        result = []
        for flower in self.list_flowers:
            param_value = getattr(flower, param)
            if type_of_comparison == '=' and param_value == value:
                result.append(flower)
            elif type_of_comparison == '>' and param_value > value:
                result.append(flower)
            elif type_of_comparison == '<' and param_value < value:
                result.append(flower)
        return result


rose1 = Rose('rose', 'red', 10, 14, 100, True)
tulip1 = Tulip('tulip', 'yellow', 5, 5, 40, 'Bud')
lily1 = Lily('lily', 'violet', 8, 10, 180, 'Medium')
bouquet = Bunch(rose1, tulip1, lily1)

print(f"Список цветов в букете: {bouquet.list_flowers}")
print(f"Цена за букет: {bouquet.total_price}$")
print(f"Время жизни букета: {bouquet.count_wilting_time()} дней")

# sort by
bouquet.sort_by_price()
print(bouquet.list_flowers)

# find by
print(bouquet.find_by('freshness', 14, '<'))
