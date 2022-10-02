from dependency_injector import containers, providers

from .repository import TaskRepository, UserRepository
from .service import TaskService, UserService


class Repositories(containers.DeclarativeContainer):
    tasks_repository = providers.Singleton(TaskRepository)
    users_repository = providers.Singleton(UserRepository)


class Services(containers.DeclarativeContainer):
    repositories: Repositories = providers.DependenciesContainer()
    tasks_service = providers.Factory(
        TaskService, repository=repositories.tasks_repository
    )
    users_service = providers.Factory(
        UserService, repository=repositories.users_repository
    )


class Application(containers.DeclarativeContainer):
    repositories: Repositories = providers.Container(Repositories)
    services: Services = providers.Container(Services, repositories=repositories)
