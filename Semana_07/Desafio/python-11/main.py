from api.models import User, Agent, Event, Group
from datetime import date, timedelta


def get_active_users() -> User:
    """Traga todos os uarios ativos, seu último login deve ser menor que 10 dias """
    return User.objects.filter(last_login__gt=date.today() - timedelta(days=10))


def get_amount_users() -> User:
    """Retorne a quantidade total de usuarios do sistema """
    return User.objects.count()


def get_admin_users() -> User:
    """Traga todos os usuarios com grupo = 'admin"""
    return User.objects.filter(group__name="admin")


def get_all_debug_events() -> Event:
    """Traga todos os eventos com tipo debug"""
    return Event.objects.filter(level="debug")


def get_all_critical_events_by_user(agent) -> Event:
    """Traga todos os eventos do tipo critico de um usuário específico"""
    return Event.objects.filter(level="critical", agent__name=agent)


def get_all_agents_by_user(username) -> Agent:
    """Traga todos os agentes de associados a um usuário pelo nome do usuário"""
    return Agent.objects.filter(user__name=username)


def get_all_events_by_group() -> Group:
    """Traga todos os grupos que contenham alguem que possua um agente que possuem eventos do tipo information"""
    return Group.objects.filter(user__agent__event__level="information")
