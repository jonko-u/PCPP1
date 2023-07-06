import textwrap


class Frame:
    def __init__(self, text, width=20, border="*", padding=" "):
        self.text = text
        self.width = width
        self.border = border
        self.padding = padding

    def draw(self):
        # Wrap the text to fit within the framepackage
        wrapped_text = textwrap.wrap(self.text, width=self.width-4)

        # Calculate the height of the framepackage
        height = len(wrapped_text) + 2

        # Calculate the top and bottom padding for the framepackage
        top_padding = self.padding * ((height - len(wrapped_text) - 2) // 2)
        bottom_padding = self.padding * ((height - len(wrapped_text) - 2) // 2 + (height - len(wrapped_text) - 2) % 2)

        # Draw the top border of the framepackage
        frame = self.border * self.width + "\n"

        # Draw the top padding of the framepackage
        for i in range((height - len(wrapped_text) - 2) // 2):
            frame += self.border + self.padding * (self.width - 2) + self.border + "\n"

        # Draw the middle section of the framepackage
        for line in wrapped_text:
            left_padding = self.padding * ((self.width - len(line) - 2) // 2)
            right_padding = self.padding * ((self.width - len(line) - 6) // 2 + (self.width - len(line) - 2) % 2)
            frame += self.border + left_padding + " " + line + " " + right_padding + self.border + "\n"

        # Draw the bottom padding of the framepackage
        for i in range((height - len(wrapped_text) - 2) // 2):
            frame += self.border + self.padding * (self.width - 2) + self.border + "\n"

        # Draw the bottom border of the framepackage
        frame += self.border * self.width

        return frame