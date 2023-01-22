from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Protocol, TYPE_CHECKING


if TYPE_CHECKING:
    from .intervals import AnyInterval
    from .nexus import TheUserModel
    from .intention import Intention


class IntervalType(Enum):
    """
    The type of a given interval.
    """

    Pomodoro = "Pomodoro"
    GracePeriod = "GracePeriod"
    Break = "Break"
    StartPrompt = "StartPrompt"


class PomStartResult(Enum):

    Started = "Started"
    """
    The pomodoro was started, and with it, a new streak was started.
    """

    Continued = "Continued"
    """
    A pomodoro was started, and with it, an existing streak was continued.
    """

    OnBreak = "OnBreak"
    AlreadyStarted = "AlreadyStarted"
    """
    The pomodoro could not be started, either because we were on break, or
    because another pomodoro was already running.
    """


class AnUserInterface(Protocol):
    """
    Protocol that user interfaces must adhere to.
    """

    def intervalStart(self, interval: AnyInterval) -> None:
        """
        Set the interval type to "pomodoro".
        """

    def intervalProgress(self, percentComplete: float) -> None:
        """
        The active interval has progressed to C{percentComplete} percentage
        complete.
        """

    def intervalEnd(self) -> None:
        """
        The interval has ended. Hide the progress bar.
        """

    def intentionAdded(self, intention: Intention) -> None:
        """
        An intention was added to the set of intentions.
        """

    def intentionAbandoned(self, intention: Intention) -> None:
        """
        An intention was removed from the set of intentions by the user.
        """

    def intentionCompleted(self, intention: Intention) -> None:
        """
        An intention was marked as completed, so it is no longer available for
        selection for new pomodoros by the user.
        """


@dataclass
class NoUserInterface(AnUserInterface):
    """
    Do-nothing implementation of a user interface.
    """


class UserInterfaceFactory(Protocol):
    """
    Entry point to a frontend that creates a user interface from a user model
    """

    def __call__(self, model: TheUserModel) -> AnUserInterface:
        ...  # pragma: no cover


class EvaluationResult(Enum):
    """
    How did a given Pomodoro go?
    """

    points: float

    distracted = "distracted"
    """
    The user was distracted by something that they could have had control over,
    and ideally would have ignored or noted for later.
    """

    interrupted = "interrupted"
    """
    The user was interrupted by something that was legitimately higher priority
    than their specified intention.
    """

    focused = "focused"
    """
    The user was focused on the task at hand.
    """

    achieved = "achieved"
    """
    The intended goal of the pomodoro was achieved.
    """


EvaluationResult.distracted.points = 0.1
EvaluationResult.interrupted.points = 0.2
EvaluationResult.focused.points = 1.0
EvaluationResult.achieved.points = 1.25


class ScoreEvent(Protocol):
    """
    An event that occurred that affected the users score.
    """

    @property
    def points(self) -> float:
        """
        The number of points awarded to this event.
        """

    @property
    def time(self) -> float:
        """
        The point in time where this scoring event occurred.
        """