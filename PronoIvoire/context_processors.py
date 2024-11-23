from .middleware import ActiveUsersMiddleware

def active_users(request):
    """
    Ajoute le nombre total de sessions actives (utilisateurs connectés et anonymes) au contexte.
    """
    active_user_count = ActiveUsersMiddleware.get_total_active_sessions()  # Méthode pour obtenir le total des sessions actives
    return {
        'active_user_count': active_user_count,
    }
