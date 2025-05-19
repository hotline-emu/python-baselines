from invoke.tasks import task
from invoke.context import Context


@task
def flake8(context: Context) -> None:
    context.run("flake8 .")


@task
def pylint(context: Context) -> None:
    context.run("pylint .")


@task
def mypy(context: Context) -> None:
    context.run("mypy .")


@task(
    flake8,
    pylint,
    mypy,
)
def lint(_context: Context) -> None: ...
