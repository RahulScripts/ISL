# Government engineering college eligibility

def check_engg_college(age, jee_qualified, has_maths):
    if age > 18 and jee_qualified and has_maths:
        return "Eligible for Government Engineering College"
    else:
        return "Not Eligible"

def main():
    age = int(input("Enter age: "))
    jee = input("JEE Mains qualified? (yes/no): ").lower() == "yes"
    maths = input("Mathematics in 12th? (yes/no): ").lower() == "yes"
    print(check_engg_college(age, jee, maths))

if __name__ == "__main__":
    main()
