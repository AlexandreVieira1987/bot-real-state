from src.modules.search.useCase.LoadAllLinksUseCase import LoadAllLinksUseCase
from src.modules.search.useCase.ReadLinkUseCase import ReadLinkUseCase


class SearchController():

    def execute(self):
        links = LoadAllLinksUseCase()
        read = ReadLinkUseCase()

        links.execute()
        read.execute()


    
