from sqlalchemy import create_engine, text
from src.core.config import settings

def setup_database():
    engine = create_engine(settings.database_url)
    
    # Create basic tables (expand as needed)
    with engine.connect() as conn:
        conn.execute(text("""
            CREATE TABLE IF NOT EXISTS analyses (
                id SERIAL PRIMARY KEY,
                analysis_id VARCHAR(255) UNIQUE,
                status VARCHAR(50),
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                completed_at TIMESTAMP,
                result_data JSONB
            )
        """))
        conn.commit()
    
    print("Database setup completed!")

if __name__ == "__main__":
    setup_database()
