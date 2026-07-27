def day_of_week(day):
    match day:
        case 1:
            return "It is Monday!"
        case 2:
            return "It is Tuesday!"
        case 3:
            return "It is Wednesday!"
        case 4:
            return "It is Thursday!"
        case 5:
            return "It is Friday!"
        case 6: 
            return "It is Satureday!"
        case 7:
            return "It is Sunday!"
        case _:
            return "It is not a valid day!"
day_of_week(7)