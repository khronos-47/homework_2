from .common_item_validation import CommonItemValidation
from .prescription_item_validation import PrescriptionItemValidation
from .special_item_validation import SpecialItemValidation


item_validation = {
    "common": CommonItemValidation,
    "receipt": PrescriptionItemValidation,
    "special": SpecialItemValidation,
}
