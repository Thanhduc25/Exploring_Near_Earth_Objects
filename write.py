"""Write a stream of close approaches to CSV or to JSON.

This module exports two functions: `write_to_csv` and `write_to_json`, each of
which accept an `results` stream of close approaches and a path to which to
write the data.

These functions are invoked by the main module with the output of the `limit`
function and the filename supplied by the user at the command line. The file's
extension determines which of these functions is used.

You'll edit this file in Part 4.
"""
import csv
import json


def write_to_csv(results, filename):

    """Write an iterable of `CloseApproach` objects to a CSV file.

    The precise output specification is in `README.md`. Roughly, each output row
    corresponds to the information in a single close approach from the `results`
    stream and its associated near-Earth object.

    :param results: An iterable of `CloseApproach` objects.
    :param filename: A Path-like object pointing to where the data should be saved.
    """
    fieldnames = (
        'datetime_utc', 'distance_au', 'velocity_km_s',
        'designation', 'name', 'diameter_km', 'potentially_hazardous'
    )
    # TODO: Write the results to a CSV file, following the specification in the instructions.
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for result in results:
            ca = result[0]
            neo = result[1]

            writer.writerow({
                'datetime_utc': ca.time_str,
                'distance_au': ca.distance,
                'velocity_km_s': ca.velocity,
                'designation': neo.designation,
                'name': neo.name or "",
                'diameter_km': neo.diameter or "",
                'potentially_hazardous': str(neo.hazardous)
            })


def write_to_json(results, filename):
    """Write an iterable of `CloseApproach` objects to a JSON file.

    The precise output specification is in `README.md`. Roughly, the output is a
    list containing dictionaries, each mapping `CloseApproach` attributes to
    their values and the 'neo' key mapping to a dictionary of the associated
    NEO's attributes.

    :param results: An iterable of `CloseApproach` objects.
    :param filename: A Path-like object pointing to where the data should be saved.
    """
    # TODO: Write the results to a JSON file, following the specification in the instructions.
    close_approaches = []

    for result in results:
        ca = result[0]
        neo = result[1]

        close_approach = {
            'close_approach': {
                'datetime_utc': ca.time.isoformat(),
                'distance_au': ca.distance,
                'velocity_km_s': ca.velocity
            },
            'neo': {
                'designation': neo.designation,
                'name': neo.name,
                'diameter_km': neo.diameter or "-",
                'potentially_hazardous': neo.hazardous
            }
        }

        close_approaches.append(close_approach)

    # Write the list of dictionaries to the output JSON file.
    with open(filename, 'w') as f:
        json.dump(close_approaches, f, indent=2)
