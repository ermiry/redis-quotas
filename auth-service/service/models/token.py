from redis import Redis
from redis_om import Migrator, JsonModel, Field

TOKEN_STATUS_NONE = 0
TOKEN_STATUS_AVAILABLE = 1
TOKEN_STATUS_EXPIRED = 2
TOKEN_STATUS_DISABLED = 3
TOKEN_STATUS_REVOKED = 4

class Token (JsonModel):
	reference: str = Field (index=True)
	name: str = Field (index=False)
	quota: str = Field (index=True)
	value: int = Field (index=True)
	status: int = Field (index=False)
	created: float = Field (index=False)
	expired: float = Field (index=False)
	disabled: float = Field (index=False)
	revoked: float = Field (index=False)

	class Meta:
		database = Redis (host="cache", port=6379)

Migrator ().run ()
