# Government scheme eligibility

def check_eligibility(age, income, region, education):
    allowed_regions = ["region1", "region2", "region3"]
    min_education = ["highschool", "bachelor", "master", "phd"]

    region_ok = region.lower() in allowed_regions
    edu_ok = education.lower() in min_education
    age_ok = age > 18
    income_ok = income < 500000  # example limit

    if age_ok and income_ok and region_ok and edu_ok:
        return "Eligible"
    elif age_ok and income_ok and (region_ok or edu_ok):
        return "Conditionally Eligible"
    else:
        return "Not Eligible"

def main():
    age = int(input("Enter age: "))
    income = float(input("Enter annual income: "))
    region = input("Enter region: ")
    education = input("Enter highest education: ")

    print("Result:", check_eligibility(age, income, region, education))

if __name__ == "__main__":
    main()
