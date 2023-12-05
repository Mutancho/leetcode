class ATM:
    def __init__(self):
        self.bank_notes = {20: 0, 50: 0, 100: 0, 200: 0, 500: 0}

    def deposit(self, banknotesCount: list[int]) -> None:
        for i, bank_note in enumerate(self.bank_notes):
            self.bank_notes[bank_note] += banknotesCount[i]

    def __str__(self):
        return " | ".join([str(kv) for kv in self.bank_notes.items()])

    def withdraw(self, amount: int) -> list[int]:
        bank_note_copy = self.bank_notes.copy()
        output = [0] * len(self.bank_notes)

        for i, note_value in enumerate(reversed(self.bank_notes.keys())):
            if bank_note_copy[note_value] and amount >= note_value:
                required_number_of_notes = amount // note_value
                available_notes = min(required_number_of_notes, bank_note_copy[note_value])
                amount -= note_value * available_notes
                bank_note_copy[note_value] -= available_notes
                output[i] += available_notes

        if amount == 0:
            self.bank_notes = bank_note_copy
            return output[::-1]
        else:
            return [-1]


