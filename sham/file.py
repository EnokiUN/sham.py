class File:
    content_type = "application/octet-stream"

    def __init__(self, filepath: str | bytes, filename: str = "attachment"):
        # This is amazing
        if isinstance(filepath, str):
            self.data = open(filepath, "rb").read()
        else:
            self.data = filepath
        self.filename = filename

    def to_dict(self):
        return {"value": self.data, "filename": self.filename, "content_type": self.content_type}
