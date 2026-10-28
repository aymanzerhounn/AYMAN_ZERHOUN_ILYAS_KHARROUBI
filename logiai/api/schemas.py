"""Les fiches techniques (schémas Pydantic) de l'API LogiAI."""
from pydantic import BaseModel, Field
from typing import Literal

class Livraison(BaseModel):
    class Config:
        extra = "forbid"  # <--- Notez bien "forbid" au lieu de "forbidden" avec Config classique

    distance_km: float = Field(..., gt=0, description="Distance du trajet en kilomètres")
    poids_kg: float = Field(..., ge=0, le=10000, description="Poids transporté en kg")
    heure_depart: int = Field(..., ge=0, le=23, description="Heure de départ (0-23)")
    pluie_mm: float = Field(..., ge=0, le=100, description="Quantité de pluie (mm)")
    trafic_index: float = Field(..., ge=0, le=10, description="Indice de trafic (0-10)")
    nb_arrets: int = Field(..., ge=0, le=50, description="Nombre d'arrêts prévus")
    type_vehicule: Literal["moto", "fourgon", "camion"] = Field(..., description="Type de véhicule")

class PredictionOut(BaseModel):
    probabilite_retard: float = Field(ge=0, le=1, description="Probabilité que la livraison soit en retard")
    alerte: bool = Field(description="True si la probabilité atteint le seuil")
    seuil: float = Field(description="Seuil d'alerte utilisé")
    model_version: str = Field(description="Version du modèle")
