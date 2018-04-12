HEX_COLORS = {"aliceblue": "#f0f8ff", "aquamarine1": "#7fffd4", "blue1": "#0000ff", "blueviolet": "#8a2be2",
              "cadetblue1": "#98f5ff", "chartreuse2": "#76ee00", "darkorchid4": "#68228b", "dodgerblue1": "#1e90ff",
              "deeppink1": "#ff1493", "yellow1": "#ffff00"}

color = input("Enter color name: ").lower()
while color != "":
    if color in HEX_COLORS:
        print(color, "is", HEX_COLORS[color])
    else:
        print("Invalid color")
    color = input("Enter color name: ").lower()
    