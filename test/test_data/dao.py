from posixpath import abspath, dirname
import sys

from dao_base import BaseDAO

sys.path.insert(0, dirname(dirname(dirname(abspath(__file__)))))
sys.path.insert(0, dirname(dirname(dirname(abspath(__file__)))) + "/app")

from organizations.models import Organization
from divisions.models import Division
from users.models import User
from projects.models import Project
from activity_types.models import ActivityType
from tasks.models import Task


class OrganizationDAO(BaseDAO):
    model = Organization


class DivisionDAO(BaseDAO):
    model = Division


class UserDAO(BaseDAO):
    model = User


class ActivityTypeDAO(BaseDAO):
    model = ActivityType


class ProjectDAO(BaseDAO):
    model = Project


class TaskDAO(BaseDAO):
    model = Task
