# Данные о продажах
sales_data = {
    'youtube': [0, 200, 260, 317, 371, 422, 470, 515, 557, 596, 632, 665, 695, 722, 746, 767, 785, 800, 812, 821, 827],
    'facebook': [0, 100, 190, 275, 355, 430, 500, 565, 625, 680, 730, 775, 815, 850, 880, 905, 925, 940, 950, 955, 956],
    'pinterest': [0, 150, 250, 330, 394, 446, 488, 522, 551, 575, 592, 608, 621, 632, 641, 649, 656, 662, 667, 671, 675]
}

# Максимальный бюджет
max_budget = 20000
num_platforms = len(sales_data)
platforms = list(sales_data.keys())
increments = 1000

# Инициализация DP массива
dp = [[0] * (max_budget // increments + 1) for _ in range(num_platforms + 1)]

# Заполнение DP массива
for i in range(1, num_platforms + 1):
    for budget in range(max_budget // increments + 1):
        for spend in range(budget + 1):
            sales = sales_data[platforms[i - 1]][spend]
            dp[i][budget] = max(dp[i][budget], dp[i - 1][budget - spend] + sales)

# Извлечение результатов
allocations = [0] * num_platforms
budget = max_budget // increments

for i in range(num_platforms, 0, -1):
    for spend in range(budget, -1, -1):
        if dp[i][budget] == dp[i - 1][budget - spend] + sales_data[platforms[i - 1]][spend]:
            allocations[i - 1] = spend * increments
            budget -= spend
            break

# Печать результатов
platform_allocations = {platforms[i]: allocations[i] for i in range(num_platforms)}
max_sales = dp[num_platforms][max_budget // increments]

print(f"Allocations: {platform_allocations}")
print(f"Max Sales: {max_sales}")