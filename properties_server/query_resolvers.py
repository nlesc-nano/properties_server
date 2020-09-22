"""Module to resolve the queries.

API
---

"""
from typing import Any, Dict, List, Optional

from tartiflette import Resolver

from properties_server.data import INGREDIENTS, RECIPES


# @Resolver("Query.jobs")
# async def resolver_query_jobs(
#     parent: Optional[Any],
#     args: Dict[str, Any],
#     ctx: Dict[str, Any],
#     info: "ResolveInfo",
# ) -> List[Dict[str, Any]]:
#     """
#     Resolver in charge of returning available jobs.

#     Parameters
#     ----------
#     paren
#         initial value filled in to the engine `execute` method
#     args
#         computed arguments related to the field
#     ctx
#         context filled in at engine initialization
#     info
#         information related to the execution and field resolution

#     Returns
#     -------
#     The list of all recipes.
#     """
#     pass


@Resolver("Query.recipes")
async def resolve_query_recipes(
    parent: Optional[Any],
    args: Dict[str, Any],
    ctx: Dict[str, Any],
    info: "ResolveInfo",
) -> List[Dict[str, Any]]:
    """
    Resolver in charge of returning all recipes.

    Parameters
    ----------
    paren
        initial value filled in to the engine `execute` method
    args
        computed arguments related to the field
    ctx
        context filled in at engine initialization
    info
        information related to the execution and field resolution

    Returns
    -------
    The list of all recipes.
    """
    return RECIPES


@Resolver("Query.recipe")
async def resolve_query_recipe(
    parent: Optional[Any],
    args: Dict[str, Any],
    ctx: Dict[str, Any],
    info: "ResolveInfo",
) -> Optional[Dict[str, Any]]:
    """
    Resolver in charge of returning a recipe depending on the filled in `id`.
    :param parent: initial value filled in to the engine `execute` method
    :param args: computed arguments related to the field
    :param ctx: context filled in at engine initialization
    :param info: information related to the execution and field resolution
    :type parent: Optional[Any]
    :type args: Dict[str, Any]
    :type ctx: Dict[str, Any]
    :type info: ResolveInfo
    :return: a recipe
    :rtype: Optional[Dict[str, Any]]
    """
    for recipe in RECIPES:
        if recipe["id"] == args["id"]:
            return recipe
    return None


@Resolver("Recipe.ingredients")
async def resolve_recipe_ingredients(
    parent: Optional[Dict[str, Any]],
    args: Dict[str, Any],
    ctx: Dict[str, Any],
    info: "ResolveInfo",
) -> Optional[List[Dict[str, Any]]]:
    """
    Resolver in charge of returning the ingredient list of a recipe.
    :param parent: the recipe for which to return the ingredients
    :param args: computed arguments related to the field
    :param ctx: context filled in at engine initialization
    :param info: information related to the execution and field resolution
    :type parent: Optional[Dict[str, Any]]
    :type args: Dict[str, Any]
    :type ctx: Dict[str, Any]
    :type info: ResolveInfo
    :return: the ingredient list of a recipe
    :rtype: Optional[List[Dict[str, Any]]]
    """
    if parent and parent["id"] in INGREDIENTS:
        return INGREDIENTS[parent["id"]]
    return None
