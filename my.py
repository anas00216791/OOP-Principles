class Illness:
    def __init__(self, name):
        self.name = name
        self.extra_info = None

    def ask_extra(self):
        pass  # Default: do nothing

    def get_medicine(self):
        return "No suggestion available"

    def get_dosage(self):
        return "Consult a doctor"

    def get_precautions(self):
        return "No general advice available"


class Fever(Illness):
    def ask_extra(self):
        self.extra_info = input("🌡️ Fever kitna hai (in °F)? ")

    def get_medicine(self):
        return "Paracetamol"

    def get_dosage(self):
        return "1 tablet every 6 hours after meals"

    def get_precautions(self):
        return f"Drink water, rest. Your fever is {self.extra_info}°F. If over 102°F, consult a doctor."


class Cold(Illness):
    def get_medicine(self):
        return "Cetirizine"

    def get_dosage(self):
        return "1 tablet at night for 3 days"

    def get_precautions(self):
        return "Avoid cold drinks, keep warm, drink herbal tea"


class Headache(Illness):
    def get_medicine(self):
        return "Ibuprofen"

    def get_dosage(self):
        return "1 tablet every 8 hours"

    def get_precautions(self):
        return "Reduce screen time, rest, avoid loud noise"


class Cough(Illness):
    def get_medicine(self):
        return "Benadryl syrup"

    def get_dosage(self):
        return "2 teaspoons every 6 hours"

    def get_precautions(self):
        return "Avoid cold drinks, use warm water for drinking"


class StomachPain(Illness):
    def get_medicine(self):
        return "Buscopan"

    def get_dosage(self):
        return "1 tablet after meals, 2 times a day"

    def get_precautions(self):
        return "Avoid spicy food, drink warm water"


class Diarrhea(Illness):
    def get_medicine(self):
        return "ORS + Loperamide"

    def get_dosage(self):
        return "ORS after every stool + 1 Loperamide if needed"

    def get_precautions(self):
        return "Stay hydrated, eat light food, avoid dairy"


class SoreThroat(Illness):
    def get_medicine(self):
        return "Strepsils or Salt Water Gargle"

    def get_dosage(self):
        return "1 lozenge every 4 hours or gargle 2–3 times/day"

    def get_precautions(self):
        return "Avoid cold items, talk less, drink warm fluids"


class Cancer(Illness):
    def get_medicine(self):
        return "Consult oncologist"

    def get_dosage(self):
        return "Based on stage and diagnosis"

    def get_precautions(self):
        return "Eat clean, avoid smoking/alcohol, follow up regularly"


class BloodPressure(Illness):
    def ask_extra(self):
        self.extra_info = input("🩺 Aap ka blood pressure aam tor par kitna rehta hai (e.g., 140/90)? ")

    def get_medicine(self):
        return "Amlodipine or as prescribed"

    def get_dosage(self):
        return "1 tablet daily in the morning"

    def get_precautions(self):
        return f"Your BP: {self.extra_info}. Reduce salt, monitor BP, exercise daily."


class Sugar(Illness):
    def ask_extra(self):
        self.extra_info = input("🩸 Sugar reading kya aayi thi (e.g., 180 mg/dL)? ")

    def get_medicine(self):
        return "Metformin or Insulin (based on level)"

    def get_dosage(self):
        return "As prescribed by a doctor"

    def get_precautions(self):
        return f"Your sugar level: {self.extra_info}. Avoid sugar, walk daily, monitor glucose."


class HealthApp:
    def __init__(self):
        self.illnesses = {
            1: ("Fever", Fever("Fever")),
            2: ("Cold", Cold("Cold")),
            3: ("Headache", Headache("Headache")),
            4: ("Cough", Cough("Cough")),
            5: ("Stomach Pain", StomachPain("Stomach Pain")),
            6: ("Diarrhea", Diarrhea("Diarrhea")),
            7: ("Sore Throat", SoreThroat("Sore Throat")),
            8: ("Cancer", Cancer("Cancer")),
            9: ("Blood Pressure", BloodPressure("Blood Pressure")),
            10: ("Sugar", Sugar("Sugar"))
        }

    def show_menu(self):
        print("\n🔢 Please select your illness:")
        for key, (name, _) in self.illnesses.items():
            print(f"{key}. {name}")

    def suggest_treatment(self, choice):
        illness_data = self.illnesses.get(choice)
        if not illness_data:
            print("❌ Invalid choice. Please try again.")
            return

        name, illness = illness_data
        illness.ask_extra()
        print("\n💊 Health Suggestions:")
        print(f"🔹 Illness: {name}")
        print(f"🔹 Recommended Medicine: {illness.get_medicine()}")
        print(f"🔹 Dosage: {illness.get_dosage()}")
        print(f"🔹 Precautions: {illness.get_precautions()}")


# CLI Loop
def main():
    print("🩺 Welcome to the Health Suggestion App")
    app = HealthApp()

    while True:
        app.show_menu()
        try:
            choice = int(input("Enter the number of your illness (or 0 to exit): "))
            if choice == 0:
                print("👋 Stay healthy! Goodbye.")
                break
            app.suggest_treatment(choice)
        except ValueError:
            print("❗ Please enter a valid number.")


if __name__ == "__main__":
    main()
