# -*- coding: utf-8 -*-
#
# Copyright © 2015 Hasan Yavuz Özderya
#
# This file is part of ecad-3d-model-generator.
#
# ecad-3d-model-generator is free software: you can redistribute it
# and/or modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation, either version 3 of
# the License, or (at your option) any later version.
#
# ecad-3d-model-generator is distributed in the hope that it will be
# useful, but WITHOUT ANY WARRANTY; without even the implied warranty
# of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with ecad-3d-model-generator.  If not, see
# <http://www.gnu.org/licenses/>.

from e3dmg.generators.dip import DIPGen

DIP08 = DIPGen(
    D = 9.27,   # package length
    E1 = 6.35,  # package width
    E = 7.874,  # shoulder to shoulder width (includes pins)
    A1 = 0.38,  # base to seating plane
    A2 = 3.3,   # package height

    b1 = 1.524, # upper lead width
    b = 0.457,  # lower lead width
    e = 2.54,   # pin to pin distance

    npins = 8  # total number of pins
)
