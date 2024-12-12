import inject 

from students.infrastructure.adapters import AdaStudents
from students.domain.interfaces import IStudents


def configure_inject()->None:
    def config(binder: inject.Binder) -> None:
        binder.bind(IStudents,AdaStudents)

    if not inject.is_configured():
        inject.configure_once(inject.configure(config))