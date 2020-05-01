from numpy.random import choice

class Edge:
    def __init__(self, length):
        self.length, self.feroment, self.delta = length, 1, 0

shortest_path, path = float("inf"), []

g = {
	'A': {'B': Edge(2), 'C': Edge(3), 'D': Edge(6)},
	'B': {'E': Edge(4), 'F': Edge(5)},
	'C': {'E': Edge(2), 'F': Edge(3)},
	'D': {'E': Edge(5), 'F': Edge(2)},
	'E': {'G': Edge(2)},
	'F': {'G': Edge(1)},
	'G': {},
}

class Ant:
    def __init__(self, start, target):
        self.tabu_list = []
        self.vertice = start
        self.target = target
        self.path_length = 0
        self.path = []
        self.alive = True

    def step(self):
        # абсолютні характеристики привабливості дозволених напрямків
        pre_probability = {
            to: (g[self.vertice][to].feroment + 1 / g[self.vertice][to].length) for to in (set(g[self.vertice].keys()) - set(self.tabu_list))
        }

        # якщо мурашка не може нікуди йти то вона "мертва"
        if not pre_probability:
            self.alive = False
            return

        # нормалізуємо абсолютні привабливості до відносних
        sum_pre_probability = sum(pre_probability.values())

        probability = {
            to: pre_probability[to] / sum_pre_probability
            for to in pre_probability
        }

        # вибираємо напрямок кроку
        choose_from, choice_probability = [], []

        for t, p in probability.items():
            choose_from.append(t)
            choice_probability.append(p)

        step_to = choice(choose_from,p=choice_probability)

        # опрацьовуємо крок
        self.path_length += g[self.vertice][step_to].length
        self.path.append((self.vertice, step_to))
        self.tabu_list.append(self.vertice)
        self.vertice = step_to

    def solve(self):
        global path, shortest_path
        while self.vertice != self.target and self.alive:
            self.step()
        if self.vertice == self.target:
            if self.path_length < shortest_path:
                shortest_path = self.path_length
                path = self.path
        if self.alive:
            for f, t in self.path:
                g[f][t].delta += .05 * g[f][t].length / self.path_length**2


n, m = 100, 100

for i in range(m):
    for j in range(n):
        ant = Ant(start="A", target="C")
        ant.solve()

    for f in g:
        for t in g[f]:
            g[f][t].feroment, g[f][t].delta =  0.7 * g[f][t].feroment + g[f][t].delta, 0

print(shortest_path, path)
