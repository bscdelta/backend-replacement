# ForkDelta Backend
# https://github.com/forkdelta/backend-replacement
# Copyright (C) 2018, Arseniy Ivanov and ForkDelta Contributors
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

# Eternally constant constants

BASE_ADDR = "0x0000000000000000000000000000000000000000"
BASE_ADDR_BYTES = b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'

# We might change our mind about these:
FILTER_ORDERS_UNDER_ETH = 0.001
MAX_ORDERS_PER_USER = 8

ZERO_ADDR = "0x55d398326f99059ff775485246999027b3197955"
ZERO__ADDR_BYTES = b'\55\xd3\x98\x32\x6f\x99\x05\x9f\xf7\x75\x48\x52\x46\x99\x90\x27\xb3\x19\x79\x55'