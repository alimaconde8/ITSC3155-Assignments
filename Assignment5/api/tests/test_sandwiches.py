from fastapi.testclient import TestClient
from ..controllers import orders
from ..main import app
import pytest
from ..models import models

# Create a test client for the app
client = TestClient(app)


@pytest.fixture
def db_session(mocker):
    return mocker.Mock()


def test_create_order(db_session):
    # Create a sample order using the Pydantic model
    order_data = {
        "customer_name": "John Doe",
        "description": "Test order"
    }

    # Call the create function
    created_order = orders.create(db_session, models.Order(**order_data))

    # Assertions
    assert created_order.customer_name == order_data["customer_name"]
    assert created_order.description == order_data["description"]
