from src.api.v1.openapi.base import BaseOpenapi

signup = BaseOpenapi(
    summary='Регистрация',
    description=('Регистрирует пользователя с предоставленными регистрационными '
                 'данными. Проверка сложности пароля не производится. На длину '
                 'полей наложены ограничения: от 3 до 30 символов.'),
    response_description='Данные вновь созданного пользователя'
)

login = BaseOpenapi(
    summary='Вход',
    description=('Авторизует ранее зарегистрированного пользователя по логину '
                 'и паролю.'),
    response_description='Пара access и refresh токенов'
)

logout = BaseOpenapi(
    summary='Выход',
    description=('Завершает текущую сессию.'),
    response_description=''
)

logout_others = BaseOpenapi(
    summary='Выход на других устройствах',
    description=('Завершает все сессии, кроме текущей.'),
    response_description=''
)

refresh = BaseOpenapi(
    summary='Обновление токенов',
    description=('Продлевает текущую сессию.'),
    response_description='Пара access и refresh токенов'
)

login_with_external_account = BaseOpenapi(
    summary='Вход с помощью стороннего сервиса',
    description=('Вход осуществялется только после перехода пользователем по '
                 'ссылке, полученной от эндпоинта и одобрения доступа '
                 'приложения к пользовательским данным. Полученный от OAuth '
                 'сервиса аутентификации код, должен быть введён в поле code '
                 'для получения access и refresh токенов'),
    response_description=('Ссылка для разрешения доступа приложения к учетным '
                          'данным пользователя в другом сервисе ИЛИ пара '
                          'access и refresh токенов')
)

link_external_account = BaseOpenapi(
    summary='Привязка стороннего сервиса к своему аккаунту',
    description=('Привязка осуществялется только после перехода пользователем '
                 'по ссылке, полученной от эндпоинта и одобрения доступа '
                 'приложения к пользовательским данным. Полученный от OAuth '
                 'сервиса аутентификации код, должен быть введён в поле code '
                 'для успешной привязки аккаунта'),
    response_description=('Ссылка для разрешения доступа приложения к учетным '
                          'данным пользователя в другом сервисе ИЛИ сообщение '
                          'об успешной привязке аккаунта')
)
