class Project:
    """Represent information about a guitar."""

    def __init__(self, name, start_date, priority, estimate, completion):
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.estimate = estimate
        self.completion = completion

    def __str__(self):
        """Return string representation of a guitar."""
        return f'{self.name}, start: {self.start_date}, priority {self.priority}, estimate: ${self.estimate:.2f}' \
               f', completion: {self.completion}%'

    def is_complete(self):
        return self.completion > 99





