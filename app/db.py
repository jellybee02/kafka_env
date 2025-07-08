from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession  # 비동기 DB 연결을 위한 모듈
from sqlalchemy.orm import sessionmaker, declarative_base  # ORM 세션 및 Base 클래스

import os  # 환경변수에서 DB URL 읽기

DATABASE_URL = os.environ["DATABASE_URL"]  # .env 또는 docker-compose에서 정의된 DB URL

# SQLAlchemy 비동기 엔진 생성 (asyncpg 사용)
engine = create_async_engine(DATABASE_URL, echo=True)

# DB 세션 생성기 정의 (비동기 세션 사용)
SessionLocal = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)

# 모델 정의 시 사용할 베이스 클래스
Base = declarative_base()
