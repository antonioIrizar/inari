from unittest import mock

from django.test import TestCase

from .. import factories
from .. import permissions


class IsGameInProgressTest(TestCase):
    def test_has_permission(self):
        game = factories.GameFactory()
        permission = permissions.IsGameInProgress()

        self.assertTrue(permission.has_permission(request=mock.MagicMock(), view=mock.MagicMock(game=game)))

    def test_has_not_permission(self):
        game = factories.GameFactory(not_in_progress=True)
        permission = permissions.IsGameInProgress()

        self.assertFalse(permission.has_permission(request=mock.MagicMock(), view=mock.MagicMock(game=game)))
