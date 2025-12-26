from abc import ABC, abstractmethod
from typing import Generic, TypeVar, List, Any, Optional
from pydantic import BaseModel

T = TypeVar("T", bound=BaseModel)

class DAOInterface(Generic[T], ABC):
    """
    Interface générique pour un DAO.
    - T est le type du modèle (ex : ProjectModel).
    - Les id sont typés Any pour rester simple; tu peux remplacer par int | str | UUID selon ton projet.
    """

    @abstractmethod
    def find_all(self) -> List[T]:
        """Retourne toutes les instances de T."""
        raise NotImplementedError

    @abstractmethod
    def find_by_id(self, id: Any) -> Optional[T]:
        """Retourne une instance par son id ou None si introuvable."""
        raise NotImplementedError

    @abstractmethod
    def create(self, item: T) -> T:
        """Crée une nouvelle instance et la retourne (avec id si applicable)."""
        raise NotImplementedError

    @abstractmethod
    def create_all(self, items: List[T]) -> T:
        """Crée une nouvelle instance et la retourne (avec id si applicable)."""
        raise NotImplementedError

    @abstractmethod
    def update(self, id: Any, item: T) -> Optional[T]:
        """
        Met à jour l'entité identifiée par id avec les données d'item.
        Retourne l'entité mise à jour, ou None si l'entité n'existe pas.
        """
        raise NotImplementedError

    @abstractmethod
    def update_all(self, ids: List[Any], items: List[T]) -> Optional[T]:
        """
        Met à jour l'entité identifiée par id avec les données d'item.
        Retourne l'entité mise à jour, ou None si l'entité n'existe pas.
        """
        raise NotImplementedError

    @abstractmethod
    def delete(self, id: Any) -> bool:
        """
        Supprime l'entité identifiée par id.
        Retourne True si suppression réussie, False si l'entité n'existait pas.
        """
        raise NotImplementedError

    @abstractmethod
    def delete_all(self, ids: List[Any]) -> bool:
        """
        Supprime l'entité identifiée par id.
        Retourne True si suppression réussie, False si l'entité n'existait pas.
        """
        raise NotImplementedError
    
    @abstractmethod
    def get_total(self)-> int:
        """
        Cette methode permet de count le nombre d'enregistrement de l'entite dans la base de donnees
        
        :param self: Description
        :return: Description
        :rtype: int
        """
        raise NotImplementedError
