from dependency_injector import containers, providers

from .repository import AnswerRepository, UserRepository
from .service import AnswerService, TaskService, TelegramLoggerService, UserService


class Repositories(containers.DeclarativeContainer):
    answers_repository = providers.Singleton(AnswerRepository)
    users_repository = providers.Singleton(UserRepository)


class Services(containers.DeclarativeContainer):
    repositories: Repositories = providers.DependenciesContainer()
    users_service = providers.Factory(
        UserService, repository=repositories.users_repository
    )
    telegram_logger_service = providers.Factory(TelegramLoggerService)
    answers_service = providers.Factory(
        AnswerService,
        repository=repositories.answers_repository,
        users_service=users_service,
        telegram_logger_service=telegram_logger_service,
    )
    tasks_service = providers.Factory(
        TaskService,
        users_service=users_service,
        repository=repositories.answers_repository,
    )


class Application(containers.DeclarativeContainer):
    repositories: Repositories = providers.Container(Repositories)
    services: Services = providers.Container(Services, repositories=repositories)
