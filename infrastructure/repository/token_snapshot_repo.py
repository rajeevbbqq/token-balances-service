from infrastructure.repository.base_repository import BaseRepository
from infrastructure.models import Snapshots, TransferInfo
from domain.factory.token_snapshot_factory import TokenSnapshotFactory
from sqlalchemy import exc


class TokenSnapshotRepo(BaseRepository):
    def get_token_balance(self, address):

        try:
            result = (
                self.session.query(Snapshots)
                .filter(Snapshots.address == address)
                .first()
            )
        except exc.SQLAlchemyError as e:
            raise (e)

        if result is not None:
            transfer_details = self.get_transfer_status(address)
            return TokenSnapshotFactory.convert_token_snapshot_db_to_entity_model(
                result, transfer_details
            ).to_response()
        else:
            return None

    def get_transfer_status(self, address):
        try:
            result = (
                self.session.query(TransferInfo)
                .filter(TransferInfo.wallet_address == address)
                .first()
            )
        except exc.SQLAlchemyError as e:
            raise (e)

        return result or None