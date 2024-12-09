# Данные о продажах и доходности
sales_data = {
    'youtube': [0, 200, 260, 317, 371, 422, 470, 515, 557, 596, 632, 665, 695, 722, 746, 767, 785, 800, 812, 821, 827],
    'facebook': [0, 100, 190, 275, 355, 430, 500, 565, 625, 680, 730, 775, 815, 850, 880, 905, 925, 940, 950, 955, 956],
    'pinterest': [0, 150, 250, 330, 394, 446, 488, 522, 551, 575, 592, 608, 621, 632, 641, 649, 656, 662, 667, 671, 675]
}

# Параметры задачи
max_budget = 20000
revenue_per_sale = 15
increments = 1000

# Количество возможных шагов бюджета
budget_steps = max_budget // increments + 1

# Инициализация таблицы DP
dp = [[0] * budget_steps for _ in range(len(sales_data) + 1)]

platforms = list(sales_data.keys())

# Заполнение таблицы DP
for i in range(1, len(platforms) + 1):
    for budget in range(budget_steps):
        max_profit = dp[i - 1][budget]
        for spend in range(budget + 1):
            sales = sales_data[platforms[i - 1]][spend]
            profit = sales * revenue_per_sale - spend * increments
            if budget - spend >= 0:
                max_profit = max(max_profit, dp[i - 1][budget - spend] + profit)
        dp[i][budget] = max_profit

# Извлечение оптимального распределения бюджета
allocations = [0] * len(platforms)
budget = budget_steps - 1

for i in range(len(platforms), 0, -1):
    for spend in range(budget + 1):
        sales = sales_data[platforms[i - 1]][spend]
        if dp[i][budget] == dp[i - 1][budget - spend] + sales * revenue_per_sale - spend * increments:
            allocations[i - 1] = spend * increments
            budget -= spend
            break

# Вывод результатов
platform_allocations = {platforms[i]: allocations[i] for i in range(len(platforms))}
max_profit = dp[len(platforms)][budget_steps - 1]

print(f"Allocations: {platform_allocations}")
print(f"Max Profit: {max_profit}")