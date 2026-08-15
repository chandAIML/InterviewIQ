from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.schemas.dashboard import DashboardSummary
from app.services.dashboard_service import get_dashboard_summary
from app.dependencies.auth import get_current_user
from app.models.user import User

router = APIRouter(prefix="/api/v1/dashboard", tags=["dashboard"])


@router.get("/", response_model=DashboardSummary)
def dashboard(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    summary = get_dashboard_summary(db, current_user.id)
    return DashboardSummary(**summary)
