class WCTool:
    def __init__(self, file_path):
        self.file_path = file_path
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                self.content = file.read()
        except FileNotFoundError:
            print(f"File not found: {file_path}")
            raise

    def byte_count(self):
        return len(self.content.encode('utf-8'))

    def word_count(self, delimiter=' '):
        words = self.content.split(delimiter)
        return len([word for word in words if word.strip()])

    def line_count(self):
        return len(self.content.splitlines())

    def char_count(self):
        return len(self.content)
