from src.modules.search.useCase.LoadAllLinksUseCase import LoadAllLinksUseCase
from src.modules.search.useCase.ReadLinksUseCase import ReadLinksUseCase


class SearchController():

    def execute(self):
        links = LoadAllLinksUseCase()
        # read = ReadLinksUseCase()

        links.execute()
        # read.execute()


    
