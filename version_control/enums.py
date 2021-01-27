from enum import Enum


class TaskStatus(Enum):

    TO_DO = "IN"
    IN_PROGRESS = "IN_PROGRESS"
    IN_REVIEW = "IN_REVIEW"
    DONE = "DONE"
    ARCHIVED = "ARCHIVED"


    @classmethod
    def choices(cls):
        print(tuple((i.name, i.value) for i in cls))
        return tuple((i.name, i.value) for i in cls)
