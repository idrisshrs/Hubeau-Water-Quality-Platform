import os

import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    raise RuntimeError(
        "DATABASE_URL is not configured. Copy .env.example to .env and provide a local PostgreSQL URL."
    )

engine = create_engine(DATABASE_URL)


def fct_condition(filtres: dict):
    conditions = []
    params = []
    for cle, valeur in filtres.items():
        if valeur:
            conditions.append(f"{cle} = %s")
            params.append(valeur)
    return " AND ".join(conditions), tuple(params)


def obtenir_valeurs_distinctes(table, colonne):
    requete = f"""
    SELECT DISTINCT
        {colonne}
    FROM
        {table}
    """
    resultat = pd.read_sql_query(requete, engine)
    return resultat.to_dict(orient='records')


def obtenir_donnees_filtrees(table, colonnes, jointures, filtres) -> pd.DataFrame:
    condi_where, params = fct_condition(filtres)
    requete = f"""
    SELECT
        {', '.join(colonnes)}
    FROM
        {table}
    {jointures}
    WHERE
        {condi_where};
    """
    return pd.read_sql_query(requete, engine, params=tuple(params))


def obtenir_donnees(table, colonnes, jointures) -> pd.DataFrame:
    requete = f"""
    SELECT
        {', '.join(colonnes)}
    FROM
        {table}
    {jointures}
    """
    return pd.read_sql_query(requete, engine)


def obtenir_info_ouvrage(filtres=None):
    table = "ouvrages"
    colonnes = [
        'ouvrages.code_ouvrage',
        'ouvrages.nom_ouvrage',
        'ouvrages.date_exploitation_debut',
        'ouvrages.date_exploitation_fin',
        'ouvrages.code_type_milieu',
        'departement.libelle_departement',
        'ouvrages.longitude',
        'ouvrages.latitude',
        'ouvrages.code_departement'
    ]
    jointures = """
    INNER JOIN departement ON departement.code_departement = ouvrages.code_departement
    """
    return obtenir_donnees_filtrees(table, colonnes, jointures, filtres) if filtres else obtenir_donnees(table, colonnes, jointures)


def obtenir_info_prelevement(filtres=None):
    table = "pt_prelevement"
    colonnes = [
        'pt_prelevement.code_point_prelevement',
        'pt_prelevement.code_ouvrage',
        'pt_prelevement.nom_point_prelevement',
        'pt_prelevement.date_exploitation_debut',
        'pt_prelevement.code_type_milieu',
        'pt_prelevement.libelle_nature',
        'pt_prelevement.code_departement',
        'departement.libelle_departement'
    ]
    jointures = """
    INNER JOIN departement ON departement.code_departement = pt_prelevement.code_departement
    """
    return obtenir_donnees_filtrees(table, colonnes, jointures, filtres) if filtres else obtenir_donnees(table, colonnes, jointures)


def obtenir_info_commune(filtres=None):
    table = "commune"
    colonnes = [
        'commune.nom_commune',
        'commune.code_commune_insee',
        'commune.code_departement'
    ]
    jointures = """
    INNER JOIN departement ON departement.code_departement = commune.code_departement
    """
    return obtenir_donnees_filtrees(table, colonnes, jointures, filtres) if filtres else obtenir_donnees(table, colonnes, jointures)


def obtenir_info_departement(filtres=None):
    table = "departement"
    colonnes = [
        "departement.code_departement",
        "departement.libelle_departement",
    ]
    jointures = ""
    return obtenir_donnees_filtrees(table, colonnes, jointures, filtres) if filtres else obtenir_donnees(table, colonnes, jointures)
