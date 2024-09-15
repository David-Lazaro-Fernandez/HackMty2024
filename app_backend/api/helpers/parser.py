"""
Parser module for parsing the request data
"""
import srt

def parse_srt(srt_text: str) -> list:
    """
    This function parses the srt text and returns a text string
    """
    data = srt.parse(srt_text)
    parsed_data = [{
        "content": sub.content,
        "start": sub.start.total_seconds(),
        "end": sub.end.total_seconds()
    } for sub in data]

    return parsed_data