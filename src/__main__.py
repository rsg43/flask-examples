from argparse import ArgumentParser


parser = ArgumentParser(description="A simple command-line tool.")
parser.add_argument(
    "service",
    type=str,
    help="The service to run. Options: 'normal', 'async'.",
)
args = parser.parse_args()

if args.service == "normal":
    from src.api import WebAPI

    with WebAPI() as app:
        app.run()

elif args.service == "async":
    from src.async_api import AsyncWebAPI

    with AsyncWebAPI() as app:
        app.run()

else:
    raise ValueError(
        f"Invalid service '{args.service}'. Options are 'normal' or 'async'."
    )
