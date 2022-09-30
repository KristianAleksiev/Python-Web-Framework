"""
1. Unit vs Integration testing
- Units -> Specific piece of code
- Integration -> Coupled pieces of code

2. Best practices
- If it can break, it should be tested
- One function or flow
- Arrange, Act Assert
- Test everything without the django code, all the custom behavior

3. Structure
- tests.py -> app level or package tests / package views , package models etc. (a file per view)

4. Testing Django components

class ProfileTests(TestCase):
    def test_profile_full_name__when_valid__expect_correct_full_name(self):
        profile = Profile(
            first_name="Kristian",
            last_name="Aleksiev",
            age=12,
        )
        self.assertEqual("Kristian Aleksiev", profile.full_name)

- When testing Models, need to call full_clean - p = Profile(), p.full_clean()

"""