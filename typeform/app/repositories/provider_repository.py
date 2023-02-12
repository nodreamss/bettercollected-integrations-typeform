from typeform.app.container import repository
from typeform.app.models.provider import Provider


@repository()
class ProviderRepository:

    @staticmethod
    async def get_provider(provider_name: str) -> Provider:
        return await Provider.find_one_by_args(Provider.provider_name == provider_name)
