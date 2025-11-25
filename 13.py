# Voting eligibility: age > 18, Indian resident, voter ID, min education

def check_voting_eligibility(age, resident, has_voter_id, education):
    min_edu = ["highschool", "bachelor", "master", "phd"]
    if age > 18 and resident.lower() == "india" and has_voter_id and education.lower() in min_edu:
        return "Eligible to Vote"
    else:
        return "Not Eligible"

def main():
    age = int(input("Enter age: "))
    resident = input("Enter country of residence: ")
    voter_id = input("Do you have voter ID? (yes/no): ").lower() == "yes"
    edu = input("Enter highest qualification: ")
    print(check_voting_eligibility(age, resident, voter_id, edu))

if __name__ == "__main__":
    main()
