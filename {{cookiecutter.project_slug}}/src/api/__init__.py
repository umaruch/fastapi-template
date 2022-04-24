from src.api.endpoints import auth


"""
    Пользовательские роутеры записывать в словарь в формате:
    url: роутер
"""
routers = {
    "/auth": auth.router
}