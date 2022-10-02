from dependency_injector import containers, providers

from .repository import TaskRepository
from .service import TaskService


class Repositories(containers.DeclarativeContainer):
    tasks_repository = providers.Singleton(TaskRepository)
    pass


class Services(containers.DeclarativeContainer):
    repositories = providers.DependenciesContainer()
    tasks_service = providers.Factory(
        TaskService, repository=repositories.tasks_repository
    )


class Application(containers.DeclarativeContainer):
    repositories = providers.Container(Repositories)
    services = providers.Container(Services, repositories=repositories)
