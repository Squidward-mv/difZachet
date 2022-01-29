#include <iostream>

int main() {
    setlocale(LC_ALL, "Ru");
    double Ax, Ay;
    std::cout << "\t Введите координаты А ";
    std::cin >> Ax >> Ay;

    double Bx, By;
    std::cout << "\t Введите координаты Б ";
    std::cin >> Bx >> By;

    if (Ax == Bx && Ay == By) {
        std::cout << "Точка.\n";
        return 0;
    }

    if (Ax == Bx) {
        std::cout << "x=" << Ax << '\n';
        return 0;
    }
    if (Ay == By) {
        std::cout << "y=" << Ay << '\n';
        return 0;
    }

    double k = (By - Ay) / (Bx - Ax);
    double b = (-k*Ax + Ay);

    std::cout << "y=" << k << "x+("<<b<<")\n";
    
    return 0;
}
