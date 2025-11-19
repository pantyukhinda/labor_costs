from typing import List
from fastapi import APIRouter, HTTPException, status

from app.schemes.project import (
    ProjectCreate,
    ProjectUpdate,
    ProjectResponse,
)
from app.dao.project import ProjectDAO


router = APIRouter(prefix="/project", tags=["project"])


@router.post(
    "/add",
    response_model=ProjectResponse,
    status_code=status.HTTP_201_CREATED,
)
async def create_project(project: ProjectCreate):
    """Create new project"""
    new_project = await ProjectDAO.add(**project.model_dump())
    return ProjectResponse.model_validate(new_project)


@router.get("/all", response_model=List[ProjectResponse])
async def get_all_projects():
    """Get all projects"""
    all_projects = await ProjectDAO.find_all()
    if not all_projects:
        raise HTTPException(status_code=404, detail="No projects found")
    return [ProjectResponse.model_validate(a_type) for a_type in all_projects]


@router.get("/{project_id}", response_model=ProjectResponse)
async def get_project_by_id(project_id: int):
    """Get project by id"""

    project = await ProjectDAO.find_one_or_none(id=project_id)
    if not project:
        raise HTTPException(status_code=404, detail="No project found")
    return ProjectResponse.model_validate(project)


@router.put("/{project_id}", response_model=ProjectResponse)
async def update_project(project_id: int, project_update: ProjectUpdate):
    """Update project"""
    update_a_type = await ProjectDAO.update(
        id=project_id, **project_update.model_dump()
    )
    if not update_a_type:
        raise HTTPException(status_code=404, detail="Project not found")

    return ProjectResponse.model_validate(update_a_type)


@router.delete("/{project_id}", response_model=ProjectResponse)
async def delete_project(project_id: int):
    """Delete project"""
    del_project = await ProjectDAO.delete(id=project_id)
    if not del_project:
        raise HTTPException(status_code=404, detail="Project not found")
    return ProjectResponse.model_validate(del_project)
