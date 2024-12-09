import openpyxl
from sqlalchemy.ext.asyncio import AsyncSession
from storage.database import get_db
from storage.models import PriceList

async def import_price_list(file_path: str):
    """Импорт прайслиста из Excel в таблицу `PriceList`."""
    # Загружаем Excel-файл
    workbook = openpyxl.load_workbook(file_path, data_only=True)  # `data_only=True` возвращает вычисленные значения
    sheet = workbook.active

    async with get_db() as session:  # Получение асинхронной сессии
        for row in sheet.iter_rows(min_row=2, values_only=True): 
            try:
                new_price_list = PriceList(
                    name=row[0],
                    driver_price=int(row[1]),
                    dispatcher_price=int(row[2]),
                    price_per_cubic_meter=int(float(row[3])),  
                    description=row[5] or "",  
                )
                session.add(new_price_list)  
            except Exception as e:
                print(f"Ошибка при обработке строки {row}: {e}")

        await session.commit()  
        print("Прайслист успешно импортирован!")
