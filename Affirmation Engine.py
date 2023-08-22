import colors

name = input("What is your preferred name? ")
pronoun = input("What pronouns would you like us to use? ").lower()
print("Thank you for sharing that you use " + pronoun + ", " + name + ". We affirm and respect your gender identity. "
                                                                       "We would like to build an inclusive "
                                                                       "environment where everyone feels heard and "
                                                                       "accepted.")

while True:
    choices = ["agender", "aromantic", "asexual", "bisexual", "demiromantic", "demisexual", "genderfluid",
               "genderqueer", "intersex", "lesbian", "nonbinary", "pansexual", "polyamorous", "polysexual",
               "rainbow", "transgender", "help"]
    flag_help = ["agender", "aromantic", "asexual", "bisexual", "demiromantic", "demisexual", "genderfluid",
                 "genderqueer", "intersex", "lesbian", "nonbinary", "pansexual", "polyamorous", "polysexual",
                 "rainbow", "transgender"]
    # flags
    agender = colors.color('AG', fg='black', bg=234) + colors.color("E", fg='white', bg=234) \
              + colors.color("N", fg='green', bg=234) + colors.color("DE", fg='white', bg=234) \
              + colors.color("R", fg='black', bg=234)
    aromantic = colors.color('AR', fg=2, bg=234) + colors.color("OM", fg=10, bg=234) + colors.color("N", fg=7,
                                                                                                    bg=234) + colors.color(
        "DE", fg=15, bg=234) + colors.color("R", fg=16, bg=234)
    asexual = colors.color('AS', fg=16, bg=234) + colors.color('EX', fg=7, bg=234) + colors.color('UA', fg=15,
                                                                                                  bg=234) + colors.color(
        'L', fg=91, bg=234)
    bisexual = colors.color('BIS', fg=125, bg=234) + colors.color('EX', fg=141, bg=234) + colors.color('UAL', fg=20,
                                                                                                       bg=234)
    demisexual = colors.color('DEM', fg=16, bg=234) + colors.color('IROM', fg=15, bg=234) + colors.color('ANT', fg=2,
                                                                                                         bg=234) + colors.color(
        'IC', fg=7, bg=234)
    genderfluid = colors.color('GE', fg=211, bg=234) + colors.color('ND', fg=15, bg=234) + colors.color('DER', fg=165,
                                                                                                        bg=234) + colors.color(
        'FLU', fg=16, bg=234) + colors.color('ID', fg=55, bg=234)
    genderqueer = colors.color('GENDE', fg=63, bg=234) + colors.color('RQU', fg=255, bg=234) + colors.color('EER',
                                                                                                            fg=100,
                                                                                                            bg=234)
    intersex = colors.color('INTE', fg=11, bg=234) + colors.color('RSEX', fg=55, bg=234)
    lesbian = colors.color('L', fg=166, bg=234) + colors.color('E', fg=130, bg=234) + colors.color('S', fg=173,
                                                                                                   bg=234) + colors.color(
        'B', fg=15, bg=234) + colors.color('I', fg=211, bg=234) + colors.color('A', fg=168, bg=234) + colors.color('N',
                                                                                                                   fg=89,
                                                                                                                   bg=234)
    nonbinary = colors.color('NON', fg=11, bg=234) + colors.color('BI', fg=15, bg=234) + colors.color('NA', fg=61,
                                                                                                      bg=234) + colors.color(
        'RY', fg=16, bg=234)
    pansexual = colors.color('PAN', fg=125, bg=234) + colors.color('SEX', fg=11, bg=234) + colors.color('UAL', fg=39,
                                                                                                        bg=234)
    polyamorous = colors.color('POL', fg=20, bg=234) + colors.color('YAM', fg=124, bg=234) + colors.color('OUR', fg=11,
                                                                                                          bg=234) + colors.color(
        'OUS', fg=16, bg=234)
    polysexual = colors.color('POLY', fg=126, bg=234) + colors.color('SEX', fg=48, bg=234) + colors.color('UAL', fg=39,
                                                                                                          bg=234)
    rainbow = colors.color('P', fg=1, bg=234) + colors.color('R', fg=3, bg=234) + colors.color('I', fg=11,
                                                                                               bg=234) + colors.color(
        'D', fg=2, bg=234) + colors.color('E', fg=12, bg=234) + colors.color('!', fg=55, bg=234)
    transgender = colors.color('TR', fg=25, bg=234) + colors.color('AN', fg=13, bg=234) + colors.color('SGE', fg=15,
                                                                                                       bg=234) + colors.color(
        'ND', fg=13, bg=234) + colors.color('ER', fg=25, bg=234)
    flag = None

    while flag not in choices:
        flag = input("Which flag would you like to see? Enter help for a list: ").lower()
    if flag == "agender":
        print(agender)
    elif flag == "aromantic":
        print(aromantic)
    elif flag == "asexual":
        print(asexual)
    elif flag == "bisexual":
        print(bisexual)
    elif flag == "demisexual":
        print(demisexual)
    elif flag == "demisexual":
        print(demisexual)
    elif flag == "genderqueer":
        print(genderqueer)
    elif flag == "genderfluid":
        print(genderfluid)
    elif flag == "intersex":
        print(intersex)
    elif flag == "lesbian":
        print(lesbian)
    elif flag == "nonbinary":
        print(nonbinary)
    elif flag == "pansexual":
        print(pansexual)
    elif flag == "polysexual":
        print(polysexual)
    elif flag == "polyamorous":
        print(polyamorous)
    elif flag == "rainbow":
        print(rainbow)
    elif flag == "transgender":
        print(transgender)
    elif flag == "help":
        print(flag_help)

    play_again = input("Pick again? (yes/no)").lower()

    if play_again != "yes":
        break
print("Bye")
