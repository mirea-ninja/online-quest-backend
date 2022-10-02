from dependency_injector import containers, providers

# from .repository import
# from .service import


class Repositories(containers.DeclarativeContainer):
    # stories_repository = providers.Singleton(StoriesRepository)]
    pass


class Services(containers.DeclarativeContainer):
    repositories = providers.DependenciesContainer()

    # stories_service = providers.Factory(
    #     StoriesService, repository=repositories.stories_repository
    # )


class Application(containers.DeclarativeContainer):
    repositories = providers.Container(Repositories)
    services = providers.Container(Services, repositories=repositories)
