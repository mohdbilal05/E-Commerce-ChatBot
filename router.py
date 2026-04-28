from semantic_router import Route
from semantic_router.routers import SemanticRouter
from semantic_router.encoders import HuggingFaceEncoder
from semantic_router.index.local import LocalIndex
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)


encoder = HuggingFaceEncoder(
    name = "sentence-transformers/all-MiniLM-L6-v2",
)


faq = Route(
    name="faq",
    utterances=[
         "What payment methods are accepted?", 
        "How do I use a promo code during checkout?",
        "What is your refund policy?",
        "Do you accept cash?",
        "Can I pay with credit card or cash?",
        "What forms of payment do you support?",
        "Is cash on delivery available?",
        "What are the different ways I can pay for my order?",
        "What is your return policy?",
        "How do I return a product?",
        "Can I return an item?",
        "What is the return and refund policy?",
        "How many days do I have to return something?",
        "What is the policy on defective products?",
    ]
)


sql = Route(
    name="sql",
    utterances=[
        "I want to buy nike shoes that have 50% discount",
        "Are there any shoes under Rs. 3000?",
        "Do you have any formal shoes in size 9?",
        "Are there any Puma Shoes on sale?",
        "What is the price of Puma running shoes?",
    ]
)


router = SemanticRouter(
    routes=[faq, sql],
    encoder=encoder,
    auto_sync="local"
)


if __name__ == "__main__":
    print(router("What is the return policy of the products?").name)
    print(router("Pink Puma Shoes in price range 5000 to 10000").name)