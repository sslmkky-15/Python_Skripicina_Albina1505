import argparse
import math
import sys


def main():

    parser = argparse.ArgumentParser(description="Кредитный калькулятор")
    parser.add_argument("--type", type=str, help="Тип платежа: 'annuity' или 'diff'")
    parser.add_argument("--principal", type=float, help="Основная сумма кредита")
    parser.add_argument("--periods", type=int, help="Кількість місяців")
    parser.add_argument("--interest", type=float, help="Відсоток по кредиту")
    parser.add_argument("--payment", type=float, help="Щомісячний платіж")

    args = parser.parse_args()


    if len(sys.argv) < 5:
        print("Incorrect parameters")
        return


    if args.type not in ["annuity", "diff"]:
        print("Incorrect parameters")
        return

    if args.type == "diff" and args.payment is not None:
        print("Incorrect parameters")
        return

    if args.interest is None:
        print("Incorrect parameters")
        return


    params = [args.principal, args.periods, args.interest, args.payment]
    for param in params:
        if param is not None and param < 0:
            print("Incorrect parameters")
            return


    i = args.interest / (12 * 100)


    if args.type == "diff":
        principal = args.principal
        periods = args.periods
        total_paid = 0

        for m in range(1, periods + 1):

            diff_payment = math.ceil(principal / periods + i * (principal - principal * (m - 1) / periods))
            print(f"Month {m}: payment is {diff_payment}")
            total_paid += diff_payment

        overpayment = int(total_paid - principal)
        print(f"\nOverpayment = {overpayment}")


    elif args.type == "annuity":

        if args.periods is None:
            principal = args.principal
            payment = args.payment


            months = math.ceil(math.log(payment / (payment - i * principal), 1 + i))

            years = months // 12
            remaining_months = months % 12


            if years == 0:
                time_str = f"{remaining_months} months" if remaining_months != 1 else "1 month"
            elif remaining_months == 0:
                time_str = f"{years} years" if years != 1 else "1 year"
            else:
                y_str = "years" if years != 1 else "year"
                m_str = "months" if remaining_months != 1 else "month"
                time_str = f"{years} {y_str} and {remaining_months} {m_str}"

            print(f"It will take {time_str} to repay this loan!")
            overpayment = int(months * payment - principal)
            print(f"Overpayment = {overpayment}")


        elif args.payment is None:
            principal = args.principal
            periods = args.periods


            payment = math.ceil(principal * (i * math.pow(1 + i, periods)) / (math.pow(1 + i, periods) - 1))

            print(f"Your annuity payment = {payment}!")
            overpayment = int(payment * periods - principal)
            print(f"Overpayment = {overpayment}")


        elif args.principal is None:
            payment = args.payment
            periods = args.periods


            principal = math.floor(payment / ((i * math.pow(1 + i, periods)) / (math.pow(1 + i, periods) - 1)))

            print(f"Your loan principal = {principal}!")
            overpayment = int(payment * periods - principal)
            print(f"Overpayment = {overpayment}")


if __name__ == "__main__":
    main()