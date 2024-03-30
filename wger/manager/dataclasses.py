#  This file is part of wger Workout Manager <https://github.com/wger-project>.
#  Copyright (C) wger Team
#
#  wger Workout Manager is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Affero General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  wger Workout Manager is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Affero General Public License for more details.
#
#  You should have received a copy of the GNU Affero General Public License
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.


# Standard Library
import datetime
from dataclasses import (
    dataclass,
    field,
)
from decimal import Decimal
from typing import List

# wger
from wger.exercises.models import ExerciseBase


@dataclass
class SetConfigData:
    weight: Decimal | int
    reps: Decimal | int
    rir: Decimal | int
    rest: Decimal | int


@dataclass
class SetExerciseData:
    exercise: ExerciseBase
    config: 'SetConfig'
    data: SetConfigData


@dataclass
class SetData:
    set: 'SetNg'
    exercise_data: List[SetExerciseData] = field(default_factory=list)


@dataclass
class WorkoutDayData:
    day: 'DayNg'
    date: datetime.date
    iteration: int
    sets: List[SetData] = field(default_factory=list)
