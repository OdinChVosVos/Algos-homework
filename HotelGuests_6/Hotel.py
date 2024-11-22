class Hotel:
    def __init__(self):
        self.events = []

    def book_dates(self, check_in, check_out):

        self.events.append((check_in, 1))
        self.events.append((check_out, -1))

    def get_max_visitors_day(self):
        # Sort events by date; if dates are the same, end event (-1) comes first
        self.events.sort(key=lambda x: (x[0], x[1]))

        max_visitors = 0
        current_visitors = 0
        max_day = None

        # Sweep through events
        for date, change in self.events:
            current_visitors += change
            if current_visitors > max_visitors:
                max_visitors = current_visitors
                max_day = date

        return max_day, max_visitors
