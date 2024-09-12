def main():
    f_name = input("First Name: ")
    l_name = input("Last Nake: ")
    m_or_f = input("Male or Female(m or f): ")

    result = m_or_f + l_name[0] + f_name[:6]

    print(result.upper())

main()
