from invoke.tasks import task
from invoke.context import Context

DISABLE_WARNING = "set PYTHONWARNINGS=ignore::DeprecationWarning"


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


@task
def run(context: Context) -> None:
    run_script = "python src/source.py"
    context.run(f"{DISABLE_WARNING} && {run_script}")


@task
def test(context: Context) -> None:
    context.run(f"{DISABLE_WARNING} && pytest")


@task
def coverage(context: Context) -> None:
    coverage_script = "pytest --cov=src --cov-report=html --cov-report=term-missing"
    context.run(f"{DISABLE_WARNING} && {coverage_script}")
