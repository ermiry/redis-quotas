from redis import Redis
from redis_om import Migrator, JsonModel, Field

QUOTA_STATUS_NONE = 0
QUOTA_STATUS_WAITING = 1
QUOTA_STATUS_ACTIVE = 2
QUOTA_STATUS_DISABLED = 3
QUOTA_STATUS_ENDED = 4

class Quota (JsonModel):
	name: str = Field (index=False)
	value: int = Field (index=True)
	status: int = Field (index=False)
	quantity: int = Field (index=False)
	used: int = Field (index=False)
	last_time: float = Field (index=False)

	class Meta:
		database = Redis (host="cache", port=6379)

Migrator ().run ()
