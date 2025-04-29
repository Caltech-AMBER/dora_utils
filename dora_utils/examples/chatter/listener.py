from dora_utils.node import DoraNode, on_event


class Listener(DoraNode):
    """Simple publisher node for a Dora tutorial."""

    @on_event("INPUT", "speech")
    def listen(self, event: dict) -> None:
        message = event["value"][0].as_py()
        print(f"""I heard {message} from {event["id"]}""")
