"""Bootstrap the service superuser (admin) with id=0 and system org/division."""

from core.config import settings
from auth.auth import auth_verifier
from organizations.dao import OrganizationDAO
from divisions.dao import DivisionDAO
from users.dao import UserDAO

ADMIN_USER_ID = 0
SYSTEM_ORG_ID = 0
SYSTEM_DIVISION_ID = 0


async def ensure_system_organization() -> None:
    """Create system organization with id=0 if it does not exist."""
    existing = await OrganizationDAO.find_one_or_none(id=SYSTEM_ORG_ID)
    if existing:
        return
    await OrganizationDAO.add(id=SYSTEM_ORG_ID, name="System")


async def ensure_system_division() -> None:
    """Create system division with id=0 if it does not exist."""
    existing = await DivisionDAO.find_one_or_none(id=SYSTEM_DIVISION_ID)
    if existing:
        return
    await DivisionDAO.add(
        id=SYSTEM_DIVISION_ID,
        division=None,
        organization_id=SYSTEM_ORG_ID,
    )


async def ensure_admin_user() -> None:
    """Create service superuser with id=0 if it does not exist."""
    existing = await UserDAO.find_one_or_none(id=ADMIN_USER_ID)
    if existing:
        return
    password_hash = auth_verifier.get_password_hash(
        settings.admin.password.get_secret_value()
    )
    await UserDAO.add(
        id=ADMIN_USER_ID,
        last_name="Admin",
        first_name="System",
        patronymic=None,
        email=settings.admin.email,
        password=password_hash,
        division_id=SYSTEM_DIVISION_ID,
    )


async def run_bootstrap() -> None:
    """Ensure system organization, division, and admin user (id=0) exist."""
    await ensure_system_organization()
    await ensure_system_division()
    await ensure_admin_user()
