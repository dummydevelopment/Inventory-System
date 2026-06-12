import os
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

from app.config import settings

print("\n========== DATABASE CONFIG ==========")

print("DB_HOST =", settings.DB_HOST)
print("DB_NAME =", settings.DB_NAME)
print("DB_USER =", settings.DB_USER)

DATABASE_URL = os.getenv("DATABASE_URL")

print("\nDATABASE_URL exists =", DATABASE_URL is not None)

if DATABASE_URL:
    # hide password before printing
    safe_url = DATABASE_URL

    if "@" in safe_url and "://" in safe_url:
        protocol = safe_url.split("://")[0]
        remaining = safe_url.split("://")[1]

        if ":" in remaining:
            user = remaining.split(":")[0]
            host_part = remaining.split("@")[-1]

            safe_url = (
                f"{protocol}://"
                f"{user}:******@"
                f"{host_part}"
            )

    print("DATABASE_URL =", safe_url)
else:
    print("❌ DATABASE_URL is None")

print("=====================================\n")

engine = create_engine(DATABASE_URL)

print("✅ SQLAlchemy engine created")

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

print("✅ SessionLocal created")

Base = declarative_base()

print("✅ Base created")