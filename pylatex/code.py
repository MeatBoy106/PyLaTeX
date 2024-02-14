# -*- coding: utf-8 -*-
"""
This module implements the class that deals with code snippets.

..  :copyright: (c) 2024 by Gabriel Busnot.
    :license: MIT, see License for more details.
"""


from .base_classes import Environment
from .utils import NoEscape
from .package import Package

class Minted(Environment):
    """A class that represents a minted listing."""

    _repr_attributes_mapping = {
        "language": "arguments",
    }

    def __init__(
        self,
        language,
        data,
        **kwargs,
    ):
        """
        Args
        ----
        language: str
            A string that represents the language used to parse the content of
            the minted environement.
        """
        
        self.packages.add(Package("minted"))

        super().__init__(
            data=data, arguments=NoEscape(language), **kwargs
        )

        # Parameter that determines if the xcolor package has been added.
        self.color = False
