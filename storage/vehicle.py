from datetime import datetime
from sqlalchemy.future import select

from storage.models import Vehicle
from storage.database import get_db

async def create_vehicle(vehicle_number: str, agent_id: int, created_at: str = None) -> Vehicle:
    """Создать новое транспортное средство."""
    if created_at is None:
        created_at = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')  # Используем текущую дату и время, если не указано.

    async with get_db() as session:
        new_vehicle = Vehicle(
            vehicle_number=vehicle_number,
            agent_id=agent_id,
            created_at=created_at
        )
        session.add(new_vehicle)  # Добавляем новый объект в сессию
        await session.commit()  # Явный коммит
        await session.refresh(new_vehicle)  # Обновляем объект с данными из базы
        return new_vehicle


async def get_vehicle_by_number(vehicle_number: str) -> Vehicle:
    """Получить транспортное средство по номеру."""
    async with get_db() as session:
        result = await session.execute(select(Vehicle).filter_by(vehicle_number=vehicle_number))
        vehicle = result.scalar_one_or_none()
        return vehicle