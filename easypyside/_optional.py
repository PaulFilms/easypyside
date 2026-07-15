'''
Optional imports

Include:
    - pandas
    - mardown
'''

def pandas():
    try:
        import pandas as pd
        return pd
    except ImportError as e:
        raise ImportError(
            "Pandas support is optional.\n"
            "Install it with:\n\n"
            "    pip install easypyside[pandas]"
        ) from e


def markdown2():
    try:
        import markdown2
        return markdown2
    except ImportError as e:
        raise ImportError(
            "Markdown support is optional.\n"
            "Install it with:\n\n"
            "    pip install easypyside[markdown]"
        ) from e