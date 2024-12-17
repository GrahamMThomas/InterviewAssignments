from abc import ABC, abstractmethod


class BaseDataProvider:
    @abstractmethod
    def pull_data(self):
        pass
