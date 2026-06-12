from dotenv import load_dotenv
import os


print("\n========== CONFIG START ==========")

print("Loading environment variables...")

load_dotenv()

print("Environment loaded")


class Settings:

    DB_HOST = os.getenv("DB_HOST", "").strip()

    DB_PORT = os.getenv("DB_PORT", "").strip()

    DB_NAME = os.getenv("DB_NAME", "").strip()

    DB_USER = os.getenv("DB_USER", "").strip()

    DB_PASSWORD = os.getenv("DB_PASSWORD", "").strip()

    def debug(self):

        print("\n========== ENV VALUES ==========")

        print("DB_HOST:", repr(self.DB_HOST))

        print("DB_PORT:", repr(self.DB_PORT))

        print("DB_NAME:", repr(self.DB_NAME))

        print("DB_USER:", repr(self.DB_USER))

        print(
            "DB_PASSWORD_EXISTS:",
            bool(self.DB_PASSWORD)
        )

        print(
            "DB_PASSWORD_LENGTH:",
            len(self.DB_PASSWORD)
            if self.DB_PASSWORD
            else 0
        )

        print("===============================\n")


settings = Settings()

settings.debug()

print("========== CONFIG END ==========\n")