from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from sqlalchemy.engine.url import URL

async_engine = None
async_session_maker = None

def create_database_url(app_config):
    return URL.create(
        drivername='postgresql+asyncpg',
        username=app_config.POSTGRES_USER,
        password=app_config.POSTGRES_PASSWORD,
        host=app_config.POSTGRES_HOST,
        database=app_config.POSTGRES_DB
    )

def init_engine(app_config):
    global async_engine
    async_engine = create_async_engine(create_database_url(app_config))

def init_session_maker(engine):
    global async_session_maker
    async_session_maker = async_sessionmaker(bind=engine, expire_on_commit=False, class_=AsyncSession)

AsyncEngine = create_async_engine
AsyncSessionMaker = async_sessionmaker
URLCreate = URL.create