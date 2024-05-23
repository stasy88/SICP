
def calculate_plunger_pump_parameters(volume=30, time=60, density=1000, gravity=9.81, efficiency=0.7):
    def calculate_flow_rate():
        return volume / time, "м3/с"

    def calculate_power():
        return density * gravity * volume / time * efficiency, "Вт"

    return calculate_flow_rate(), calculate_power()


def calculate_diaphragm_pump_parameters(volume=25, time=50, density=1100, gravity=9.81, efficiency=0.75):
    def calculate_flow_rate():
        return volume / time, "м3/с"

    def calculate_power():
        return density * gravity * volume / time * efficiency, "Вт"

    return calculate_flow_rate(), calculate_power()


def print_pump_parameters(flow_rate, power, pump_type):
    if pump_type == "plunger":
        print("\nПараметры плунжерного насоса:")
    elif pump_type == "diaphragm":
        print("\nПараметры мембранного насоса:")
    else:
        print("\nНеизвестный тип насоса")
        return

    print("\nРасход:", flow_rate)
    print("Мощность:", power, "\n")


if __name__ == "__main__":
    plunger_flow_rate, plunger_power = calculate_plunger_pump_parameters()
    diaphragm_flow_rate, diaphragm_power = calculate_diaphragm_pump_parameters()

    print_pump_parameters(plunger_flow_rate, plunger_power, pump_type="plunger")
    print_pump_parameters(diaphragm_flow_rate, diaphragm_power, pump_type="diaphragm")
