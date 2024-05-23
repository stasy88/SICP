#include <iostream>
#include <string>

using namespace std;

class Example {
private:
    int private_var;
    string private_str;
public:
    Example() { // Конструктор по умолчанию
        private_var = 0;
        private_str = "default";
    }
    // Перегруженный конструктор с параметрами
    Example(int var, string str) {
        private_var = var;
        private_str = str;
    }
    // Установка значений private
    void setValues(int var, string str) {
        private_var = var;
        private_str = str;
    }
    // Получение значения private
    int getPrivateVar() { // переменной
        return private_var;
    }
    string getPrivateStr() { // строкой
        return private_str;
    }
};

int main() {
    Example obj_1; // Создание объекта обычным конструктором
    cout << "\nPrivate var: " << obj_1.getPrivateVar() << endl;
    cout << "Private str: " << obj_1.getPrivateStr() << endl;

    Example obj_2(10, "hello"); // перегруженным конструктором
    cout << "\nPrivate var: " << obj_2.getPrivateVar() << endl;
    cout << "Private str: " << obj_2.getPrivateStr() << endl;

    obj_1.setValues(5, "world"); // Изменение значений private
    cout << "\nPrivate var: " << obj_1.getPrivateVar() << endl;
    cout << "Private str: " << obj_1.getPrivateStr() << endl;

    return 0;
}