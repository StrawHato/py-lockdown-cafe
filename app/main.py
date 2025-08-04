from app.cafe import Cafe
from app.errors import (VaccineError, NotWearingMaskError,
                        NotVaccinatedError, OutdatedVaccineError)
import datetime


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    for friend in friends:
        try:
            if "vaccine" not in friend:
                raise NotVaccinatedError
            if friend["vaccine"]["expiration_date"] < datetime.date.today():
                raise OutdatedVaccineError
        except VaccineError:
            return "All friends should be vaccinated"

    masks_to_buy = sum(not f["wearing_a_mask"] for f in friends)
    if masks_to_buy > 0:
        return f"Friends should buy {masks_to_buy} masks"

    try:
        for friend in friends:
            cafe.visit_cafe(friend)
    except (VaccineError, NotWearingMaskError):
        return "Something went wrong"
    else:
        return f"Friends can go to {cafe.name}"
