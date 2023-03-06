from src.modules.search.useCase.LoadAllLinksUseCase import LoadAllLinksUseCase


class SearchController():

    def execute(self):
        links = LoadAllLinksUseCase()

        links.execute()


    
