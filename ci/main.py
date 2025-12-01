import sys

import anyio
import dagger


async def main():
    config = dagger.Config(log_output=sys.stdout)

    # initialize Dagger client
    async with dagger.Connection(config) as client:
        # use a python:3.11-slim container
        # get version
        python = (
            client.container()
            .from_("python:3.11-slim")
            .with_exec(["python", "-V"])
            .with_workdir("/src")
        )

        notifier = (
            client.container()
            .from_("python:3.11-slim")
            .with_exec(
                [
                    "apt",
                    "update",
                    "-y",
                ]
            )
            .with_exec(
                [
                    "apt",
                    "install",
                    "-y",
                    "curl",
                ]
            )
        )

        source = python.with_file(
            "requirements.txt",
            client.host().file("requirements.txt"),
        )
        # set the working directory in the container
        # install application dependencies
        runner = source.with_exec(["pip", "install", "-r", "requirements.txt"])

        builder = runner.with_directory(
            "/src",
            client.host().directory("."),
            exclude=[
                "ci",
                "markout",
                ".venv",
                ".markata.cache",
                ".mypy_cache",
            ],
        ).with_exec(
            ["python", "-m", "markata", "build"],
        )

        notifier = notifier.with_exec(
            [
                "curl",
                "-d",
                "finished building waylonwalker.com",
                "https://ntfy.wayl.one/deployments",
            ]
        )

        # execute
        version = await python.stdout()
        output = await runner.stdout()
        build = await builder.stdout()
        notify = await notifier.stdout()

    # print output
    print(f"Hello from Dagger and {version}")


anyio.run(main)
