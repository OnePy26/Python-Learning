while True:

    annual_ctc = int(input("Enter Annual CTC - "))

    #salary component's bifurcated calculation - monthly

    ctc = round(annual_ctc / 12)
    basic = ctc * 0.5
    hra = basic * 0.4
    gratuity = basic * 0.0481
    pf_er = basic * 0.012
    if basic <21001:
        esic_er = basic * 0.0325
    else:
        esic_er = 0
    special_allowance = ctc - (basic + hra + pf_er + esic_er + gratuity)
    gross = basic + hra + special_allowance

    print()
    print(f"Monthly Salary breakup for       INR {ctc:,.0f}")
    print("...........................................")
    print(f"Basic Salary                   = INR {basic:,.0f}")
    print(f"HRA                            = INR {hra:,.0f}")
    print(f"Special Allowance              = INR {special_allowance:,.0f}")

    print("...........................................")
    print(f"Gross Salary                   = INR {gross:,.0f}")
    print("...........................................")
    print(f"Employer PF                    = INR {pf_er:,.0f}")
    if esic_er <1:
        print()
    else:
        print(f"Employer ESIC                  = INR {esic_er:,.0f}")

    print(f"Gratuity                       = INR {gratuity:,.0f}")
    print("...........................................")
    print(f"Total Monthly CTC              = INR {ctc:,.0f}")

#Below condition should be indented in line with the while loop.

    user_exit = input("Do you want another CTC breakup(Y/N): ").upper()
    if user_exit == "Y":
        continue
    elif user_exit =="N":
        break