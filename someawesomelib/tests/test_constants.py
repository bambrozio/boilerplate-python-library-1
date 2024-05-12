from unittest import TestCase

from someawesomelib.configuration.constants import EnvProfile


class TestConstant(TestCase):
    def test_env_profile_enum(self):
        self.assertEqual(EnvProfile["PRODUCTION"], EnvProfile.PRODUCTION)
        self.assertEqual(EnvProfile["STAGING"], EnvProfile.STAGING)
        self.assertEqual(EnvProfile["DEVELOPMENT"], EnvProfile.DEVELOPMENT)

        self.assertEqual(EnvProfile.PRODUCTION.value, "prod")
        self.assertEqual(EnvProfile.PRODUCTION.name, "PRODUCTION")
        self.assertEqual(EnvProfile.STAGING.value, "stage")
        self.assertEqual(EnvProfile.STAGING.name, "STAGING")
        self.assertEqual(EnvProfile.DEVELOPMENT.value, "dev")
        self.assertEqual(EnvProfile.DEVELOPMENT.name, "DEVELOPMENT")

        self.assertTrue(EnvProfile.has("PRODUCTION"))
        self.assertTrue(EnvProfile.has("STAGING"))
        self.assertTrue(EnvProfile.has("DEVELOPMENT"))
        self.assertFalse(EnvProfile.has("TEST"))
