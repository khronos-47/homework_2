from .search_doctor import SearchDoctors
from .search_ordinary_user import SerchOrdinaryUser
from .search_user_with_receipt import SearchUserReceipt


search_user = [SearchDoctors, SearchUserReceipt, SerchOrdinaryUser]
