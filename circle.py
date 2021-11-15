import math as mt

#Unicode de quadrado \u25A0

def main():
    lisCircle = ['\n\t\t'];
    circleRadius = abs(int(input("\n>> Insira o raio do circulo: ")));
    caracter = str(input(">> Insira o caracter que quer que componha o círculo: "));
    print("\n\n");

    inCircleX = - circleRadius;
    inCircleY = circleRadius;

    for y in range(0, 2 * circleRadius + 1):
        for x in range(0, 2 * circleRadius + 1):     
            if (mt.pow(inCircleX, 2) + mt.pow(inCircleY, 2) == mt.pow(circleRadius, 2) or (mt.pow(inCircleX, 2) + mt.pow(inCircleY, 2) <= (mt.pow(circleRadius, 2) + circleRadius // 2))):
                lisCircle.append(str(caracter));    
            else:
                lisCircle.append(" ");

            inCircleX += 1;
            
        inCircleX = -circleRadius;
        inCircleY -= 1;
        lisCircle.append('\n\t\t');
    
    print(*lisCircle, '\n\n');

main();
