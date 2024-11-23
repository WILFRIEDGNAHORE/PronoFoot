from datetime import datetime
from django.utils.timezone import now
from django.contrib.sessions.models import Session

class ActiveUsersMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response  # Nécessaire pour exécuter le prochain middleware ou la vue

    def __call__(self, request):
        # Enregistrer l'activité pour les utilisateurs authentifiés
        if request.user.is_authenticated:
            request.session['last_activity'] = now()

        # Passer la requête au middleware suivant ou à la vue
        response = self.get_response(request)
        return response

    @staticmethod
    def get_total_active_sessions():
        """
        Compte toutes les sessions actives (connectées et anonymes).
        """
        sessions = Session.objects.filter(expire_date__gte=now())
        return sessions.count()

    @staticmethod
    def get_active_authenticated_user_count():
        """
        Compte uniquement les utilisateurs connectés.
        """
        sessions = Session.objects.filter(expire_date__gte=now())
        active_user_count = 0
        for session in sessions:
            data = session.get_decoded()
            if '_auth_user_id' in data:
                active_user_count += 1
        return active_user_count

    @staticmethod
    def get_active_anonymous_user_count():
        """
        Compte uniquement les utilisateurs anonymes (non connectés).
        """
        total_sessions = ActiveUsersMiddleware.get_total_active_sessions()
        authenticated_users = ActiveUsersMiddleware.get_active_authenticated_user_count()
        return total_sessions - authenticated_users
