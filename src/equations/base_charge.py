"""
An abstract charge, from which subclasses overload.
"""

import abc

from PyQt6 import QtCore
from sympy import Basic

from equations.constants import Point2D  # pylint: disable=import-error


class BaseCharge(abc.ABC):
    """
    An abstract charge, from which subclasses overload.
    """

    @abc.abstractmethod
    def electric_field_magnitude(self, point: Point2D) -> float:
        """
        Return the electric field magnitude generated by this charge at a given point.

        Args:
            point (Point2D): x, y location of test point.

        Returns:
            float: magnitude of electric field.
        """

    @abc.abstractmethod
    def electric_field_x(self, point: Point2D) -> float:
        """
        Calculate the x component of the magnetic field generated by the charge at a given point.

        Args:
            point (Point2D): test point to check.

        Returns:
            float: x component of electric field.
        """

    @abc.abstractmethod
    def electric_field_y(self, point: Point2D) -> float:
        """
        Calculate the y component of the magnetic field generated by the charge at a given point.

        Args:
            point (Point2D): test point to check.

        Returns:
            float: y component of electric field.
        """

    @abc.abstractmethod
    def open_menu(self, pos: QtCore.QPointF) -> bool:
        """
        Open a context menu for this charge.

        Configures options associated with the charge.

        Args:
            pos (QPointF): The location to open the menu at.

        Returns:
            bool: True if this charge should be deleted, False otherwise.
        """

    @abc.abstractmethod
    def electric_field_mag_string(self) -> Basic:
        """
        Returns the position-independent electric field equation.
        """

    @abc.abstractmethod
    def electric_field_x_string(self) -> Basic:
        """
        Returns the position-independent electric field x-component equation.
        """

    @abc.abstractmethod
    def electric_field_y_string(self) -> Basic:
        """
        Returns the position-independent electric field y-component equation.
        """
