from nada_dsl import *

def nada_main():
    # Define parties
    sensor_a = Party(name="SensorA")
    sensor_b = Party(name="SensorB")
    sensor_c = Party(name="SensorC")
    aggregator = Party(name="Aggregator")

    # Define secret inputs from sensors
    data_sensor_a = SecretInteger(Input(name="data_sensor_a", party=sensor_a))
    data_sensor_b = SecretInteger(Input(name="data_sensor_b", party=sensor_b))
    data_sensor_c = SecretInteger(Input(name="data_sensor_c", party=sensor_c))

    # Perform secure addition to aggregate sensor data
    total_data = data_sensor_a + data_sensor_b + data_sensor_c

    # Define constants as Inputs
    threshold_input = Input(name="threshold", party=aggregator)
    total_data_threshold_input = Input(name="total_data_threshold", party=aggregator)

    # Convert Inputs to PublicInteger
    threshold = PublicInteger(threshold_input)
    total_data_threshold = PublicInteger(total_data_threshold_input)

    # Check if any sensor data exceeds the threshold
    is_sensor_a_high = data_sensor_a > threshold
    is_sensor_b_high = data_sensor_b > threshold
    is_sensor_c_high = data_sensor_c > threshold

    # Use integer variable to track if any sensor is high
 
    # Check if the total aggregated data exceeds a certain threshold
    is_total_data_high = total_data > total_data_threshold

    # Output the aggregated data and high value checks to the aggregator party
    return [
        Output(total_data, name="total_data", party=aggregator),
        # Output(is_any_sensor_high, name="is_any_sensor_high", party=aggregator),
        Output(is_total_data_high, name="is_total_data_high", party=aggregator)
    ]

# Run the main function
nada_main()