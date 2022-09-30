from django.test import TestCase


# TESTING MODELS
class ProfileTests(TestCase):
    USER_DATA = {
        "first_name": "Kristian",
        "last_name": "Aleksiev",
        "age": 12,
    }

    def test_profile_full_name__when_valid__expect_correct_full_name(self):
        profile = Profile(
            first_name="Kristian",
            last_name="Aleksiev",
            age=12,
        )
        self.assertEqual("Kristian Aleksiev", profile.full_name)

    def test_profile_create__when_first_name_contains_only_letters__expect_success(self):
        profile = Profile(**self.USER_DATA)
        profile.save()
        self.assertIsNotNone(profile.pk)

    def test_profile_create__when_first_name_contains_a_digit__expect_to_fail(self):
        first_name = "Kris2"
        profile = Profile(first_name=first_name, last_name=self.USER_DATA["last_name"], age=self.USER_DATA["age"])
        with self.assertRaises(ValidationError) as context:
            profile.full_clean()
            profile.save()

        self.assertIsNotNone(context.exception)

    def test_profile_create__when_first_name_contains_a_dollar_sign__expect_to_fail(self):
        first_name = "Kri$"
        profile = Profile(first_name=first_name, last_name=self.USER_DATA["last_name"], age=self.USER_DATA["age"])
        with self.assertRaises(ValidationError) as context:
            profile.full_clean()
            profile.save()

        self.assertIsNotNone(context.exception)

    def test_profile_create__when_first_name_contains_a_space__expect_to_fail(self):
        first_name = "Kri s"
        profile = Profile(first_name=first_name, last_name=self.USER_DATA["last_name"], age=self.USER_DATA["age"])
        with self.assertRaises(ValidationError) as context:
            profile.full_clean()
            profile.save()

        self.assertIsNotNone(context.exception)

    def test_profile_create__when_first_name_contains_a_space__expect_to_fail(self):
        pass


# TESTING VIEWS - 1. Request factory(get url), 2. Test client
from django.test import TestCase


class ProfileListViewTests(TestCase):
    def test_get__expect_correct_template(self):
        # calls to views by urls
        response = self.client.get(reverse("list profiles"))  # <- Not lazy, get request to url before the template
        self.assertTemplateUsed(response, "profiles/list.html")

    def test_get__when_two_profiles__expect_context_to_contain_two_profiles(self):
        #  Arrange
        profiles_to_create = (
            Profile(first_name="Kris", last_name="X", age=23),
            Profile(first_name="Kris2", last_name="X2", age=22),
        )
        Profile.objects.bulk_create(profiles_to_create)
        # Act
        response = self.client.get(reverse("list profiles"))

        # Assert
        profiles = response.context["object_list"]
        # checking for profiles
        self.assertEqual(len(profiles), 2)

    def test_get__when_not_logged_user__expect_context_user_to_be_no_user(self):
        response = self.client.get(reverse("list profiles"))
        self.assertEqual("No user", response.context["user"])
