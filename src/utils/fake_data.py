import uuid
from datetime import datetime, timedelta

from faker import Faker
from sqlalchemy.ext.asyncio import AsyncSession

from src.models.budget import Budget
from src.models.category import Category
from src.models.goal import Goal
from src.models.transaction import Transaction
from src.models.user import User

fake = Faker()


async def create_fake_user():
    return User(
        user_id=uuid.uuid4(),
        username=fake.user_name(),
        email=fake.email(),
        hashed_password=fake.password(),
    )


async def create_fake_category():
    return Category(name=fake.word())


async def create_fake_budget(user_id, category_id):
    start_date = datetime.now()
    end_date = start_date + timedelta(days=30)
    return Budget(
        user_id=user_id,
        category_id=category_id,
        amount=fake.random_number(digits=5) / 100,
        start_date=start_date,
        end_date=end_date,
    )


async def create_fake_goal(user_id, category_id):
    target_date = datetime.now() + timedelta(days=60)
    return Goal(
        user_id=user_id,
        category_id=category_id,
        amount=fake.random_number(digits=5) / 100,
        description=fake.sentence(),
        target_date=target_date,
    )


async def create_fake_transaction(user_id, category_id):
    timestamp = datetime.now()
    return Transaction(
        user_id=user_id,
        category_id=category_id,
        amount=fake.random_number(digits=5) / 100,
        timestamp=timestamp,
        description=fake.sentence(),
    )


async def create_fake_data(n: int, db: AsyncSession):
    for _ in range(n):
        user = await create_fake_user()
        db.add(user)
        await db.commit()
        await db.refresh(user)

        category = await create_fake_category()
        db.add(category)
        await db.commit()
        await db.refresh(category)

        budget = await create_fake_budget(user.user_id, category.category_id)
        db.add(budget)

        goal = await create_fake_goal(user.user_id, category.category_id)
        db.add(goal)

        transaction = await create_fake_transaction(user.user_id, category.category_id)
        db.add(transaction)

        await db.commit()
