#include <iostream>
#include <stdexcept>
#include <memory>

using namespace std;

// Шаблонный класс
template <typename T>
class List {
private:
    T* data;
    size_t size;
    size_t volume;

    // Увеличение ёмкости списка
    void incVolume() {
        size_t new_vol = volume * 2;
        T* new_data = new T[new_vol];
        for (size_t i = 0; i < size; ++i) {
            new_data[i] = data[i];
        }
        delete[] data; // Освобождение
        data = new_data; // старой памяти
        volume = new_vol;
    }
public:
    // Конструктор по умолчанию
    List() : data(nullptr), size(0), volume(0) {}

    // Добавление в конец списка
    void add(const T& item) {
        if (size == volume) {
            incVolume();
        }
        data[size++] = item;
    }
    // Удаление элемента
    void remove(size_t index) {
        if (index >= size) {
            throw out_of_range("Индекс вне диапазона");
        }
        for (size_t i = index; i < size - 1; ++i) {
            data[i] = data[i + 1];
        }
        --size;
    }
    // Возвращение элемента
    T& getItem(size_t index) const {
        if (index >= size) {
            throw out_of_range("Индекс вне диапазона");
        }
        return data[index];
    }
    // Возвращение размера списка
    size_t getSize() const {
        return size;
    }
    // Конструктор копирования
    List(const List& other) {
        size = other.size;
        volume = other.volume;
        data = new T[volume];
        for (size_t i = 0; i < size; ++i) {
            data[i] = other.data[i];
        }
    }
    // Присваивание элементов
    List& operator=(const List& other) {
        if (this == &other) { // Проверка на
            return *this; // самоприсваивание
        }
        delete[] data; // Освобождение
        size = other.size; // старой памяти
        volume = other.volume;
        data = new T[volume];
        for (size_t i = 0; i < size; ++i) {
            data[i] = other.data[i];
        }
        return *this;
    }
    // Деструктор класса
    ~List() {
        delete[] data;
    }
};

int main() {
    // Пример использования
    List<int> int_list;
    int_list.add(1);
    int_list.add(2);
    int_list.add(3);
    cout << "" << endl;

    for (size_t i = 0; i < int_list.getSize(); ++i) {
        cout << i << " элемент: " << int_list.getItem(i) << endl;
    } // Доступ к значениям
    cout << "\nРазмер списка: " << int_list.getSize() << endl;
    int_list.remove(1); // Удаление элемента
    cout << "После удаления: " << int_list.getSize() << "" << endl;

    return 0;
}