from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from urllib.parse import quote_plus

from app.config import settings


print("\n========== DATABASE START ==========")

print("Step 1 → Validate ENV")


required = {
    "DB_HOST": settings.DB_HOST,
    "DB_PORT": settings.DB_PORT,
    "DB_NAME": settings.DB_NAME,
    "DB_USER": settings.DB_USER,
    "DB_PASSWORD": settings.DB_PASSWORD,
}


missing = []

for key, value in required.items():

    if not value:

        print(f"❌ Missing: {key}")

        missing.append(key)

    else:

        print(f"✅ Found: {key}")


if missing:

    raise Exception(
        f"Missing env variables: {missing}"
    )


print("\nStep 2 → Encode password")

encoded_password = quote_plus(
    settings.DB_PASSWORD
)

print("Password encoded")


print("\nStep 3 → Build DATABASE_URL")

DATABASE_URL = (
    "postgresql://"
    f"{settings.DB_USER}:"
    f"{encoded_password}@"
    f"{settings.DB_HOST}:"
    f"{settings.DB_PORT}/"
    f"{settings.DB_NAME}"
)

safe_url = DATABASE_URL.replace(
    encoded_password,
    "******"
)

print("DATABASE_URL:")
print(safe_url)


print("\nStep 4 → Create SQLAlchemy engine")

try:

    engine = create_engine(
        DATABASE_URL,
        pool_pre_ping=True
    )

    print("✅ Engine created")

except Exception as e:

    print("❌ Engine creation failed")

    print(str(e))

    raise


print("\nStep 5 → Create SessionLocal")

SessionLocal = sessionmaker(
    bind=engine,
    autocommit=False,
    autoflush=False
)

print("✅ SessionLocal created")


print("\nStep 6 → Create Base")

Base = declarative_base()

print("✅ Base created")

print("\n========== DATABASE END ==========\n")